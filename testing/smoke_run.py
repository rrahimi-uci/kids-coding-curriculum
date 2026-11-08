"""Open a turtle program in a REAL window for a moment, then close it.

Used by ``make smoke`` (``pytest --gui``) on a Mac to prove that solution
files really run with the real turtle module + Tk, not just with the fake
turtle used in unit tests.

    python testing/smoke_run.py path/to/solution.py [--ms 1500]

Answers for input()/textinput()/numinput() are read from a file called
``smoke_inputs.txt`` next to the program (one answer per line), if present.
Exit code 0 = ran without errors, 1 = an exception happened.
"""

from __future__ import annotations

import argparse
import builtins
import os
import runpy
import signal
import sys
import time
import traceback
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("script")
    parser.add_argument("--ms", type=int, default=1500, help="how long to keep the window open")
    parser.add_argument("--timeout", type=int, default=20, help="hard stop in seconds")
    args = parser.parse_args()

    script = Path(args.script).resolve()
    answers_file = script.parent / "smoke_inputs.txt"
    answers = answers_file.read_text().splitlines() if answers_file.exists() else []

    import tkinter
    import turtle

    errors: list = []

    def report_callback_exception(self, exc, val, tb):
        if exc is turtle.Terminator:
            return
        errors.append("".join(traceback.format_exception(exc, val, tb)))
        try:
            turtle.bye()
        except Exception:
            pass

    tkinter.Tk.report_callback_exception = report_callback_exception

    def next_answer(prompt=""):
        if not answers:
            raise EOFError(f"smoke_inputs.txt has no answer left for prompt {prompt!r}")
        value = answers.pop(0)
        print(f"{prompt}{value}")
        return value

    builtins.input = next_answer
    turtle.textinput = lambda title, prompt: next_answer(prompt)
    turtle.TurtleScreen.textinput = lambda self, title, prompt: next_answer(prompt)

    def numinput(*a, **k):
        prompt = a[1] if len(a) > 1 else ""
        return float(next_answer(prompt))

    turtle.numinput = numinput
    turtle.TurtleScreen.numinput = lambda self, *a, **k: numinput(*a, **k)

    # Draw instantly: ignore animation speed and screen.tracer() requests.
    screen = turtle.Screen()
    screen.tracer(0)
    turtle.TurtleScreen.tracer = lambda self, n=None, delay=None: 0
    turtle.tracer = lambda n=None, delay=None: 0
    time.sleep = lambda s: None  # games that sleep between frames run fast

    def close_soon():
        try:
            screen.update()
        except Exception:
            pass
        screen.ontimer(turtle.bye, args.ms)

    real_mainloop = tkinter.mainloop

    def patched_mainloop(*a, **k):
        close_soon()
        try:
            real_mainloop()
        except turtle.Terminator:
            pass

    turtle.mainloop = turtle.done = patched_mainloop
    turtle.TurtleScreen.mainloop = lambda self: patched_mainloop()
    turtle._Screen.exitonclick = lambda self: patched_mainloop()
    turtle.exitonclick = patched_mainloop

    def on_alarm(signum, frame):  # program never reached mainloop (e.g. while True)
        raise TimeoutError

    signal.signal(signal.SIGALRM, on_alarm)
    signal.alarm(args.timeout)

    os.chdir(script.parent)
    sys.path.insert(0, str(script.parent))
    try:
        runpy.run_path(str(script), run_name="__main__")
        screen.update()
    except (turtle.Terminator, TimeoutError, SystemExit):
        pass
    except tkinter.TclError as exc:
        if "application has been destroyed" not in str(exc):
            errors.append(traceback.format_exc())
    except Exception:
        errors.append(traceback.format_exc())
    finally:
        signal.alarm(0)
        try:
            turtle.bye()
        except Exception:
            pass

    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"OK {script}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
