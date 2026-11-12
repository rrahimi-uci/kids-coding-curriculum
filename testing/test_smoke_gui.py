"""Open every turtle program (exercise solutions + project reference code) in
a real window for a moment. Run on a Mac with:  make smoke   (pytest --gui)

Programs that call input() need a smoke_inputs.txt next to them.
"""

import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import curriculum  # noqa: E402  (tools/curriculum.py)

LEVELS = [lv.dir for lv in curriculum.levels()]


def turtle_programs():
    for level in LEVELS:
        for path in sorted((ROOT / level).rglob("*.py")):
            if path.name.startswith("test_") or path.name == "check_my_work.py":
                continue
            if path.name == "starter.py":
                continue
            text = path.read_text(encoding="utf-8")
            if "import turtle" not in text and "from turtle" not in text:
                continue
            if 'if __name__ == "__main__"' not in text and path.name != "solution.py" \
                    and "SMOKE: run" not in text:
                continue  # helper modules are exercised through their main program
            yield path


@pytest.mark.gui
@pytest.mark.parametrize("program", list(turtle_programs()), ids=lambda p: str(p.relative_to(ROOT)))
def test_runs_in_a_real_turtle_window(program):
    result = subprocess.run(
        [sys.executable, str(ROOT / "testing" / "smoke_run.py"), str(program), "--ms", "800"],
        capture_output=True, text=True, timeout=90,
    )
    assert result.returncode == 0, result.stderr[-3000:]
