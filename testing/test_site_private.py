"""The website's private-content check must catch leaks and pass clean output.

These tests build a tiny fake repository and a fake site, then verify that tools/site/check_private.py
fails when a solution line, a teacher-only marker, a private file name or a solution inside a ZIP would be
published, and passes when only public material is present.
"""
import importlib.util
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("check_private", ROOT / "tools" / "site" / "check_private.py")
cp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cp)

SOLUTION_LINE = "result = compute_the_secret_answer(first_value, second_value) + 42"
STARTER = "# TODO: finish the program\nimport turtle\n"
MANIFEST = {
    "levels": [{"number": 1, "dir": "lvl", "slug": "level-1", "published": True}],
    "public": {
        "workbook": "{dir}/teaching-material/workbook/week[0-9][0-9].tex",
        "homework": "{dir}/teaching-material/homework/week[0-9][0-9].tex",
        "exercise_dirs": "{dir}/exercises/week[0-9][0-9]/*/",
        "parents": {"source": "parents/main.tex", "shared": "parents/shared.tex"},
    },
    "private": {
        "paths": ["answers/", "solution", "test_", "check_my_work", "lesson-plans"],
        "strings": ["TEACHER ONLY", "Teacher script", "Answer key"],
        "fingerprint_sources": ["{dir}/exercises/week*/*/solution.py",
                                "{dir}/teaching-material/answers/*.tex"],
    },
}


def make_repo(tmp: Path) -> Path:
    ex = tmp / "lvl" / "exercises" / "week01" / "ex-a"
    ex.mkdir(parents=True)
    (ex / "README.md").write_text("# Exercise 1.1 - A\nDraw a square with the turtle.\n")
    (ex / "starter.py").write_text(STARTER)
    (ex / "solution.py").write_text(STARTER + SOLUTION_LINE + "\n")
    ans = tmp / "lvl" / "teaching-material" / "answers"
    ans.mkdir(parents=True)
    (ans / "week01.tex").write_text(
        "\\answersweek{1}{A}{b}\nThe teacher should explain that the secret answer is forty-two because of the pattern.\n")
    (tmp / "lvl" / "teaching-material" / "workbook").mkdir(parents=True)
    (tmp / "lvl" / "teaching-material" / "workbook" / "week01.tex").write_text("\\chapterweek{1}{A}{b}\nHello.\n")
    (tmp / "parents").mkdir()
    (tmp / "parents" / "main.tex").write_text("x")
    (tmp / "parents" / "shared.tex").write_text("x")
    return tmp


def make_site(tmp: Path) -> Path:
    d = tmp / "dist"
    (d / "levels").mkdir(parents=True)
    (d / "levels" / "index.html").write_text("<html><body><h1>Week 1</h1><p>Draw a square with the turtle.</p></body></html>")
    return d


def run(tmp_path, mutate=None):
    repo = make_repo(tmp_path / "repo")
    dist = make_site(tmp_path)
    if mutate:
        mutate(dist)
    return cp.check(dist, MANIFEST, repo)


def test_clean_site_passes(tmp_path):
    assert run(tmp_path) == []


def test_solution_line_in_html_is_caught(tmp_path):
    def leak(d):
        (d / "levels" / "index.html").write_text(
            f"<html><body><pre><span>{SOLUTION_LINE.split('=')[0]}</span>= {SOLUTION_LINE.split('=')[1]}</pre></body></html>")
    problems = run(tmp_path, leak)
    assert any("private source" in p for p in problems), problems


def test_teacher_marker_is_caught(tmp_path):
    problems = run(tmp_path, lambda d: (d / "levels" / "index.html").write_text("<p>TEACHER ONLY notes</p>"))
    assert any("TEACHER ONLY" in p for p in problems), problems


def test_private_file_name_is_caught(tmp_path):
    def leak(d):
        (d / "downloads").mkdir()
        (d / "downloads" / "answers").mkdir()
        (d / "downloads" / "answers" / "week01.pdf").write_bytes(b"%PDF-1.4")
    problems = run(tmp_path, leak)
    assert any("private path fragment" in p for p in problems), problems


def test_solution_inside_zip_is_caught(tmp_path):
    def leak(d):
        (d / "downloads").mkdir()
        with zipfile.ZipFile(d / "downloads" / "starter.zip", "w") as z:
            z.writestr("ex-a/solution.py", STARTER + SOLUTION_LINE)
    problems = run(tmp_path, leak)
    assert problems, "a solution.py inside a ZIP must be flagged"


def test_answer_key_sentence_is_caught(tmp_path):
    sentence = "The teacher should explain that the secret answer is forty-two because of the pattern."
    problems = run(tmp_path, lambda d: (d / "levels" / "index.html").write_text(f"<p>{sentence}</p>"))
    assert any("private source" in p for p in problems), problems


def test_video_narration_is_public_but_answers_are_still_caught(tmp_path):
    """A week page shows its video's transcript. A sentence the narration shares with a private source is
    published in the video itself, so it is allowed; answer lines that are not in the narration still fail."""
    import json

    repo = make_repo(tmp_path / "repo")
    narration = "The teacher should explain that the secret answer is forty-two because of the pattern."
    (repo / "videos" / "specs").mkdir(parents=True)
    (repo / "videos" / "specs" / "junior1.json").write_text(
        json.dumps({"videos": [{"scenes": [{"narration": narration}]}]}), encoding="utf-8")
    manifest = {**MANIFEST, "public": {**MANIFEST["public"], "video_scripts": ["videos/specs/junior[0-9].json"]}}
    dist = make_site(tmp_path)
    (dist / "levels" / "index.html").write_text(f"<p>{narration}</p>")
    assert cp.check(dist, manifest, repo) == []
    (dist / "levels" / "index.html").write_text(f"<pre>{SOLUTION_LINE}</pre>")
    assert any("private source" in p for p in cp.check(dist, manifest, repo))
