"""Cross-document consistency checks.

* coverage tables generated from the lesson plans are up to date;
* every lesson objective names at least one level goal, and every level goal
  is taught in at least two sessions;
* every code file a document prints with \\pyfile exists;
* every word in a workbook vocabulary box is in that level's glossary.
"""

import re
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
LEVELS = {1: "1-introduction", 2: "2-intermediate", 3: "3-advanced"}

sys.path.insert(0, str(ROOT / "tools"))
import coverage  # noqa: E402  (tools/coverage.py)


def strip_comments(tex: str) -> str:
    return re.sub(r"(?<!\\)%.*", "", tex)


def test_coverage_tables_are_up_to_date():
    result = subprocess.run([sys.executable, str(ROOT / "tools" / "coverage.py"), "--check"],
                            capture_output=True, text=True)
    assert result.returncode == 0, result.stdout + "\nRun: python3 tools/coverage.py"


@pytest.mark.parametrize("level", sorted(LEVELS))
def test_every_objective_has_a_goal_and_every_goal_is_taught(level):
    lessons = ROOT / LEVELS[level] / "teaching-material" / "lessons"
    taught: dict = {}
    untagged = []
    for path in sorted(lessons.glob("*.tex")):
        for text, goals in coverage.objectives(strip_comments(path.read_text(encoding="utf-8"))):
            if not goals:
                untagged.append(f"{path.name}: {text[:60]}")
            for g in goals:
                taught.setdefault(g, set()).add(path.stem)
    assert not untagged, "Objectives without a goal code:\n" + "\n".join(untagged)
    goals = [code for code, _d, _s in coverage.syllabus_goals(level)]
    thin = {g: sorted(taught.get(g, ())) for g in goals if len(taught.get(g, ())) < 2}
    assert not thin, f"Goals taught in fewer than 2 sessions: {thin}"


def documents():
    for folder in LEVELS.values():
        yield from sorted((ROOT / folder).rglob("*.tex"))


def base_dir(tex: Path) -> Path:
    """\\pyfile paths are relative to the main document's folder."""
    for parent in tex.parents:
        if parent.name in ("teaching-material", "project"):
            return parent
    return tex.parent


@pytest.mark.parametrize("tex", list(documents()), ids=lambda p: str(p.relative_to(ROOT)))
def test_printed_code_files_exist(tex):
    text = strip_comments(tex.read_text(encoding="utf-8"))
    missing = []
    for opts, path in re.findall(r"\\pyfile(\[[^\]]*\])?\{([^}]+)\}", text):
        if not (base_dir(tex) / path).is_file():
            missing.append(path)
    for path in re.findall(r"\\lstinputlisting(?:\[[^\]]*\])?\{([^}]+)\}", text):
        if not (base_dir(tex) / path).is_file():
            missing.append(path)
    assert not missing, f"{tex.name} prints files that do not exist: {missing}"


def _norm(word: str) -> str:
    word = re.sub(r"\\[a-zA-Z]+\*?", " ", word)  # drop macro names like \texttt, keep their text
    word = re.sub(r"[{}|$\\\[\]]", " ", word)
    return " ".join(word.lower().split())


@pytest.mark.parametrize("level", sorted(LEVELS))
def test_workbook_vocabulary_is_in_the_glossary(level):
    tm = ROOT / LEVELS[level] / "teaching-material"
    glossary = _norm(strip_comments((tm / "extras" / "glossary.tex").read_text(encoding="utf-8")))
    missing = []
    for path in sorted((tm / "workbook").glob("*.tex")):
        text = strip_comments(path.read_text(encoding="utf-8"))
        for term in re.findall(r"\\vocabword\{((?:[^{}]|\{[^{}]*\})*)\}", text):
            key = _norm(term)
            key = re.sub(r"\s*\(.*?\)\s*", " ", key).strip()  # "loop (repeat)" -> "loop"
            if key and key not in glossary:
                missing.append(f"{path.stem}: {term}")
    assert not missing, "Add these workbook words to the glossary:\n" + "\n".join(missing)


# Common UK spellings, with the US form to use instead (docs/AUTHORING.md section 8).
UK_TO_US = {
    r"colour": "color",
    r"favourite": "favorite",
    r"behaviour": "behavior",
    r"neighbour": "neighbor",
    r"armour": "armor",
    r"flavour": "flavor",
    r"centre": "center",
    r"\bgrey": "gray",
    r"\bmaths\b": "math",
    r"\bmum\b": "mom",
    r"licence": "license",
    r"labelled": "labeled",
    r"travelled": "traveled",
    r"modelling": "modeling",
    r"\bpractis(e|ed|es|ing)\b": "practice",
    r"\b(organ|recogn|visual|anonym|apolog|initial|summar|custom|memor|random|optim|categor)is(e|ed|es|ing|ation)\b": "-ize",
    r"\banalys(e|ed|ing)\b": "analyze",
    r"\b(elementry|excercises?)\b": "elementary / exercise",
}


def text_files():
    skip = {".pdf", ".png", ".jpg", ".sb3"}
    for path in sorted(ROOT.rglob("*")):
        rel = path.relative_to(ROOT)
        if (path.is_file() and path.suffix not in skip and rel.parts[0] not in
                {".git", ".venv", "build"} and "__pycache__" not in rel.parts
                and path.name != "test_consistency.py"):
            yield path


def test_us_english_spelling():
    bad = []
    for path in text_files():
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for n, line in enumerate(text.splitlines(), 1):
            for pattern, us in UK_TO_US.items():
                m = re.search(pattern, line, re.I)
                if m:
                    bad.append(f"{path.relative_to(ROOT)}:{n}: '{m.group(0)}' -> {us}")
    paths = [str(p.relative_to(ROOT)) for p in text_files()
             if re.search(r"colour|favourite|maths|elementry|excercise", str(p.relative_to(ROOT)))]
    assert not bad and not paths, "Use US English (docs/AUTHORING.md):\n" + "\n".join(bad + paths)
