"""The student copy (tools/student_bundle.py) must let a child self-check
without giving them any solution or teacher material."""

import os
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

import student_bundle  # noqa: E402

TEACHER_ONLY = ("solution.py", "solution.md", "answer", "lesson", "teacher-guide",
                "assessments", "reference")


@pytest.fixture(scope="module")
def bundle(tmp_path_factory):
    return student_bundle.build_bundle(tmp_path_factory.mktemp("bundle"), sorted(student_bundle.LEVELS))


def test_bundle_has_no_teacher_material(bundle):
    bad = [str(p.relative_to(bundle)) for p in bundle.rglob("*")
           if any(word in p.name for word in TEACHER_ONLY)]
    assert not bad, f"Teacher-only files leaked into the student copy: {bad}"


def test_every_python_exercise_can_self_check(bundle):
    for level in student_bundle.LEVELS.values():
        for readme in (ROOT / level / "exercises").glob("week*/*/README.md"):
            folder = readme.parent
            if not (folder / "starter.py").exists():
                continue  # Scratch / Terminal exercise
            copy = bundle / folder.relative_to(ROOT)
            # Junior children check by matching the picture in the README (no check_my_work.py).
            junior = level.startswith("junior/")
            names = ("README.md", "hints.md", "starter.py") + (() if junior else ("check_my_work.py",))
            for name in names:
                assert (copy / name).is_file(), f"{copy} is missing {name}"
            assert list(copy.glob("test_*.py")), f"{copy} has no tests"
    for name in ("conftest.py", "pytest.ini", "testing/kidtest/checker.py", "START-HERE.txt"):
        assert (bundle / name).is_file(), f"student copy is missing {name}"


def test_self_check_works_without_solutions(bundle, tmp_path):
    """Put the reference answer in place of starter.py in the bundle copy and run
    check_my_work.py the way a child would: every check must pass."""
    folder = "1-introduction/exercises/week07/ex-first-square"
    copy = bundle / folder
    (copy / "starter.py").write_text((ROOT / folder / "solution.py").read_text())
    env = {k: v for k, v in os.environ.items() if k != "KIDCODE_TARGET"}
    proc = subprocess.run([sys.executable, "check_my_work.py"], cwd=copy, env=env,
                          capture_output=True, text=True, timeout=120)
    assert "All" in proc.stdout and "checks passed" in proc.stdout, proc.stdout + proc.stderr
