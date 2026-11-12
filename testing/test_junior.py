"""Junior-track rules (Grades 2-3, docs/JUNIOR-SYLLABUS.md "Junior rules").

A 7-9-year-old has not met negative numbers (Grade 6), coordinates (Grade 5)
or angles in degrees computed from 360 (Grade 4), reads slowly, and a grown-up
reads the pages aloud. These checks keep student-facing junior material short
and inside Grade 2-3 math, and keep each session inside its time.
"""

import re
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import curriculum  # noqa: E402  (tools/curriculum.py)

JUNIOR = curriculum.levels("junior")  # active junior levels only
SESSION_MINUTES = {1: 45, 2: 60, 3: 60}
MAX_WORDS = {"workbook": 350, "homework": 200, "README.md": 200}


def student_files(level):
    tm = level.path / "teaching-material"
    yield from sorted((tm / "workbook").glob("*.tex"))
    yield from sorted((tm / "homework").glob("*.tex"))
    yield from sorted((level.path / "exercises").glob("week*/*/README.md"))
    yield from sorted((level.path / "exercises").glob("week*/*/hints.md"))
    for extra in ("project/project-brief.tex", "teaching-material/extras/cheat-sheet.tex"):
        if (level.path / extra).exists():
            yield level.path / extra


def _blank(match: re.Match) -> str:
    return "\n" * match.group(0).count("\n")  # keep line numbers


def strip_tex(text: str) -> str:
    """Drop comments, TikZ drawings and spacing commands: their coordinates and lengths
    (for example "at (-5,0)" or "\\vspace{-1cm}") are layout, not math a child reads."""
    text = re.sub(r"(?<!\\)%.*", "", text)
    text = re.sub(r"\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}", _blank, text, flags=re.S)
    text = re.sub(r"\\tikz\b[^;]*;", "", text)
    text = re.sub(r"\\[vh]space\*?\{[^}]*\}", "", text)
    return text


def words(text: str) -> int:
    text = strip_tex(text)
    text = re.sub(r"\\begin\{(tikzpicture|scratch)\}.*?\\end\{\1\}", "", text, flags=re.S)
    text = re.sub(r"\\[a-zA-Z]+\*?(\[[^\]]*\])?", "", text)
    return len(re.findall(r"[A-Za-z][A-Za-z'\u2019]*", text))


def ids(level):
    return level.key


PROBLEMS = [
    # a minus sign in front of a number: "-5", "$-5$", "\ovalnum{-5}", but not ranges like "5--10"
    (re.compile(r"(?:(?<=[\s{(:])|^)(?:\$\s*)?[-\u2212]\s?\d"), "a negative number (Grade 6 math)"),
    # a typed or shown position: "x: 0", "go to x: \ovalnum{0}"
    (re.compile(r"\b[xy]:\s*(?:\\ovalnum\{\s*)?[-\u2212]?\d"), "a typed x/y position (use dragging or random position)"),
    # turn = 360 / sides
    (re.compile(r"360\s*(?:\u00f7|/|\\div|divided)"), "360 divided by sides (use a turn card)"),
]


@pytest.mark.parametrize("level", JUNIOR, ids=ids)
def test_student_pages_stay_inside_grade_2_3_math(level):
    bad = []
    for path in student_files(level):
        for n, line in enumerate(strip_tex(path.read_text(encoding="utf-8")).splitlines(), 1):
            for pattern, why in PROBLEMS:
                if pattern.search(line):
                    bad.append(f"{path.relative_to(ROOT)}:{n}: {why}: {line.strip()[:70]}")
    assert not bad, "Junior student pages use math beyond Grade 3:\n" + "\n".join(bad)


@pytest.mark.parametrize("level", JUNIOR, ids=ids)
def test_student_pages_are_short(level):
    long = []
    tm = level.path / "teaching-material"
    for kind in ("workbook", "homework"):
        for path in sorted((tm / kind).glob("*.tex")):
            n = words(path.read_text(encoding="utf-8"))
            if n > MAX_WORDS[kind]:
                long.append(f"{path.relative_to(ROOT)}: {n} words (max {MAX_WORDS[kind]})")
    for path in sorted((level.path / "exercises").glob("week*/*/README.md")):
        n = words(path.read_text(encoding="utf-8"))
        if n > MAX_WORDS["README.md"]:
            long.append(f"{path.relative_to(ROOT)}: {n} words (max {MAX_WORDS['README.md']})")
    assert not long, "Junior pages are read aloud to 7-9-year-olds; keep them short:\n" + "\n".join(long)


@pytest.mark.parametrize("level", JUNIOR, ids=ids)
def test_sessions_fit_their_time(level):
    limit = SESSION_MINUTES[level.number]
    over = []
    for path in sorted((level.path / "teaching-material" / "lessons").glob("*.tex")):
        text = strip_tex(path.read_text(encoding="utf-8"))
        ends = [int(m) for m in re.findall(r"\\timeslot\{\d+\s*--\s*(\d+)\}", text)]
        if not ends or max(ends) != limit:
            over.append(f"{path.name}: timeplan ends at {max(ends) if ends else 'nothing'}, expected {limit}")
    assert not over, "\n".join(over)


@pytest.mark.parametrize("level", JUNIOR, ids=ids)
def test_documents_use_the_junior_class_option(level):
    wrong = []
    for tex in sorted(level.path.rglob("*.tex")):
        head = tex.read_text(encoding="utf-8")[:2000]
        m = re.search(r"\\documentclass\[([^\]]*)\]\{kidscode\}", head)
        if m and not ("track=junior" in m.group(1) and f"level={level.number}" in m.group(1)):
            wrong.append(str(tex.relative_to(ROOT)))
    assert not wrong, f"Use \\documentclass[track=junior,level={level.number}]{{kidscode}} in: {wrong}"


def test_junior_rules_are_tested_once_a_level_is_active():
    """Guard: the checks above silently pass for planned levels, so make sure Level 1 is active."""
    assert any(lv.key == "j1" for lv in JUNIOR), "junior Level 1 should be active in curriculum.json"
