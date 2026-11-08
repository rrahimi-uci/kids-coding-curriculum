"""Repository-wide quality gate: every deliverable exists and follows the
curriculum's teaching-quality rules (see docs/AUTHORING.md).

These checks are mechanical on purpose: they catch a missing homework set,
a lesson without a reflection prompt, or an exercise without tests long
before a student or parent would notice.
"""

import py_compile
import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
LEVELS = ["1-elementry", "2-intermediate", "3-advanced"]
WEEKS = [f"week{n:02d}" for n in range(1, 13)]
BUFFERS = ["buffer1", "buffer2"]

LESSON_ENVS = ["objectives", "materials", "timeplan", "teacherscript", "analogy",
               "workedexample", "commonmistakes", "differentiation", "stretchchallenge",
               "formativecheck", "reflection"]
LESSON_PHASES = ["Warm-up", "Concept", "Guided demo", "Hands-on build", "Wrap-up"]
WORKBOOK_ENVS = ["vocab", "exercise", "reflection"]
HOMEWORK_ENVS = ["core", "challenge", "creative", "selfcheck"]
# minimum counts per level (across lessons + buffers)
LEVEL_MINIMUMS = {"unplugged": 6, "bughunt": 10, "pairroles": 10, "freebuild": 10, "safety": 5}

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
    for folder, names in [("lessons", WEEKS + BUFFERS), ("workbook", WEEKS),
                          ("homework", WEEKS), ("answers", WEEKS + ["assessments"])]:
        missing += [f"{folder}/{n}.tex" for n in names if not (tm / folder / f"{n}.tex").is_file()]
    assert not missing, f"{level} is missing: {missing}"


@pytest.mark.parametrize("level", LEVELS)
def test_lessons_follow_the_template(level):
    problems = []
    for name in WEEKS + BUFFERS:
        path = ROOT / level / "teaching-material" / "lessons" / f"{name}.tex"
        if not path.exists():
            continue
        tex = strip_comments(read(path))
        for env in LESSON_ENVS:
            if f"\\begin{{{env}}}" not in tex:
                problems.append(f"{name}: no {env}")
        for phase in LESSON_PHASES:
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
    counts = {env: text.count(f"\\begin{{{env}}}") for env in LEVEL_MINIMUMS}
    short = {env: (n, LEVEL_MINIMUMS[env]) for env, n in counts.items() if n < LEVEL_MINIMUMS[env]}
    assert not short, f"{level}: (found, needed) {short}"


@pytest.mark.parametrize("level", LEVELS)
def test_workbook_and_homework_shape(level):
    tm = ROOT / level / "teaching-material"
    problems = []
    for week in WEEKS:
        wb, hw = tm / "workbook" / f"{week}.tex", tm / "homework" / f"{week}.tex"
        if wb.exists():
            tex = strip_comments(read(wb))
            problems += [f"workbook/{week}: no {e}" for e in WORKBOOK_ENVS if f"\\begin{{{e}}}" not in tex]
        if hw.exists():
            tex = strip_comments(read(hw))
            problems += [f"homework/{week}: no {e}" for e in HOMEWORK_ENVS if f"\\begin{{{e}}}" not in tex]
    assert not problems, "\n".join(problems)


def exercise_dirs():
    for level in LEVELS:
        base = ROOT / level / "excercises"
        if base.is_dir():
            for d in sorted(base.glob("week*/*")):
                if d.is_dir() and not d.name.startswith(("_", ".")) and d.name != "__pycache__":
                    yield d


@pytest.mark.parametrize("folder", list(exercise_dirs()), ids=lambda d: f"{d.parent.parent.parent.name}/{d.parent.name}/{d.name}")
def test_exercise_folder_is_complete(folder):
    names = {p.name for p in folder.iterdir()}
    if "solution.py" not in names and "README.md" in names:
        text = read(folder / "README.md")
        assert "Expected behavior" in text and "- [ ]" in text, \
            "Scratch exercise README needs an 'Expected behavior' section and a '- [ ]' checklist"
        return
    for required in ["starter.py", "solution.py", "check_my_work.py", "README.md"]:
        assert required in names, f"{folder} is missing {required}"
    assert any(n.startswith("test_") and n.endswith(".py") for n in names), f"{folder} has no test_*.py"


def python_files():
    for level in LEVELS:
        yield from sorted((ROOT / level).rglob("*.py"))


@pytest.mark.parametrize("path", list(python_files()), ids=lambda p: str(p.relative_to(ROOT)))
def test_python_file_compiles_and_is_ascii(path, tmp_path):
    py_compile.compile(str(path), cfile=str(tmp_path / "x.pyc"), doraise=True)
    text = path.read_bytes()
    bad = [i for i, b in enumerate(text) if b > 127]
    assert not bad, f"{path.name} has non-ASCII characters (PDF code font cannot show them) near byte {bad[0]}"
