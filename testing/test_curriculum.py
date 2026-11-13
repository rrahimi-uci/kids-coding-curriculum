"""curriculum.json is the one place that says which tracks and levels exist.

These checks keep it honest: every level has a home folder and a syllabus
section whose goals and week list match the config, and no tool falls back
to a hard-coded list of level folders or twelve weeks.
"""

import json
import re
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import coverage  # noqa: E402  (tools/coverage.py)
import curriculum  # noqa: E402  (tools/curriculum.py)

ALL = curriculum.levels(include_planned=True)


def test_config_loads_and_has_both_tracks():
    tracks = {t.id: t for t in curriculum.load()}
    assert set(tracks) == {"main", "junior"}
    # Each track is a grade band with its own top-level folder, youngest first.
    assert [t.dir for t in curriculum.tracks()] == ["grade-2-3", "grade-4-6"]
    assert tracks["junior"].band_title == "Grades 2\u20133"
    assert tracks["main"].band_title == "Grades 4\u20136"
    assert [lv.title for lv in curriculum.levels("main")] == ["Introductory", "Intermediate", "Advanced"]
    assert [lv.key for lv in curriculum.levels("main")] == ["1", "2", "3"]
    assert [lv.key for lv in curriculum.levels("junior", include_planned=True)] == ["j1", "j2", "j3"]


def test_planned_levels_are_left_out_by_default():
    assert all(lv.active for lv in curriculum.levels())
    planned = [lv for lv in ALL if not lv.active]
    assert not set(planned) & set(curriculum.levels())


def test_lookups():
    assert curriculum.by_key("2").dir == "grade-4-6/2-intermediate"
    assert curriculum.by_key("2").band == "grade-4-6" and curriculum.by_key("2").slug == "level-2"
    assert curriculum.by_dir("grade-2-3/1-little-robots").key == "j1"
    assert curriculum.level_of(ROOT / "grade-4-6" / "1-introductory" / "exercises").key == "1"
    assert curriculum.level_of(ROOT / "grade-2-3" / "3-bridge-to-python" / "README.md").key == "j3"
    with pytest.raises(KeyError):
        curriculum.by_key("9")


def test_bad_config_is_rejected(tmp_path):
    data = json.loads(curriculum.CONFIG.read_text(encoding="utf-8"))
    data["tracks"][0]["levels"][0]["key"] = "1"          # duplicate of a main-track key
    data["tracks"][0]["levels"][1]["status"] = "maybe"   # not a known status
    data["tracks"][0]["levels"][2]["dir"] = "grade-4-6/3-bridge-to-python"  # outside its band folder
    bad = tmp_path / "curriculum.json"
    bad.write_text(json.dumps(data), encoding="utf-8")
    with pytest.raises(ValueError, match="status must be.*must be inside the track folder.*duplicate key"):
        curriculum.load(bad)


@pytest.mark.parametrize("track", curriculum.tracks(), ids=lambda t: t.dir)
def test_each_band_folder_holds_its_syllabus_readme_and_levels(track):
    assert track.path.is_dir(), f"{track.dir}/ does not exist"
    assert (track.path / "README.md").is_file(), f"{track.dir}/ needs a README.md"
    assert track.syllabus == f"{track.dir}/SYLLABUS.md" and (ROOT / track.syllabus).is_file()
    assert all(lv.dir.startswith(track.dir + "/") for lv in track.levels)


def test_no_level_folder_is_left_outside_the_band_folders():
    """The old flat layout (1-introduction/, junior/ ...) must not come back."""
    stray = [p.name for p in ROOT.iterdir() if p.is_dir() and re.match(r"\d-|junior$", p.name)]
    assert not stray, f"level folders belong inside grade-2-3/ or grade-4-6/: {stray}"


@pytest.mark.parametrize("level", ALL, ids=lambda lv: lv.key)
def test_level_has_a_folder_and_readme(level):
    assert level.path.is_dir(), f"{level.dir} does not exist"
    if not level.active:
        assert (level.path / "README.md").is_file(), f"planned level {level.dir} needs a README.md"


@pytest.mark.parametrize("level", ALL, ids=lambda lv: lv.key)
def test_syllabus_matches_the_config(level):
    """The track syllabus has this level's goal table and exactly `weeks` week rows, numbered 1..N."""
    assert coverage.syllabus_goals(level), f"{level.syllabus} has no {level.goal_prefix}.G* goal rows"
    text = (ROOT / level.syllabus).read_text(encoding="utf-8")
    section = re.search(rf"^### Level {level.number} weeks\n(.*?)(?=^\*\*Level {level.number} final project)",
                        text, re.M | re.S)
    assert section, f"{level.syllabus} has no '### Level {level.number} weeks' table"
    weeks = [int(n) for n in re.findall(r"^\| (\d+) \|", section.group(1), re.M)]
    assert weeks == list(range(1, level.weeks + 1)), \
        f"{level.syllabus} level {level.number} lists weeks {weeks}, curriculum.json says {level.weeks}"


HARD_CODED = [
    re.compile(r"""\{\s*["']?1["']?\s*:\s*["'](?:grade-4-6/)?1-introduct\w+["']"""),  # a level-folder dict
    re.compile(r"""\[\s*["'](?:grade-4-6/)?1-introduct\w+["']\s*,"""),                # a level-folder list
    re.compile(r"range\(1,\s*13\)"),                                   # twelve weeks baked in
    re.compile(r"""split\(["']-["']\)\[0\]"""),                         # level key guessed from a folder name
]


@pytest.mark.parametrize("path", ["tools/build.py", "tools/coverage.py", "tools/student_bundle.py",
                                  "tools/site/build.py", "tools/site/pdfs.py", "tools/site/videos.py",
                                  "videos/pipeline/sources.py",
                                  "testing/test_repo_structure.py", "testing/test_consistency.py",
                                  "testing/test_smoke_gui.py"])
def test_tools_read_levels_from_the_config(path):
    text = (ROOT / path).read_text(encoding="utf-8")
    found = [p.pattern for p in HARD_CODED if p.search(text)]
    assert not found, f"{path} hard-codes the level list or week count; use tools/curriculum.py"
