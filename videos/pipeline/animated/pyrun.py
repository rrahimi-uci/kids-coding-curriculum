"""Run the Python code shown in a video, so the screen shows what the code really does.

Each snippet runs in a separate Python process (isolated, with a timeout) using the course's own
headless turtle (testing/kidtest). We record printed output exactly as Thonny's Shell shows it
(an input() prompt followed by the typed answer), the last line of any error, and every line,
dot, fill and text the turtle draws, in the order they were drawn. Results are cached by content.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile

REPO_ROOT = Path(__file__).resolve().parents[3]
CACHE = REPO_ROOT / "videos" / ".cache" / "pyrun"

_RUNNER = r'''
import io, json, random, sys, traceback, contextlib
sys.path.insert(0, __REPO__)
from testing.kidtest import fake_turtle as ft

order = []
_move = ft.FakeTurtle._move_to
def _move_to(self, x, y):
    before = len(self.lines)
    _move(self, x, y)
    if len(self.lines) > before:
        line = self.lines[-1]
        order.append(["line", line.start[0], line.start[1], line.end[0], line.end[1], str(line.color), line.width])
ft.FakeTurtle._move_to = _move_to
_dot = ft.FakeTurtle.dot
def dot(self, *args):
    _dot(self, *args)
    d = self.dots[-1]
    order.append(["dot", d.pos[0], d.pos[1], d.size, str(d.color)])
ft.FakeTurtle.dot = dot
_end_fill = ft.FakeTurtle.end_fill
def end_fill(self):
    _end_fill(self)
    if self.fills:
        f = self.fills[-1]
        order.append(["fill", str(f.color), [list(p) for p in f.points]])
ft.FakeTurtle.end_fill = end_fill
_write = ft.FakeTurtle.write
def write(self, arg, *args, **kwargs):
    _write(self, arg, *args, **kwargs)
    t = self.texts[-1]
    order.append(["text", t.text, t.pos[0], t.pos[1], t.align])
ft.FakeTurtle.write = write

module = ft.make_fake_turtle_module()
sys.modules["turtle"] = module
answers = list(__INPUTS__)
out = io.StringIO()
def fake_input(prompt=""):
    answer = answers.pop(0) if answers else ""
    out.write(str(prompt) + answer + "\n")
    return answer
import builtins
builtins.input = fake_input
random.seed(__SEED__)
error = ""
tb_lines = []
CODE_TEXT = __CODE__
namespace = {"__name__": "__main__"}
with contextlib.redirect_stdout(out):
    try:
        exec(compile(CODE_TEXT, "main.py", "exec"), namespace)
    except SystemExit:
        pass
    except BaseException as exc:  # the video shows the error a learner would see
        # Python's own error printer adds hints such as "Did you mean: 'print'?" (Thonny shows them too)
        printed = io.StringIO()
        saved, sys.stderr = sys.stderr, printed
        try:
            sys.__excepthook__(type(exc), exc, exc.__traceback__)
        finally:
            sys.stderr = saved
        lines = [ln for ln in printed.getvalue().splitlines() if ln.strip()]
        error = lines[-1] if lines else "".join(traceback.format_exception_only(type(exc), exc)).strip()
        # the traceback as Thonny shows it, keeping only the learner's own file (main.py)
        frames = [f for f in traceback.extract_tb(exc.__traceback__) if f.filename == "main.py"]
        source = CODE_TEXT.splitlines()
        tb_lines = ["Traceback (most recent call last):"]
        for f in frames:
            tb_lines.append(f'  File "main.py", line {f.lineno}, in {f.name}')
            if 0 < f.lineno <= len(source):
                tb_lines.append("    " + source[f.lineno - 1].strip())
        tb_lines.append(error)
screen = module.screen
result = {"stdout": out.getvalue(), "error": error, "traceback": tb_lines, "draw": order, "bg": str(screen.bg),
          "turtles": [[t._x, t._y, t._heading] for t in screen.turtle_list]}
print("@@RESULT@@" + json.dumps(result))
'''


def interpreter() -> str:
    """The Python that runs video code: the course's Python 3.10 (like Thonny's) when available.

    Error messages differ a little between Python versions, so the videos, the tests and CI all use
    the same interpreter: VIDEO_PYTHON, else the repository's .venv (Python 3.10), else this one.
    """
    import os

    chosen = os.environ.get("VIDEO_PYTHON")
    if chosen:
        return chosen
    venv = REPO_ROOT / ".venv" / "bin" / "python"
    return str(venv) if venv.is_file() else sys.executable


def run(code: str, inputs: tuple[str, ...] = (), seed: int = 1, timeout: float = 20.0) -> dict:
    """Run `code` and return {"stdout", "error", "draw", "bg", "turtles"} (cached)."""
    python = interpreter()
    version = subprocess.run([python, "-c", "import sys; print(sys.version_info[:2])"], capture_output=True,
                             text=True).stdout.strip()
    key = hashlib.sha256(json.dumps([code, list(inputs), seed, 5, version]).encode()).hexdigest()[:32]
    cached = CACHE / f"{key}.json"
    if cached.is_file():
        return json.loads(cached.read_text(encoding="utf-8"))
    program = (_RUNNER.replace("__REPO__", repr(str(REPO_ROOT)), 1).replace("__SEED__", repr(seed), 1)
               .replace("__INPUTS__", repr(list(inputs)), 1).replace("__CODE__", repr(code), 1))
    with tempfile.TemporaryDirectory() as tmp:
        script = Path(tmp) / "runner.py"
        script.write_text(program, encoding="utf-8")
        completed = subprocess.run([python, "-I", str(script)], capture_output=True, text=True,
                                   timeout=timeout, cwd=tmp)
    marker = completed.stdout.rfind("@@RESULT@@")
    if marker < 0:
        raise RuntimeError(f"could not run the video's code snippet: {completed.stderr.strip()[-400:]}")
    result = json.loads(completed.stdout[marker + len("@@RESULT@@"):])
    CACHE.mkdir(parents=True, exist_ok=True)
    cached.write_text(json.dumps(result), encoding="utf-8")
    return result


def shell_lines(result: dict, full_traceback: bool = False) -> list[str]:
    """What Thonny's Shell shows after running: output lines, then the error (its last line, or the
    whole traceback with the file name, line number and source line when `full_traceback`)."""
    lines = result["stdout"].splitlines()
    if result["error"]:
        lines += result.get("traceback") or [result["error"]] if full_traceback else [result["error"]]
    return lines
