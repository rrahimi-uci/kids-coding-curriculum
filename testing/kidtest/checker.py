"""Friendly "check my work" runner used by every exercise's check_my_work.py.

A student opens ``check_my_work.py`` in Thonny and presses Run (F5). This runs
the exercise's tests against *their* ``starter.py`` and prints a short,
encouraging summary instead of pytest's wall of text.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path


def _repo_root(start: Path) -> Path:
    for parent in [start, *start.parents]:
        if (parent / "pytest.ini").is_file() and (parent / "testing" / "kidtest").is_dir():
            return parent
    return start


def check_folder(folder, target: str = "starter") -> int:
    folder = Path(folder).resolve()
    try:
        import pytest
    except ImportError:
        print("I need a helper called pytest to check your work.")
        print("In Thonny: Tools > Manage packages... > type pytest > Search > Install.")
        print("(Ask your teacher if you are not sure. No account is needed.)")
        return 2

    class Collector:
        def __init__(self):
            self.passed, self.failed = [], []

        def pytest_runtest_logreport(self, report):
            if report.when == "call" or (report.when == "setup" and report.failed):
                name = report.nodeid.split("::")[-1].replace("test_", "", 1).replace("_", " ")
                if report.passed:
                    self.passed.append(name)
                elif report.failed:
                    message = ""
                    if hasattr(report.longrepr, "reprcrash") and report.longrepr.reprcrash:
                        message = report.longrepr.reprcrash.message
                    self.failed.append((name, message))

    os.environ["KIDCODE_TARGET"] = target
    collector = Collector()
    root = _repo_root(folder)
    args = [str(folder), "-q", "-p", "no:cacheprovider", "--no-header", "--tb=no",
            "-o", "console_output_style=classic", f"--rootdir={root}"]
    import io
    import contextlib
    with contextlib.redirect_stdout(io.StringIO()):
        code = pytest.main(args, plugins=[collector])

    print("=" * 50)
    print(f"Checking {target}.py in {folder.name}")
    print("=" * 50)
    for name in collector.passed:
        print(f"  [PASS] {name}")
    for name, message in collector.failed:
        print(f"  [TRY AGAIN] {name}")
        if message:
            first = message.splitlines()[0].replace("AssertionError: ", "")
            print(f"      hint: {first}")
    total = len(collector.passed) + len(collector.failed)
    print("-" * 50)
    if total == 0:
        print("I could not find any checks to run. Ask your teacher for help.")
    elif not collector.failed:
        print(f"Amazing! All {total} checks passed. You did it!")
    else:
        print(f"{len(collector.passed)} of {total} checks passed. Read the hints, fix one thing, and run me again.")
        print("Bugs are normal - every programmer meets them every day.")
    return int(code)


if __name__ == "__main__":
    sys.exit(check_folder(sys.argv[1] if len(sys.argv) > 1 else "."))
