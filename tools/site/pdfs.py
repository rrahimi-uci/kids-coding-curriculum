"""PDF downloads for the website: whole-level documents and one PDF per week.

Whole-level PDFs come from tools/build.py (standard and dyslexia-friendly editions). The per-week
PDF is the student workbook chapter followed by the homework set, compiled from a tiny wrapper that
inputs the same source files, so it is always in sync with the source of truth.
"""
from __future__ import annotations

import hashlib
import os
import shutil
import subprocess
from pathlib import Path

from tools import curriculum

ROOT = Path(__file__).resolve().parents[2]


def ensure_level_pdfs(level_dir: str, stems: list[str], variants=("standard", "dyslexia")) -> dict[str, dict[str, Path]]:
    """Return {stem: {variant: path}} for the requested level documents, building them if needed."""
    out: dict[str, dict[str, Path]] = {}
    sources = list((ROOT / level_dir).rglob("*.tex")) + list((ROOT / "shared" / "latex").glob("*"))
    newest = max((f.stat().st_mtime for f in sources if f.is_file()), default=0)
    for stem in stems:
        for variant in variants:
            found = list((ROOT / "build" / "pdf" / variant / level_dir).rglob(f"{stem}.pdf"))
            if found and found[0].stat().st_mtime < newest:
                found = []  # a source file changed after the PDF was built: rebuild it
            if not found:
                subprocess.run(["python3", str(ROOT / "tools" / "build.py"), "--level", curriculum.by_dir(level_dir).key,
                                "--variant", variant, "--only", stem], cwd=ROOT, check=True,
                               capture_output=True, text=True)
                found = list((ROOT / "build" / "pdf" / variant / level_dir).rglob(f"{stem}.pdf"))
            if found:
                out.setdefault(stem, {})[variant] = found[0]
    return out


def week_pdf(level_num: int, level_dir: str, week: int, dest: Path, cache: Path) -> Path | None:
    """Student workbook chapter + homework for one week (standard edition)."""
    tm = ROOT / level_dir / "teaching-material"
    nn = f"{week:02d}"
    wb, hw = tm / "workbook" / f"week{nn}.tex", tm / "homework" / f"week{nn}.tex"
    if not wb.exists():
        return None
    digest = hashlib.sha1(wb.read_bytes() + (hw.read_bytes() if hw.exists() else b"")
                          + (ROOT / "shared" / "latex" / "kidscode.cls").read_bytes()).hexdigest()[:12]
    cached = cache / f"{level_num}-{nn}-{digest}.pdf"
    if not cached.exists():
        cache.mkdir(parents=True, exist_ok=True)
        tmp = cache / f"tmp-{level_num}-{nn}"
        tmp.mkdir(exist_ok=True)
        (tmp / "week.tex").write_text(
            f"\\documentclass[level={level_num}]{{kidscode}}\n\\begin{{document}}\n"
            f"\\kcinput{{workbook/week{nn}}}\n"
            + (f"\\kcinput{{homework/week{nn}}}\n" if hw.exists() else "")
            + "\\end{document}\n", encoding="utf-8")
        env = dict(os.environ, TEXINPUTS=f"{ROOT / 'shared' / 'latex'}//:{tm}//:" + os.environ.get("TEXINPUTS", ""))
        for _ in range(2):
            p = subprocess.run(["lualatex", "-interaction=nonstopmode", "-halt-on-error", "week.tex"],
                               cwd=tmp, env=env, capture_output=True, text=True, errors="replace")
            if p.returncode != 0:
                raise RuntimeError(f"week PDF failed for level {level_num} week {nn}:\n{p.stdout[-1500:]}")
        shutil.copy2(tmp / "week.pdf", cached)
        shutil.rmtree(tmp, ignore_errors=True)
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(cached, dest)
    return dest
