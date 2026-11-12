"""The junior track (Grades 2-3) on the website: manifest, syllabus, converter, videos and private check.

The converter tests need the site packages (BeautifulSoup, Pygments) and Pandoc, so they are skipped in
the plain test environment; `make site` runs the real conversion of every junior file.
"""
import hashlib
import importlib
import importlib.util
import json
import re
import shutil
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import curriculum  # noqa: E402


def _load(name: str):
    spec = importlib.util.spec_from_file_location(f"site_{name}", ROOT / "tools" / "site" / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


needs_pandoc = pytest.mark.skipif(shutil.which("pandoc") is None, reason="needs Pandoc")


# --------------------------------------------------------------------------- manifest


def test_every_active_level_is_in_the_site_manifest_with_its_track() -> None:
    yaml = pytest.importorskip("yaml")
    manifest = yaml.safe_load((ROOT / "site" / "manifest.yml").read_text(encoding="utf-8"))
    entries = {e["dir"]: e for e in manifest["levels"]}
    for level in curriculum.levels():
        entry = entries.get(level.dir)
        assert entry is not None, f"{level.dir} is active in curriculum.json but not in site/manifest.yml"
        assert entry.get("track", "main") == level.track
        assert entry["number"] == level.number
    slugs = [e["slug"] for e in manifest["levels"]]
    assert len(slugs) == len(set(slugs)), "level slugs must be unique (they are URLs)"
    juniors = [e["slug"] for e in manifest["levels"] if e.get("track") == "junior"]
    assert juniors == ["junior-1", "junior-2", "junior-3"]


def test_junior_private_sources_are_fingerprinted() -> None:
    yaml = pytest.importorskip("yaml")
    manifest = yaml.safe_load((ROOT / "site" / "manifest.yml").read_text(encoding="utf-8"))
    pats = manifest["private"]["fingerprint_sources"]
    for level in curriculum.levels("junior"):
        found = {p: [f for f in ROOT.glob(p.format(dir=level.dir))] for p in pats}
        assert found["{dir}/exercises/week*/*/solution.md"], level.dir
        assert found["{dir}/teaching-material/answers/*.tex"], level.dir
        assert found["{dir}/teaching-material/lessons/*.tex"], level.dir
        assert found["{dir}/teaching-material/extras/certificate.tex"], level.dir


# --------------------------------------------------------------------------- syllabus


@needs_pandoc
def test_the_junior_syllabus_is_parsed_like_the_main_one() -> None:
    syllabus = _load("syllabus")
    junior = syllabus.parse("docs/JUNIOR-SYLLABUS.md")
    assert [junior[n]["name"] for n in (1, 2, 3)] == ["Little Robots", "Game Makers", "Bridge to Python"]
    for level in curriculum.levels("junior"):
        data = junior[level.number]
        assert [w["n"] for w in data["weeks"]] == list(range(1, level.weeks + 1))
        assert data["goals"] and all(g["code"].startswith(level.goal_prefix + ".G") for g in data["goals"])
        assert data["project_title"] and data["tools"]
    main = syllabus.parse()
    assert [main[n]["name"] for n in (1, 2, 3)] == ["Introduction", "Intermediate", "Advanced"]


# --------------------------------------------------------------------------- converter


@pytest.fixture(scope="module")
def texconv():
    pytest.importorskip("bs4")
    pytest.importorskip("pygments")
    if shutil.which("pandoc") is None:
        pytest.skip("needs Pandoc")
    sys.path.insert(0, str(ROOT))
    return importlib.import_module("tools.site.texconv")


def _html(texconv, tex: str) -> str:
    prepared, res = texconv.prepare(tex, "test.tex")
    return texconv.post_process(texconv.run_pandoc(prepared), res, {}, {})


def test_junior_boxes_become_labeled_callouts(texconv) -> None:
    html = _html(texconv, r"""
\section{What you will learn}
\begin{ican}
  \item I can snap blocks together.
\end{ican}
\begin{grownup}[Bringing the cat back]
Drag the cat back with the mouse.
\end{grownup}
\begin{playathome}[Puppet show]
Read the cards aloud.
\end{playathome}
""")
    assert 'class="callout callout-ican"' in html and "I can snap blocks together." in html
    assert re.search(r'callout-grownup.*?callout-label">For the grown-up<.*?Bringing the cat back', html, re.S)
    assert re.search(r'callout-playathome.*?callout-label">Play at home \(5\u201310 minutes, with a grown-up\)<.*?Puppet show',
                     html, re.S)
    assert "\\begin" not in html and "\\item" not in html


def test_the_learning_goals_come_from_the_i_can_list(texconv) -> None:
    pytest.importorskip("yaml")
    build = importlib.import_module("tools.site.build")
    html = _html(texconv, "\\section{What you will learn}\n\\begin{ican}\n\\item I can find the sprite.\n"
                          "\\item I can click the green flag.\n\\end{ican}\n\\section{Meet Scratch}\nHello.\n")
    goals, rest = build.extract_objectives(html)
    assert goals == ["I can find the sprite.", "I can click the green flag."]
    assert "callout-ican" not in rest and "Meet Scratch" in rest


def test_an_assessment_checklist_is_never_converted(texconv) -> None:
    with pytest.raises(ValueError, match="show-me checklist"):
        texconv.prepare("\\begin{showme}[Week 5]\n\\showmerow{Puts arrow cards in order}\n\\end{showme}\n", "x.tex")


def test_junior_cheat_sheet_rows_and_twin_table(texconv) -> None:
    html = _html(texconv, r"""\documentclass[track=junior,level=3]{kidscode}
\newcommand{\cat}[5]{#1 #2 #3 #4 #5}
\newcolumntype{S}{>{\RaggedRight}m{3cm}}
\begin{document}
\sheethead{Blocks}
\cat{scevents}{\faFlag}{Events}{yellow: start}{Start blocks.}
\begin{tabular}{@{}SS@{}}
Move & \pyl{t.forward(100)}\pyl{t.left(90)}\\
\multicolumn{2}{@{}>{\RaggedRight}m{5cm}}{\pyl{for i in range(4):}\pyin{t.forward(100)}}\\
\end{tabular}
\end{document}""")
    assert re.search(r"<h3[^>]*>Events</h3>", html) and "yellow: start" in html
    assert 'class="swatch" style="background:#FFBF00"' in html
    assert "<table" in html and "\\pyl" not in html
    assert "<code>t.forward(100)</code>" in html and "<code>t.left(90)</code>" in html
    assert 'colspan="2"' in html


def test_three_argument_word_book_entries_are_read(tmp_path) -> None:
    pytest.importorskip("bs4")
    if shutil.which("pandoc") is None:
        pytest.skip("needs Pandoc")
    sys.path.insert(0, str(ROOT))
    extras = importlib.import_module("tools.site.extras")
    path = tmp_path / "glossary.tex"
    path.write_text("\\documentclass[track=junior,level=2]{kidscode}\n\\newcommand{\\gl}[3]{#1 #2 #3}\n"
                    "\\begin{document}\n\\kctitle{Word Book}{x}\n\\gl{score}{W3}{A number that counts points.}\n"
                    "\\gl{arcade}{W10}{A place with lots of games.}\n\\end{document}\n", encoding="utf-8")
    entries = extras.parse_glossary(path)
    assert [(e["key"], e["where"], e["example"]) for e in entries] == [("arcade", "W10", ""), ("score", "W3", "")]


# --------------------------------------------------------------------------- videos


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _listing(folder: Path, key: str, stem: str) -> dict:
    names = [f"{stem}.mp4", f"{stem}.jpg", f"{stem}.vtt"]
    (folder / names[0]).write_bytes(b"\x00" * 1000)
    (folder / names[1]).write_bytes(b"jpeg")
    (folder / names[2]).write_text("WEBVTT\n\n00:00:01.000 --> 00:00:02.000\nHi, I am Aiden!\n", encoding="utf-8")
    return {"videos": {key: {"video": names[0], "poster": names[1], "captions": names[2], "seconds": 150,
                             "bytes": 1000, "sha256": {n: _sha(folder / n) for n in names}}}}


@pytest.fixture
def sv(tmp_path, monkeypatch):
    module = _load("videos")
    monkeypatch.setattr(module, "PUBLIC", tmp_path / "public" / "videos")
    monkeypatch.setattr(module, "CACHE", tmp_path / "cache")
    folder = tmp_path / "release"
    folder.mkdir()
    monkeypatch.setenv("SITE_VIDEOS", str(folder))
    return module, folder


def test_junior_videos_come_from_their_own_list(sv) -> None:
    module, folder = sv
    (folder / "videos.json").write_text(json.dumps(_listing(folder, "1-2", "level1-week02")), encoding="utf-8")
    (folder / "junior-videos.json").write_text(json.dumps(_listing(folder, "j1-2", "junior1-week02")), encoding="utf-8")
    warnings: list[str] = []
    found = module.collect(warnings, (module.MANIFEST, module.JUNIOR_MANIFEST))
    assert warnings == []
    assert set(found) == {(1, 2), ("j1", 2)}
    assert found[("j1", 2)]["src"] == "%BASE%videos/junior1-week02.mp4"
    assert found[("j1", 2)]["transcript"] == ["Hi, I am Aiden!"]


def test_a_missing_junior_list_leaves_the_main_videos_in_place(sv) -> None:
    module, folder = sv
    (folder / "videos.json").write_text(json.dumps(_listing(folder, "1-2", "level1-week02")), encoding="utf-8")
    warnings: list[str] = []
    found = module.collect(warnings, (module.MANIFEST, module.JUNIOR_MANIFEST))
    assert set(found) == {(1, 2)}
    assert len(warnings) == 1 and "junior-videos.json" in warnings[0]


# --------------------------------------------------------------------------- private check


def test_a_junior_scratch_solution_leak_is_caught(tmp_path) -> None:
    cp = _load("check_private")
    repo = tmp_path / "repo"
    ex = repo / "junior" / "1-robots" / "exercises" / "week02" / "ex-a"
    ex.mkdir(parents=True)
    (ex / "README.md").write_text("# Exercise 2.1 - A\nMake the cat say hi.\n")
    (ex / "solution.md").write_text("The finished script snaps when green flag clicked, then say Hello for two seconds, then move ten steps.\n")
    (repo / "parents").mkdir()
    for name in ("main.tex", "shared.tex"):
        (repo / "parents" / name).write_text("x")
    manifest = {
        "levels": [{"number": 1, "dir": "junior/1-robots", "slug": "junior-1", "track": "junior", "published": True}],
        "public": {"exercise_dirs": "{dir}/exercises/week[0-9][0-9]/*/",
                   "parents": {"source": "parents/main.tex", "shared": "parents/shared.tex"}},
        "private": {"paths": ["solution"], "strings": ["TEACHER ONLY"],
                    "fingerprint_sources": ["{dir}/exercises/week*/*/solution.md"]},
    }
    dist = tmp_path / "dist"
    (dist / "levels").mkdir(parents=True)
    page = dist / "levels" / "index.html"
    page.write_text("<p>Make the cat say hi.</p>")
    assert cp.check(dist, manifest, repo) == []
    page.write_text("<p>The finished script snaps when green flag clicked, then say Hello for two seconds, "
                    "then move ten steps.</p>")
    assert any("private source" in p for p in cp.check(dist, manifest, repo))


def test_a_lesson_line_in_video_captions_is_still_flagged(tmp_path) -> None:
    cp = _load("check_private")
    repo = tmp_path / "repo"
    lessons = repo / "junior" / "2-games" / "teaching-material" / "lessons"
    lessons.mkdir(parents=True)
    line = "My game is called Banana Drop. You are the Bowl. Use the arrow keys to catch ten bananas."
    (lessons / "week10.tex").write_text(f"\\item {line}\n")
    (repo / "parents").mkdir()
    for name in ("main.tex", "shared.tex"):
        (repo / "parents" / name).write_text("x")
    manifest = {
        "levels": [{"number": 2, "dir": "junior/2-games", "slug": "junior-2", "track": "junior", "published": True}],
        "public": {"exercise_dirs": "{dir}/exercises/week[0-9][0-9]/*/",
                   "parents": {"source": "parents/main.tex", "shared": "parents/shared.tex"}},
        "private": {"paths": ["solution"], "strings": ["TEACHER ONLY"],
                    "fingerprint_sources": ["{dir}/teaching-material/lessons/*.tex"]},
    }
    dist = tmp_path / "dist"
    (dist / "levels").mkdir(parents=True)
    (dist / "levels" / "index.html").write_text(f"<details><p>{line}</p></details>")
    assert any("private source" in p for p in cp.check(dist, manifest, repo))
    (dist / "videos").mkdir()
    (dist / "videos" / "junior2-week10.vtt").write_text(
        "WEBVTT\n\n00:00:01.000 --> 00:00:03.000\nMy game is called Banana Drop. You are the Bowl.\n\n"
        "00:00:03.100 --> 00:00:05.000\nUse the arrow keys to catch ten bananas.\n", encoding="utf-8")
    assert any("private source" in p for p in cp.check(dist, manifest, repo)), \
        "captions are not public text: reword the lesson line instead of loosening the check"
