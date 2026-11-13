"""Repository-wide quality gate: every deliverable exists and follows the
curriculum's teaching-quality rules (see docs/AUTHORING.md).

These checks are mechanical on purpose: they catch a missing homework set,
a lesson without a reflection prompt, or an exercise without tests long
before a student or parent would notice.
"""

import py_compile
import re
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import curriculum  # noqa: E402  (tools/curriculum.py)

# Active levels only (curriculum.json); a planned level has no content to check yet.
LEVEL_INFO = {lv.dir: lv for lv in curriculum.levels()}
LEVELS = list(LEVEL_INFO)


def weeks(level: str) -> list[str]:
    return LEVEL_INFO[level].week_names


def buffers(level: str) -> list[str]:
    return LEVEL_INFO[level].buffer_names

# Teaching-quality rules per track. The junior track (Grades 2-3) has a shorter session with
# its own five phases, "I can" student goals, a play-at-home card instead of three homework
# tiers, and an unplugged activity, bug hunt and safety talk in almost every session
# (grade-2-3/SYLLABUS.md).
RULES = {
    "main": {
        "lesson_envs": ["objectives", "materials", "timeplan", "teacherscript", "analogy",
                        "workedexample", "commonmistakes", "differentiation", "stretchchallenge",
                        "formativecheck", "reflection"],
        "phases": ["Warm-up", "Concept", "Guided demo", "Hands-on build", "Wrap-up"],
        "workbook_envs": ["vocab", "exercise", "reflection"],
        "homework_envs": ["core", "challenge", "creative", "selfcheck"],
        # minimum counts per level (across lessons + buffers)
        "minimums": {"unplugged": 6, "bughunt": 10, "pairroles": 10, "freebuild": 10, "safety": 5},
    },
    "junior": {
        "lesson_envs": ["objectives", "materials", "timeplan", "teacherscript", "analogy",
                        "workedexample", "commonmistakes", "differentiation",
                        "formativecheck", "reflection"],
        "phases": ["Warm-up", "Show me", "Make it", "Wiggle break", "Share"],
        "workbook_envs": ["ican", "vocab", "exercise", "reflection"],
        "homework_envs": ["playathome", "selfcheck"],
        "minimums": {"unplugged": 8, "bughunt": 8, "pairroles": 8, "freebuild": 6, "safety": 8},
    },
}


def rules(level: str) -> dict:
    return RULES[LEVEL_INFO[level].track]

TEACHING = {
    "teacher-guide.tex", "lesson-plans.tex", "student-workbook.tex", "homework.tex",
    "answer-key.tex", "assessments.tex",
}
EXTRAS = {"cheat-sheet.tex", "glossary.tex", "progress-tracker.tex", "parent-notes.tex",
          "certificate.tex"}
PROJECT = {"project-brief.tex", "project-teacher-guide.tex"}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def strip_comments(tex: str) -> str:
    return re.sub(r"(?<!\\)%.*", "", tex)


@pytest.mark.parametrize("level", LEVELS)
def test_level_documents_exist(level):
    tm = ROOT / level / "teaching-material"
    missing = [f for f in TEACHING if not (tm / f).is_file()]
    missing += [f"extras/{f}" for f in EXTRAS if not (tm / "extras" / f).is_file()]
    missing += [f"project/{f}" for f in PROJECT if not (ROOT / level / "project" / f).is_file()]
    w, b = weeks(level), buffers(level)
    for folder, names in [("lessons", w + b), ("workbook", w),
                          ("homework", w), ("answers", w + ["assessments"])]:
        missing += [f"{folder}/{n}.tex" for n in names if not (tm / folder / f"{n}.tex").is_file()]
    assert not missing, f"{level} is missing: {missing}"


@pytest.mark.parametrize("level", LEVELS)
def test_lessons_follow_the_template(level):
    problems = []
    for name in weeks(level) + buffers(level):
        path = ROOT / level / "teaching-material" / "lessons" / f"{name}.tex"
        if not path.exists():
            continue
        tex = strip_comments(read(path))
        for env in rules(level)["lesson_envs"]:
            if f"\\begin{{{env}}}" not in tex:
                problems.append(f"{name}: no {env}")
        for phase in rules(level)["phases"]:
            if phase not in tex:
                problems.append(f"{name}: timeplan lacks phase '{phase}'")
        for block in re.findall(r"\\begin\{objectives\}(.*?)\\end\{objectives\}", tex, re.S):
            for item in re.split(r"\\item\b", block)[1:]:
                if not item.strip().startswith("The student can"):
                    problems.append(f"{name}: objective not phrased 'The student can...': {item.strip()[:50]}")
    assert not problems, "\n".join(problems)


@pytest.mark.parametrize("level", LEVELS)
def test_level_threads_are_present(level):
    lessons = ROOT / level / "teaching-material" / "lessons"
    text = "".join(strip_comments(read(p)) for p in lessons.glob("*.tex"))
    minimums = rules(level)["minimums"]
    counts = {env: text.count(f"\\begin{{{env}}}") for env in minimums}
    short = {env: (n, minimums[env]) for env, n in counts.items() if n < minimums[env]}
    assert not short, f"{level}: (found, needed) {short}"


@pytest.mark.parametrize("level", LEVELS)
def test_workbook_and_homework_shape(level):
    tm = ROOT / level / "teaching-material"
    problems = []
    for week in weeks(level):
        wb, hw = tm / "workbook" / f"{week}.tex", tm / "homework" / f"{week}.tex"
        if wb.exists():
            tex = strip_comments(read(wb))
            problems += [f"workbook/{week}: no {e}" for e in rules(level)["workbook_envs"] if f"\\begin{{{e}}}" not in tex]
        if hw.exists():
            tex = strip_comments(read(hw))
            problems += [f"homework/{week}: no {e}" for e in rules(level)["homework_envs"] if f"\\begin{{{e}}}" not in tex]
    assert not problems, "\n".join(problems)


def exercise_dirs():
    for level in LEVELS:
        base = ROOT / level / "exercises"
        if base.is_dir():
            for d in sorted(base.glob("week*/*")):
                if d.is_dir() and not d.name.startswith(("_", ".")) and d.name != "__pycache__":
                    yield d


@pytest.mark.parametrize("folder", list(exercise_dirs()), ids=lambda d: f"{d.parent.parent.parent.name}/{d.parent.name}/{d.name}")
def test_exercise_folder_is_complete(folder):
    names = {p.name for p in folder.iterdir()}
    if "starter.py" not in names and "README.md" in names:
        text = read(folder / "README.md")
        assert "Expected behavior" in text and "- [ ]" in text, \
            "Scratch exercise README needs an 'Expected behavior' section and a '- [ ]' checklist"
        assert "solution.md" in names, f"{folder} needs a teacher reference solution.md"
        sol = read(folder / "solution.md")
        assert sol.startswith("# Teacher reference:"), "solution.md must start with '# Teacher reference:'"
        assert "TEACHER ONLY" in sol.splitlines()[1] + sol.splitlines()[2], "solution.md needs the TEACHER ONLY banner"
        for heading in ("## The finished project", "## What you should see", "## Check-off list"):
            assert heading in sol, f"solution.md is missing '{heading}'"
        return
    # Junior children check Python work by matching the picture in the README, not with
    # check_my_work.py (grade-2-3/SYLLABUS.md); the tests still check solution.py in CI.
    junior = curriculum.level_of(folder).track == "junior"
    required = ["starter.py", "solution.py", "README.md"] + (["hints.md"] if junior else ["check_my_work.py"])
    for name in required:
        assert name in names, f"{folder} is missing {name}"
    if junior:
        assert "check_my_work.py" not in names, "junior exercises are checked by matching a picture, not check_my_work.py"
        assert "## What you should see" in read(folder / "README.md"), \
            "a junior Python README needs a '## What you should see' section describing the picture"
    assert any(n.startswith("test_") and n.endswith(".py") for n in names), f"{folder} has no test_*.py"


@pytest.mark.parametrize("folder", [d for d in exercise_dirs() if (d / "solution.py").exists()],
                         ids=lambda d: f"{d.parent.parent.parent.name}/{d.parent.name}/{d.name}")
def test_teacher_solution_is_documented(folder):
    """solution.py is the teacher reference: it must say so, explain itself and leave no TODO markers."""
    lines = read(folder / "solution.py").splitlines()
    assert "TEACHER REFERENCE SOLUTION" in "\n".join(lines[:3]), \
        "solution.py must start with a 'TEACHER REFERENCE SOLUTION' header"
    commented = sum(1 for ln in lines if "#" in ln or ln.strip().startswith(('"""', "'''")))
    assert commented >= 8, "solution.py needs explanatory comments for the teacher"
    assert not any(ln.lstrip().startswith("# TODO") for ln in lines), "solution.py still has a starter '# TODO' marker"
    assert max(len(ln) for ln in lines) <= 100, "solution.py has a line longer than 100 characters"
    assert "`" not in "\n".join(lines), "solution.py uses a backtick, which the PDF code font cannot show"


def python_files():
    for level in LEVELS:
        yield from sorted((ROOT / level).rglob("*.py"))


@pytest.mark.parametrize("path", list(python_files()), ids=lambda p: str(p.relative_to(ROOT)))
def test_python_file_compiles_and_is_ascii(path, tmp_path):
    py_compile.compile(str(path), cfile=str(tmp_path / "x.pyc"), doraise=True)
    text = path.read_bytes()
    bad = [i for i, b in enumerate(text) if b > 127]
    assert not bad, f"{path.name} has non-ASCII characters (PDF code font cannot show them) near byte {bad[0]}"
