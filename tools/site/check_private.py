#!/usr/bin/env python3
"""Fail the build if anything private would be published.

    python3 -m tools.site.check_private [site/dist]

Uses only the standard library (plus PyYAML for the CLI) so it can also run inside the test suite.

Three layers of defence, all driven by site/manifest.yml (deny by default):

1. File names: no published file or ZIP member may contain a private path fragment
   (answers/, solution, test_, check_my_work, lesson-plans, teacher-guide ...).
2. Marker strings: none of the private marker strings (TEACHER ONLY, Teacher script, Answer key ...)
   may appear in any published text, ZIP member or PDF text.
3. Fingerprints: distinctive lines of every private source (solution code, answer keys, teacher
   lessons, assessments) must not appear anywhere in the output. Lines that also occur in public
   sources (starter code, workbooks, READMEs) are ignored, so legitimate shared text is fine.
"""
from __future__ import annotations

import glob
import html
import io
import re
import subprocess
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TEXT_EXT = {".html", ".htm", ".css", ".js", ".mjs", ".json", ".txt", ".xml", ".svg", ".md", ".py", ".csv", ".webmanifest"}
MIN_PY, MIN_TEX = 30, 70


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip().lower()


def strip_tex(line: str) -> str:
    line = re.sub(r"(?<!\\)%.*$", "", line)
    line = re.sub(r"\\[A-Za-z]+\*?(\[[^\]]*\])?", " ", line)
    line = re.sub(r"[{}$\\&~]|\\\\", " ", line)
    return norm(line)


def source_lines(path: Path) -> set[str]:
    out: set[str] = set()
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return out
    if path.suffix == ".py":
        for ln in text.splitlines():
            ln = ln.strip()
            if ln.startswith("#") or len(ln) < MIN_PY:
                continue
            out.add(norm(ln))
    else:
        for ln in text.splitlines():
            if path.suffix == ".tex" and re.match(r"\s*\\(lesson|kcpart|answersweek|chapterweek|homeworkweek)\{", ln):
                continue  # week banners (number, title, big idea) are public everywhere
            t = strip_tex(ln) if path.suffix == ".tex" else norm(ln)
            if len(t) >= MIN_TEX:
                out.add(t)
            if path.suffix == ".tex":  # code listings inside LaTeX keep their raw form
                raw = norm(ln)
                if len(raw) >= MIN_PY and not raw.startswith("%"):
                    out.add(raw)
    return out


def loose(s: str) -> str:
    """Normalize text for substring comparison: drop LaTeX escapes/braces so code in a .tex file matches code in a .py file."""
    s = re.sub(r"\\(?:texttt|py|verb)\b", " ", s)
    s = s.replace("\\_", "_").replace("\\#", "#").replace("\\%", "%").replace("\\&", "&")
    s = re.sub(r"[\\{}$]", " ", s)
    return norm(s)


def html_text(raw: str) -> str:
    raw = re.sub(r"<(script|style)\b.*?</\1>", " ", raw, flags=re.S | re.I)
    raw = re.sub(r"<[^>]+>", " ", raw)
    return html.unescape(raw)


def pdf_text(data: bytes) -> str:
    try:
        p = subprocess.run(["pdftotext", "-", "-"], input=data, capture_output=True)
        return p.stdout.decode("utf-8", "replace")
    except (OSError, ValueError):
        return ""


def collect_output(dist: Path):
    """Yield (label, text) for every published file; ZIP members and PDFs are opened."""
    names: list[str] = []
    for f in sorted(dist.rglob("*")):
        if not f.is_file():
            continue
        rel = f.relative_to(dist).as_posix()
        names.append(rel)
        suf = f.suffix.lower()
        if suf in TEXT_EXT:
            raw = f.read_text(encoding="utf-8", errors="replace")
            yield rel, (html_text(raw) if suf in (".html", ".htm", ".svg") else raw)
        elif suf == ".pdf":
            yield rel, pdf_text(f.read_bytes())
        elif suf == ".zip":
            with zipfile.ZipFile(f) as z:
                for m in z.namelist():
                    names.append(f"{rel}!{m}")
                    if Path(m).suffix.lower() in TEXT_EXT:
                        yield f"{rel}!{m}", z.read(m).decode("utf-8", "replace")
    yield "__names__", "\n".join(names)


def check(dist: Path, manifest: dict, root: Path = ROOT) -> list[str]:
    priv = manifest["private"]
    problems: list[str] = []
    corpus_parts: list[str] = []
    names_blob = ""
    for label, text in collect_output(dist):
        if label == "__names__":
            names_blob = text
            continue
        corpus_parts.append(text)
        for s in priv["strings"]:
            if s.lower() in text.lower():
                problems.append(f"private marker '{s}' found in {label}")
    # 1. file names
    allowed = {a.lower() for a in priv.get("allow_files", [])}
    for name in names_blob.splitlines():
        base = name.split("!")[-1].rsplit("/", 1)[-1].lower()
        if base in allowed:
            continue
        low = "/" + name.lower()
        for frag in priv["paths"]:
            f = frag.lower()
            f = f if f.startswith("/") else "/" + f if f.endswith("/") else f
            if f in low or (not f.startswith("/") and f in low):
                problems.append(f"private path fragment '{frag}' in published file name {name}")
                break
    # 3. fingerprints
    corpus = norm(" ".join(corpus_parts))
    pub = manifest["public"]
    public_parts: list[str] = []
    file_keys = ("workbook", "homework", "project_brief", "cheat_sheet", "glossary", "parent_notes",
                 "progress_tracker", "resources")
    for lvl in manifest["levels"]:
        d = lvl["dir"]
        pats = [pub[k] for k in file_keys if k in pub]
        ex = pub["exercise_dirs"].rstrip("/")
        pats += [ex + "/README.md", ex + "/starter.py", ex + "/hints.md"]
        if "project_starter_dir" in pub:
            sd = pub["project_starter_dir"]
            pats += [sd + "/*.py", sd + "/*.md", sd + "/*/*"]
        for pat in pats:
            for f in glob.glob(str(root / pat.format(dir=d)), recursive=True):
                if Path(f).is_file() and "__pycache__" not in f:
                    public_parts.append(Path(f).read_text(encoding="utf-8", errors="replace"))
    for key in ("source", "shared", "faq"):
        rel = pub["parents"].get(key)
        if rel and (root / rel).exists():
            public_parts.append((root / rel).read_text(encoding="utf-8", errors="replace"))
    syl = root / "docs" / "SYLLABUS.md"
    if syl.exists():
        public_parts.append(syl.read_text(encoding="utf-8"))
    public_blob = loose("\n".join(public_parts))
    checked = 0
    for lvl in manifest["levels"]:
        for pat in priv["fingerprint_sources"]:
            for f in sorted(glob.glob(str(root / pat.format(dir=lvl["dir"])), recursive=True)):
                for line in sorted(source_lines(Path(f))):
                    if loose(line) in public_blob:
                        continue  # the same text is already published on purpose (starter code, workbook, ...)
                    checked += 1
                    if line in corpus:
                        problems.append(f"line from private source {Path(f).relative_to(root)} found in output: '{line[:70]}...'")
                        break
    sys.stderr.write(f"private check: scanned output for {checked} distinctive private lines\n")
    return problems


def main(argv=None) -> int:
    import yaml

    dist = Path((argv or sys.argv[1:] or [str(ROOT / "site" / "dist")])[0])
    if not dist.exists():
        print(f"no such folder: {dist}")
        return 2
    manifest = yaml.safe_load((ROOT / "site" / "manifest.yml").read_text(encoding="utf-8"))
    problems = check(dist, manifest)
    if problems:
        print("PRIVATE CONTENT CHECK FAILED:")
        for p in problems[:40]:
            print("  -", p)
        return 1
    print("private content check passed: no teacher-only or solution material in the site output")
    return 0


if __name__ == "__main__":
    sys.exit(main())
