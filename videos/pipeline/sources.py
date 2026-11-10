"""Curriculum source discovery and change fingerprints."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Iterable

COMMON_SOURCES = (
    "docs/SYLLABUS.md",
    "1-introduction/teaching-material/teacher-guide.tex",
)


def week_sources(repo_root: Path, week: int) -> tuple[str, ...]:
    """Return every student/teacher source that can affect a week's video."""
    prefix = Path("1-introduction")
    candidates = [
        str(prefix / "teaching-material" / "lessons" / f"week{week:02d}.tex"),
        str(prefix / "teaching-material" / "workbook" / f"week{week:02d}.tex"),
        str(prefix / "teaching-material" / "homework" / f"week{week:02d}.tex"),
    ]
    exercise_dir = repo_root / prefix / "exercises" / f"week{week:02d}"
    if exercise_dir.is_dir():
        for path in sorted(exercise_dir.rglob("*")):
            if path.is_file() and path.suffix in {".md", ".py", ".txt"}:
                candidates.append(str(path.relative_to(repo_root)))
    if week >= 10:
        candidates.extend(
            [
                str(prefix / "project" / "project-brief.tex"),
                str(prefix / "project" / "project-teacher-guide.tex"),
                str(prefix / "project" / "starter" / "README.md"),
                str(prefix / "project" / "starter" / "my_art_show.py"),
            ]
        )
    # Common files are intentionally last so a bounded agent packet always contains
    # the exact weekly lesson, activities, and project material before broad context.
    candidates.extend(COMMON_SOURCES)
    return tuple(dict.fromkeys(candidates))


def digest_files(repo_root: Path, paths: Iterable[str]) -> str:
    digest = hashlib.sha256()
    for relative in sorted(paths):
        path = repo_root / relative
        digest.update(relative.encode("utf-8"))
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def build_manifest(repo_root: Path) -> dict[str, object]:
    weeks: dict[str, object] = {}
    for week in range(1, 13):
        paths = week_sources(repo_root, week)
        weeks[str(week)] = {"digest": digest_files(repo_root, paths), "files": list(paths)}
    return {"schema_version": 1, "level": 1, "algorithm": "sha256", "weeks": weeks}


def write_manifest(repo_root: Path, destination: Path) -> None:
    destination.write_text(
        json.dumps(build_manifest(repo_root), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def stale_weeks(repo_root: Path, manifest_path: Path) -> list[int]:
    expected = json.loads(manifest_path.read_text(encoding="utf-8"))
    current = build_manifest(repo_root)
    return [
        week
        for week in range(1, 13)
        if expected["weeks"][str(week)]["digest"]
        != current["weeks"][str(week)]["digest"]
    ]


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
