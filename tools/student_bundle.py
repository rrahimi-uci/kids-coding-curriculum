#!/usr/bin/env python3
"""Make a solution-free copy of the course for a child's Mac.

    python3 tools/student_bundle.py                # every active level
    python3 tools/student_bundle.py --level 1      # one level
    python3 tools/student_bundle.py --out somewhere/

Why: ``check_my_work.py`` lets a child check an exercise alone, but it needs the
exercise's tests and the small ``testing/kidtest`` helper. Until now the only
way to get those onto a Mac was to copy the whole repository, which also
contains every solution, answer key and teacher guide. This script copies only
what a child should have:

* each level's ``exercises/`` folders WITHOUT ``solution.py`` / ``solution.md``
  (README, hints, starter, tests, check_my_work.py and data files stay);
* each level's ``project/starter/`` (never ``project/reference/``);
* ``testing/kidtest/``, ``conftest.py`` and ``pytest.ini`` so the self-check runs;
* a short ``START-HERE.txt`` for the child.

Output: ``build/student-bundle/kids-coding/`` plus ``build/student-bundle/kids-coding.zip``.
Copy the folder (or unzip the ZIP) into the child's Documents folder.
"""

from __future__ import annotations

import argparse
import shutil
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import curriculum  # noqa: E402  (tools/curriculum.py)

# Active levels only: a planned level has no exercises to copy yet.
LEVELS = {lv.key: lv.dir for lv in curriculum.levels()}

# Never copied, anywhere in the bundle.
PRIVATE_NAMES = {"solution.py", "solution.md"}
SKIP_DIRS = {"__pycache__", ".pytest_cache"}
SKIP_SUFFIXES = {".pyc", ".tmp"}

START_HERE = """KIDS CODING - YOUR COURSE FOLDER
================================

Every exercise has its own folder, for example:

    1-introduction/exercises/week07/ex-first-square/

Inside you will find:

    README.md          what to do (open it in Thonny or any text app)
    hints.md           three hints, from a small nudge to a big one
    starter.py         the program YOU change
    check_my_work.py   open it in Thonny and press Run to check your work

How to check your work
----------------------
1. Save starter.py (Cmd+S).
2. Open check_my_work.py in the SAME folder.
3. Press the green Run button.
4. [PASS] means that part works. [TRY AGAIN] comes with a hint.
   Fix one thing, save, and run check_my_work.py again.

Scratch exercises (Level 1, weeks 1 to 6, and every exercise in the junior/
folder) have no check_my_work.py. Use the "Expected behavior" and "Checklist"
in their README.md instead. Junior exercises are read with a grown-up.

check_my_work.py needs a helper called pytest. If it says so, ask a grown-up
to install it once: in Thonny choose Tools > Manage packages..., search for
pytest and press Install.

Please do not move or rename the folders called "testing" or the files
conftest.py and pytest.ini: check_my_work.py needs them.

Bugs are normal. Every programmer meets them every day!
"""


def _copy_tree(src: Path, dst: Path) -> list[Path]:
    """Copy src to dst, leaving out private files and caches. Return copied files."""
    copied = []
    for path in sorted(src.rglob("*")):
        rel = path.relative_to(src)
        if any(part in SKIP_DIRS for part in rel.parts):
            continue
        if path.is_dir():
            continue
        if path.name in PRIVATE_NAMES or path.suffix in SKIP_SUFFIXES or path.name == ".DS_Store":
            continue
        target = dst / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, target)
        copied.append(target)
    return copied


def build_bundle(out: Path, levels: list[str]) -> Path:
    """Write the bundle folder under ``out`` and return its path."""
    bundle = out / "kids-coding"
    if bundle.exists():
        shutil.rmtree(bundle)
    bundle.mkdir(parents=True)

    for key in levels:
        level = LEVELS[key]
        _copy_tree(ROOT / level / "exercises", bundle / level / "exercises")
        _copy_tree(ROOT / level / "project" / "starter", bundle / level / "project" / "starter")

    _copy_tree(ROOT / "testing" / "kidtest", bundle / "testing" / "kidtest")
    for name in ("conftest.py", "pytest.ini"):
        shutil.copy2(ROOT / name, bundle / name)
    (bundle / "START-HERE.txt").write_text(START_HERE, encoding="utf-8")
    return bundle


def zip_bundle(bundle: Path) -> Path:
    zpath = bundle.with_suffix(".zip")
    if zpath.exists():
        zpath.unlink()
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
        for path in sorted(bundle.rglob("*")):
            if path.is_file():
                z.write(path, path.relative_to(bundle.parent))
    return zpath


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--level", choices=sorted(LEVELS), action="append",
                        help="level to include (repeatable); default: all")
    parser.add_argument("--out", type=Path, default=ROOT / "build" / "student-bundle")
    parser.add_argument("--no-zip", action="store_true")
    args = parser.parse_args(argv)
    levels = args.level or sorted(LEVELS)
    bundle = build_bundle(args.out, levels)
    leaked = [p for p in bundle.rglob("*") if p.name in PRIVATE_NAMES]
    if leaked:  # belt and braces: _copy_tree already skips them
        print("Private files found in the bundle:", *leaked, sep="\n  ")
        return 1
    print(f"Student copy: {bundle}")
    if not args.no_zip:
        print(f"ZIP:          {zip_bundle(bundle)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
