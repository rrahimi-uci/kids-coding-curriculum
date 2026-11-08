"""Run or import a student's program with the fake turtle, fake input() and a
captured screen, so tests can check what it did."""

from __future__ import annotations

import builtins
import contextlib
import importlib.util
import io
import os
import random
import runpy
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path

from .fake_turtle import make_fake_turtle_module


class NotEnoughInput(AssertionError):
    pass


@dataclass
class RunResult:
    stdout: str
    namespace: dict
    turtle_module: object
    prompts: list = field(default_factory=list)

    @property
    def screen(self):
        return self.turtle_module.screen

    @property
    def turtles(self):
        return self.turtle_module.screen.turtle_list

    @property
    def turtle(self):
        """The first turtle created (the one most programs use)."""
        if not self.turtles:
            raise AssertionError("The program did not create a turtle.")
        return self.turtles[0]

    @property
    def lines(self):
        return self.screen.all_lines

    @property
    def output_lines(self):
        return [line for line in self.stdout.splitlines()]


@contextlib.contextmanager
def sandbox(path: Path, inputs=(), seed=None, cwd=None):
    """Patch turtle, input(), time.sleep and the working directory."""
    path = Path(path)
    fake = make_fake_turtle_module(inputs=list(inputs))
    queue = fake.screen.inputs  # input() and textinput() share one queue
    prompts = fake.screen.prompts
    out = io.StringIO()

    def fake_input(prompt=""):
        print(prompt, end="", file=out)
        prompts.append(prompt)
        if not queue:
            raise NotEnoughInput(
                f"The program asked for more input than the test gave it (prompt: {prompt!r})."
            )
        value = str(queue.pop(0))
        print(value, file=out)  # echo like a terminal so output reads naturally
        return value

    saved_turtle = sys.modules.get("turtle")
    saved_input = builtins.input
    saved_sleep = time.sleep
    saved_cwd = os.getcwd()
    saved_path = list(sys.path)
    saved_modules = set(sys.modules)
    sys.modules["turtle"] = fake
    builtins.input = fake_input
    time.sleep = lambda s: None
    sys.path.insert(0, str(path.parent))
    os.chdir(cwd or path.parent)
    if seed is not None:
        random.seed(seed)
    try:
        with contextlib.redirect_stdout(out):
            yield fake, out, prompts
    finally:
        os.chdir(saved_cwd)
        sys.path[:] = saved_path
        # Forget helper modules imported from the program's folder, so two
        # exercises that both have e.g. ``model.py`` never see each other's.
        folder = str(path.parent.resolve())
        for mod_name in set(sys.modules) - saved_modules:
            mod_file = getattr(sys.modules.get(mod_name), "__file__", None) or ""
            if mod_file and str(Path(mod_file).resolve().parent) == folder:
                sys.modules.pop(mod_name, None)
        time.sleep = saved_sleep
        builtins.input = saved_input
        if saved_turtle is not None:
            sys.modules["turtle"] = saved_turtle
        else:
            sys.modules.pop("turtle", None)


def run_script(path, inputs=(), seed=None, cwd=None) -> RunResult:
    """Run a whole program as if the student pressed Run in Thonny."""
    path = Path(path)
    with sandbox(path, inputs=inputs, seed=seed, cwd=cwd) as (fake, out, prompts):
        try:
            ns = runpy.run_path(str(path), run_name="__main__")
        except SystemExit:
            ns = {}
    return RunResult(stdout=out.getvalue(), namespace=ns, turtle_module=fake, prompts=prompts)


def load_module(path, inputs=(), seed=None, name=None):
    """Import a program as a module (code under ``if __name__ == "__main__":``
    does NOT run) so tests can call its functions and classes directly.

    The fake turtle stays installed as ``module.turtle`` so drawing functions
    called later still draw on the fake screen (``module.turtle.screen``)."""
    path = Path(path)
    name = name or f"kidtest_{path.stem}_{abs(hash(str(path)))}"
    with sandbox(path, inputs=inputs, seed=seed) as (fake, out, prompts):
        spec = importlib.util.spec_from_file_location(name, path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
    module.__dict__.setdefault("turtle", fake)
    module.__kidtest_fake_turtle__ = fake
    module.__kidtest_stdout__ = out.getvalue()
    return module


@contextlib.contextmanager
def feed_inputs(inputs):
    """Make input() return these answers, in order, inside a ``with`` block.

    Use it when a test calls a function that asks questions::

        with feed_inputs(["7", "yes"]) as prompts:
            game.play_round()
    """
    queue = [str(v) for v in inputs]
    prompts: list = []
    saved = builtins.input

    def fake_input(prompt=""):
        prompts.append(prompt)
        if not queue:
            raise NotEnoughInput(f"The program asked for more input than the test gave it (prompt: {prompt!r}).")
        return queue.pop(0)

    builtins.input = fake_input
    try:
        yield prompts
    finally:
        builtins.input = saved
