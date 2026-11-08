"""Checks for Exercise 1.3 - Log Reader.

The last check makes a tiny throw-away git project in a temporary folder and
reads its real log. It is skipped if git is not installed yet.
"""

import os
import shutil
import subprocess

import pytest

LOG = """c3c3c3c Add hero jump
b2b2b2b Add hero sprite
a1a1a1a Start game
"""


def git_works():
    if shutil.which("git") is None:
        return False
    try:
        return subprocess.run(["git", "--version"], capture_output=True, timeout=20).returncode == 0
    except (OSError, subprocess.SubprocessError):
        return False


def test_parse_log_makes_a_list_of_commits(load_target):
    reader = load_target()
    commits = reader.parse_log(LOG + "\n\n")
    assert commits == [("c3c3c3c", "Add hero jump"), ("b2b2b2b", "Add hero sprite"), ("a1a1a1a", "Start game")], (
        f"parse_log should give one (id, message) tuple per line and skip empty lines. Got {commits!r}"
    )


def test_count_commits(load_target):
    reader = load_target()
    assert reader.count_commits(LOG) == 3, "This log has 3 commits."
    assert reader.count_commits("") == 0, "An empty log has 0 commits."


def test_find_commits_ignores_capitals(load_target):
    reader = load_target()
    found = reader.find_commits(LOG, "HERO")
    assert found == ["c3c3c3c", "b2b2b2b"], f"Searching for 'HERO' should find the 2 hero commits, but found {found!r}."


def test_oldest_first(load_target):
    reader = load_target()
    story = reader.oldest_first(LOG)
    assert story == ["Start game", "Add hero sprite", "Add hero jump"], (
        f"oldest_first should list the messages from the first commit to the newest. Got {story!r}"
    )


@pytest.mark.skipif(not git_works(), reason="git is not installed on this computer yet")
def test_reads_a_real_git_log(load_target, tmp_path):
    reader = load_target()
    env = dict(os.environ)
    env.update({
        "GIT_CONFIG_GLOBAL": os.devnull, "GIT_CONFIG_NOSYSTEM": "1",
        "GIT_AUTHOR_NAME": "PixelFox", "GIT_AUTHOR_EMAIL": "pixelfox@example.com",
        "GIT_COMMITTER_NAME": "PixelFox", "GIT_COMMITTER_EMAIL": "pixelfox@example.com",
    })

    def git(*args):
        result = subprocess.run(["git", *args], cwd=tmp_path, env=env,
                                capture_output=True, text=True, timeout=60)
        assert result.returncode == 0, result.stderr
        return result.stdout

    git("init", "-q")
    for number, message in enumerate(["Start game", "Add hero", "Add hero jump"]):
        (tmp_path / "game.py").write_text(f"# version {number}\n")
        git("add", "game.py")
        git("commit", "-q", "-m", message)
    log = git("log", "--oneline", "--no-decorate", "--no-color")
    assert reader.count_commits(log) == 3, f"A real git log with 3 commits was read as {reader.count_commits(log)}."
    assert reader.oldest_first(log) == ["Start game", "Add hero", "Add hero jump"], "The real log was not read in the right order."
