"""kidtest: small helpers that let pytest check kids' Python programs.

* ``run_script(path, inputs=[...])``  run a whole program (fake turtle + input)
* ``load_module(path)``               import a program to test its functions
* ``feed_inputs([...])``              answer input() calls inside a ``with`` block
* ``make_fake_turtle_module()``       the headless turtle used by both

See docs/AUTHORING.md ("Exercise code and tests") for conventions.
"""

from .fake_turtle import FakeScreen, FakeTurtle, make_fake_turtle_module
from .runner import NotEnoughInput, RunResult, feed_inputs, load_module, run_script

__all__ = [
    "FakeScreen", "FakeTurtle", "make_fake_turtle_module",
    "NotEnoughInput", "RunResult", "feed_inputs", "load_module", "run_script",
]
