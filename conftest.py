"""Shared pytest fixtures for every exercise and project in the repo.

Each exercise folder holds starter.py (what the student edits), solution.py
(the reference answer) and test_<name>.py. Tests never import those files by
name; they use the fixtures below, which load the *target* file:

* default / CI:            solution.py        (proves the reference works)
* KIDCODE_TARGET=starter:  starter.py         (used by check_my_work.py)
"""

import os
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "testing"))

from kidtest import feed_inputs, load_module, run_script  # noqa: E402


def pytest_addoption(parser):
    parser.addoption("--gui", action="store_true", default=False,
                     help="also open real turtle windows (macOS smoke run)")


def pytest_configure(config):
    config.addinivalue_line("markers", "gui: opens real turtle windows; run with --gui")


def pytest_collection_modifyitems(config, items):
    if config.getoption("--gui") or os.environ.get("KIDCODE_GUI") == "1":
        return
    skip = pytest.mark.skip(reason="needs --gui (opens real windows)")
    for item in items:
        if "gui" in item.keywords:
            item.add_marker(skip)


def _target_name() -> str:
    return os.environ.get("KIDCODE_TARGET", "solution")


@pytest.fixture
def target_path(request) -> Path:
    """Path of the file under test in this test's folder: solution.py by
    default, starter.py when KIDCODE_TARGET=starter (check_my_work.py)."""
    return Path(request.node.path).parent / f"{_target_name()}.py"


@pytest.fixture
def run_target(target_path):
    """Call ``run_target(inputs=[...], seed=1)`` to run the whole program."""
    def _run(inputs=(), seed=None, cwd=None):
        return run_script(target_path, inputs=inputs, seed=seed, cwd=cwd)
    return _run


@pytest.fixture
def load_target(target_path):
    """Call ``load_target()`` to import the program and test its functions."""
    def _load(inputs=(), seed=None):
        return load_module(target_path, inputs=inputs, seed=seed)
    return _load


@pytest.fixture
def inputs():
    """``with inputs(["7", "yes"]): module.ask()`` answers input() calls."""
    return feed_inputs
