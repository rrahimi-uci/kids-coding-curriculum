"""Curriculum source discovery and change fingerprints."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Iterable

LEVEL_DIR = Path("1-introduction")
MANIFEST_SCHEMA = 2

COMMON_SOURCES = (
    "docs/SYLLABUS.md",
    "1-introduction/teaching-material/teacher-guide.tex",
)

# Files in an exercise folder that a video must never see: answers, the tests that encode them
# and the self-check runner. Keeping them out of the agent packet prevents a script from
# quietly showing a learner the fix they are meant to find; keeping them out of the
# fingerprints means an answer-key correction does not mark a video as stale.
PRIVATE_EXERCISE_FILES = ("solution.py", "solution.md", "check_my_work.py")
PRIVATE_EXERCISE_PREFIXES = ("test_", "smoke_")


def _is_public_exercise_file(path: Path) -> bool:
    if "__pycache__" in path.parts or path.suffix not in {".md", ".py", ".txt", ".csv"}:
        return False
    if path.name in PRIVATE_EXERCISE_FILES:
        return False
    return not path.name.startswith(PRIVATE_EXERCISE_PREFIXES)


def exercise_dirs(repo_root: Path, week: int) -> list[Path]:
    """Exercise folders for one week, relative to the repository root."""
    week_dir = repo_root / LEVEL_DIR / "exercises" / f"week{week:02d}"
    if not week_dir.is_dir():
        return []
    return [path.relative_to(repo_root) for path in sorted(week_dir.iterdir()) if path.is_dir()]


def week_sources(repo_root: Path, week: int) -> tuple[str, ...]:
    """Return every student/teacher source that can affect a week's video."""
    material = LEVEL_DIR / "teaching-material"
    candidates = [
        str(material / "lessons" / f"week{week:02d}.tex"),
        str(material / "workbook" / f"week{week:02d}.tex"),
        str(material / "homework" / f"week{week:02d}.tex"),
    ]
    for folder in exercise_dirs(repo_root, week):
        for path in sorted((repo_root / folder).rglob("*")):
            if path.is_file() and _is_public_exercise_file(path):
                candidates.append(str(path.relative_to(repo_root)))
    if week >= 10:
        candidates.extend(
            [
                str(LEVEL_DIR / "project" / "project-brief.tex"),
                str(LEVEL_DIR / "project" / "project-teacher-guide.tex"),
                str(LEVEL_DIR / "project" / "starter" / "README.md"),
                str(LEVEL_DIR / "project" / "starter" / "my_art_show.py"),
            ]
        )
    # Common files are intentionally last so a bounded agent packet always contains
    # the exact weekly lesson, activities, and project material before broad context.
    candidates.extend(COMMON_SOURCES)
    return tuple(dict.fromkeys(candidates))


def file_digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def digest_files(repo_root: Path, paths: Iterable[str]) -> str:
    """One digest over the names and contents of several files."""
    digest = hashlib.sha256()
    for relative in sorted(paths):
        path = repo_root / relative
        if not path.is_file():
            raise FileNotFoundError(f"curriculum source is missing: {relative}")
        digest.update(relative.encode("utf-8"))
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def week_entry(repo_root: Path, week: int) -> dict[str, object]:
    paths = week_sources(repo_root, week)
    return {
        "digest": digest_files(repo_root, paths),
        "files": {relative: file_digest(repo_root / relative) for relative in paths},
    }


def build_manifest(repo_root: Path) -> dict[str, object]:
    weeks = {str(week): week_entry(repo_root, week) for week in range(1, 13)}
    return {"schema_version": MANIFEST_SCHEMA, "level": 1, "algorithm": "sha256", "weeks": weeks}


def load_manifest(path: Path) -> dict[str, object]:
    manifest = json.loads(path.read_text(encoding="utf-8"))
    if manifest.get("schema_version") != MANIFEST_SCHEMA:
        raise ValueError(
            f"{path.name} uses manifest schema {manifest.get('schema_version')}; "
            f"expected {MANIFEST_SCHEMA}. Run `python -m videos.pipeline.cli accept --all` "
            "after checking the scripts against the current lessons."
        )
    return manifest


def manifest_text(manifest: dict[str, object]) -> str:
    return json.dumps(manifest, indent=2, sort_keys=True) + "\n"


def write_manifest(repo_root: Path, destination: Path) -> None:
    destination.write_text(manifest_text(build_manifest(repo_root)), encoding="utf-8")


def update_manifest_weeks(repo_root: Path, manifest_path: Path, weeks: Iterable[int]) -> None:
    """Record current fingerprints for some weeks only, leaving the others untouched.

    Used after a week's script was regenerated or a teacher confirmed that it still matches
    the lesson. Other weeks keep their old fingerprints, so their drift stays visible.
    """
    if manifest_path.is_file():
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        if manifest.get("schema_version") != MANIFEST_SCHEMA:
            manifest = build_manifest(repo_root)  # old format: nothing reliable to keep
    else:
        manifest = build_manifest(repo_root)
    for week in weeks:
        manifest["weeks"][str(week)] = week_entry(repo_root, week)
    manifest_path.write_text(manifest_text(manifest), encoding="utf-8")


def changed_files(repo_root: Path, manifest_path: Path) -> dict[int, list[str]]:
    """Weeks whose sources changed since the manifest, with the files that changed.

    A file is listed as `+path` when it is new for that week and `-path` when it was removed.
    """
    expected = load_manifest(manifest_path)
    result: dict[int, list[str]] = {}
    for week in range(1, 13):
        old = expected["weeks"][str(week)]
        new = week_entry(repo_root, week)
        if old["digest"] == new["digest"]:
            continue
        old_files, new_files = old["files"], new["files"]
        changes = [path for path in new_files if path in old_files and old_files[path] != new_files[path]]
        changes += [f"+{path}" for path in new_files if path not in old_files]
        changes += [f"-{path}" for path in old_files if path not in new_files]
        result[week] = changes or ["(file list order changed)"]
    return result


def stale_weeks(repo_root: Path, manifest_path: Path) -> list[int]:
    return sorted(changed_files(repo_root, manifest_path))


def source_bundle(repo_root: Path, week: int, max_chars: int = 120_000) -> str:
    """Build a bounded, labeled source packet for an Agent SDK run."""
    sections: list[str] = []
    size = 0
    for relative in week_sources(repo_root, week):
        text = (repo_root / relative).read_text(encoding="utf-8", errors="replace")
        section = f"\n\n===== {relative} =====\n{text}"
        if size + len(section) > max_chars:
            remaining = max_chars - size
            if remaining > 200:
                sections.append(section[:remaining] + "\n[TRUNCATED BY SOURCE BUDGET]")
            break
        sections.append(section)
        size += len(section)
    return "".join(sections)
