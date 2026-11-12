"""Checks for the Junior Level 3 project (My Big Build, Python path):
the reference postcard and the starter children begin from."""

import re
from pathlib import Path

from kidtest import load_module, run_script

HERE = Path(__file__).parent
REFERENCE = HERE / "postcard_reference.py"
STARTER = HERE.parent / "starter" / "postcard.py"


def lines_in(turtle, color, length):
    return [line for line in turtle.lines if line.color == color and round(line.length) == length]


def test_starter_already_runs_and_draws_a_house_with_a_roof():
    t = run_script(STARTER).turtle
    assert len(lines_in(t, "orange", 100)) == 4, "The starter should draw an orange square house."
    assert len(lines_in(t, "purple", 100)) == 3, "The starter should draw a purple triangle roof."


def test_postcard_has_the_python_must_haves():
    t = run_script(REFERENCE).turtle
    colors = len(t.colors_used)
    assert colors >= 2, f"A postcard needs at least 2 colors, but it used {colors}."
    assert len(lines_in(t, "orange", 120)) == 4, "The house should be an orange square (4 sides)."
    assert len(lines_in(t, "purple", 120)) == 3, "The roof should be a purple triangle (3 sides)."
    assert len(lines_in(t, "gold", 40)) == 6, "The sun should be a gold hexagon with 6 sides."


def test_flower_block_draws_a_stem_and_six_petals_and_comes_back():
    module = load_module(REFERENCE)
    t = module.t
    start, heading, before = t.position(), t.heading(), len(t.lines)
    module.flower()
    new = t.lines[before:]
    stems = [line for line in new if line.color == "green"]
    petals = [line for line in new if line.color == "purple"]
    assert len(stems) == 1 and len(petals) == 6, (
        f"flower() should draw 1 stem and 6 petal sides, not {len(stems)} and {len(petals)}."
    )
    assert t.position() == start and t.heading() == heading, (
        "After flower() the turtle should be back where it started, facing the same way."
    )
    petals_on_card = len(lines_in(run_script(REFERENCE).turtle, "purple", 20))
    assert petals_on_card == 18, "The postcard should have 3 flowers (3 x 6 petal sides)."


def test_reference_follows_the_junior_rules():
    code = REFERENCE.read_text(encoding="utf-8")
    t = run_script(REFERENCE).turtle
    assert t.count("goto") == 0 and t.count("setheading") == 0, (
        "Move with forward, left and right only."
    )
    assert not re.search(r"[(\s,]-\s*\d", code), "Junior code never uses negative numbers."
    assert "input(" not in code, "Junior code never asks for typed input."
