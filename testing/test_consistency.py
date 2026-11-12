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
sys.path.insert(0, str(ROOT / "tools"))
import coverage  # noqa: E402  (tools/coverage.py)
import curriculum  # noqa: E402  (tools/curriculum.py)

# Active levels of every track, keyed by their CLI key ("1", "2", "3", later "j1", ...).
LEVEL_INFO = {lv.key: lv for lv in curriculum.levels()}
LEVELS = {key: lv.dir for key, lv in LEVEL_INFO.items()}


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
    goals = [code for code, _d, _s in coverage.syllabus_goals(LEVEL_INFO[level])]
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
    r"labelled(?!by)": "labeled",  # aria-labelledby is an HTML attribute, not UK spelling
    r"travelled": "traveled",
    r"modelling": "modeling",
    r"\bpractis(e|ed|es|ing)\b": "practice",
    r"\b(organ|recogn|visual|anonym|apolog|initial|summar|custom|memor|random|optim|categor)is(e|ed|es|ing|ation)\b": "-ize",
    r"\banalys(e|ed|ing)\b": "analyze",
    r"\b(elementry|excercises?)\b": "elementary / exercise",
}


def _authored_paths():
    """Files that are authored (tracked or new, not git-ignored): generated output, virtual
    environments and node_modules are never checked."""
    import subprocess

    try:
        out = subprocess.run(["git", "ls-files", "-co", "--exclude-standard"], cwd=ROOT, capture_output=True,
                             text=True, check=True).stdout.splitlines()
        return [ROOT / line for line in out]
    except (OSError, subprocess.CalledProcessError):  # not a git checkout: fall back to a plain walk
        skip_dirs = {".git", ".venv", ".venv-site", "node_modules", "build", "dist", "generated", ".astro", "__pycache__"}
        return [p for p in ROOT.rglob("*") if not skip_dirs & set(p.relative_to(ROOT).parts)]


def text_files():
    skip = {".pdf", ".png", ".jpg", ".sb3", ".woff2", ".webp", ".zip", ".svg"}
    for path in sorted(_authored_paths()):
        if (path.is_file() and path.suffix not in skip and "__pycache__" not in path.parts
                and path.name not in ("test_consistency.py", "package-lock.json")):
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


# --------------------------------------------------------------------------------------
# Partial code listings: \pyfile[firstline=A,lastline=B]{file} must print whole code blocks.
# The line numbers go stale silently when a solution file is edited, which once printed half a
# function in the answer key, so check where each range starts and stops.
import re as _re

_PYFILE = _re.compile(r"\\pyfile\[([^\]]*firstline=(\d+)[^\]]*)\]\{([^}]+)\}")


def _pyfile_ranges():
    for tex in sorted(ROOT.rglob("*.tex")):
        if "generated" in tex.parts:
            continue
        for m in _PYFILE.finditer(tex.read_text(encoding="utf-8")):
            opts, first = m.group(1), int(m.group(2))
            last = _re.search(r"lastline=(\d+)", opts)
            # LaTeX finds these files relative to the including document or any folder above it
            candidates = [(d / m.group(3)).resolve() for d in [tex.parent, *tex.parents] if (d / m.group(3)).exists()]
            yield tex, candidates[0] if candidates else (tex.parent / m.group(3)), first, int(last.group(1)) if last else None


@pytest.mark.parametrize("tex,src,first,last", list(_pyfile_ranges()),
                         ids=lambda v: v.name if hasattr(v, "name") else str(v))
def test_pyfile_ranges_print_whole_blocks(tex, src, first, last):
    lines = src.read_text(encoding="utf-8").splitlines()
    last = last or len(lines)
    assert 1 <= first <= last <= len(lines), f"{tex.name}: line range {first}-{last} is outside {src.name}"
    start = lines[first - 1]
    indent0 = len(start) - len(start.lstrip())
    assert start.lstrip().startswith(("def ", "class ", "@", "#", "import ", "from ", '"""')) or not start.strip(), \
        f"{tex.name}: the listing of {src.name} starts inside a block (line {first}: {start.strip()[:50]!r})"
    rest = [ln for ln in lines[last:] if ln.strip()]
    if rest:  # the first line that is NOT printed must not belong to the block that was printed
        nxt = rest[0]
        assert len(nxt) - len(nxt.lstrip()) <= indent0, \
            f"{tex.name}: the listing of {src.name} stops inside a block (next line: {nxt.strip()[:50]!r})"
