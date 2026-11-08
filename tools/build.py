#!/usr/bin/env python3
"""Build every curriculum PDF (standard + dyslexia-friendly editions).

    python3 tools/build.py                 # everything, both variants
    python3 tools/build.py --level 1       # one level
    python3 tools/build.py --variant standard --only lesson-plans
    python3 tools/build.py --jobs 6

A "main document" is any .tex file under a level folder that contains
\\documentclass. Each is compiled with LuaLaTeX from its own folder (so
relative \\pyfile paths to tested code work), twice for page references.
PDFs land in build/pdf/<variant>/<level>/<name>.pdf.
"""

from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LEVELS = {"1": "1-introduction", "2": "2-intermediate", "3": "3-advanced"}
VARIANTS = ("standard", "dyslexia")
OVERFULL_PT = 5.0  # report lines wider than the text block by more than this (about 2 mm)


def find_documents(levels, only):
    docs = []
    for key in levels:
        for tex in sorted((ROOT / LEVELS[key]).rglob("*.tex")):
            head = tex.read_text(encoding="utf-8", errors="ignore")[:4000]
            if re.search(r"^\s*\\documentclass", head, re.M) and (not only or only in tex.stem):
                docs.append(tex)
    return docs


def compile_one(tex: Path, variant: str, tag: str) -> tuple[Path, str, bool, str]:
    level = next(p for p in tex.relative_to(ROOT).parts)
    base = ROOT / "build" / tag if tag else ROOT / "build"
    out_dir = base / "pdf" / variant / level
    aux_dir = base / "aux" / variant / level / tex.parent.relative_to(ROOT / level)
    out_dir.mkdir(parents=True, exist_ok=True)
    aux_dir.mkdir(parents=True, exist_ok=True)
    job = tex.stem
    if variant == "dyslexia":
        source = f"\\def\\kcvariant{{dyslexia}}\\input{{{tex.name}}}"
    else:
        source = tex.name
    env = dict(os.environ)
    env["TEXINPUTS"] = f"{ROOT / 'shared' / 'latex'}//:{tex.parent}//:" + env.get("TEXINPUTS", "")
    cmd = ["lualatex", "-interaction=nonstopmode", "-halt-on-error", "-file-line-error",
           f"-output-directory={aux_dir}", f"-jobname={job}", source]
    log = ""
    ok = True
    # Up to 3 passes: the table of contents can shift pages, so "Page X of Y"
    # and references only settle after the page count is stable.
    for attempt in range(3):
        proc = subprocess.run(cmd, cwd=tex.parent, env=env, capture_output=True, text=True,
                              errors="replace", timeout=900)
        if proc.returncode != 0:
            ok = False
            log = proc.stdout[-4000:]
            break
        if attempt >= 1 and "Rerun" not in proc.stdout and "rerun" not in proc.stdout:
            break
    if ok:
        shutil.copy2(aux_dir / f"{job}.pdf", out_dir / f"{job}.pdf")
        logtext = (aux_dir / f"{job}.log").read_text(errors="replace")
        warnings = [w for w in re.findall(r"^(?:LaTeX|Package \w+) Warning:.*$", logtext, re.M)
                    if "undefined" in w or "Reference" in w or "multiply" in w]
        missing = sorted(set(re.findall(r"Missing character: There is no (.+?) in font", logtext)))
        # Lines sticking out of the margin by more than OVERFULL_PT are visible on paper.
        wide = [float(pt) for pt in re.findall(r"Overfull \\hbox \(([0-9.]+)pt too wide\)", logtext)
                if float(pt) > OVERFULL_PT]
        notes = []
        if wide:
            notes.append(f"{len(wide)} line(s) too wide for the page (worst {max(wide):.0f}pt)")
        if warnings:
            notes.append(f"{len(warnings)} reference warning(s): {warnings[0][:120]}")
        if missing:
            notes.append(f"missing glyphs: {', '.join(missing[:8])}")
        log = "; ".join(notes)
    return tex, variant, ok, log


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--level", choices=sorted(LEVELS), action="append")
    parser.add_argument("--variant", choices=VARIANTS, action="append")
    parser.add_argument("--only", help="substring of the document file name")
    parser.add_argument("--jobs", type=int, default=max(2, (os.cpu_count() or 4) // 2))
    parser.add_argument("--tag", default="", help="separate build folder (build/<tag>/) for parallel builds")
    parser.add_argument("--strict", action="store_true", help="fail on missing glyphs, bad refs or lines too wide for the page")
    args = parser.parse_args()

    if shutil.which("lualatex") is None:
        print("lualatex not found. Install MacTeX (see README.md) and try again.")
        return 2
    docs = find_documents(args.level or sorted(LEVELS), args.only)
    variants = args.variant or list(VARIANTS)
    jobs = [(d, v) for d in docs for v in variants]
    print(f"Building {len(jobs)} PDFs with {args.jobs} parallel jobs...")
    failures, notes = [], []
    with ThreadPoolExecutor(max_workers=args.jobs) as pool:
        for tex, variant, ok, log in pool.map(lambda j: compile_one(j[0], j[1], args.tag), jobs):
            rel = tex.relative_to(ROOT)
            if ok:
                print(f"  ok   [{variant:9}] {rel}" + (f"   ({log})" if log else ""))
                if log:
                    notes.append((rel, variant, log))
            else:
                print(f"  FAIL [{variant:9}] {rel}")
                failures.append((rel, variant, log))
    for rel, variant, log in failures:
        print(f"\n===== {rel} [{variant}] =====\n{log}")
    print(f"\n{len(jobs) - len(failures)}/{len(jobs)} PDFs built into build/{args.tag + '/' if args.tag else ''}pdf/")
    if failures or (args.strict and notes):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
