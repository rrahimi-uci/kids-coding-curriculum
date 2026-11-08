"""Checks for Exercise 10.1 - Flower Stamp."""

import inspect

YELLOW = "#F0E442"


def all_dots(screen):
    return [d for t in screen.turtle_list for d in t.dots]


def petal_colours(screen):
    return {str(f.color).upper() for t in screen.turtle_list for f in t.fills} - {YELLOW}


def test_draws_at_least_three_flowers(run_target):
    screen = run_target().screen
    middles = {d.pos for d in all_dots(screen)}
    assert len(middles) >= 3, (
        f"I found {len(middles)} flower(s). Did you CALL flower(...) three times at different places?"
    )


def test_flowers_use_different_colours(run_target):
    colours = petal_colours(run_target().screen)
    assert colours, "No flowers yet. Call flower(...) at the bottom of your program."
    assert len(colours) >= 2, (
        "All your flowers are the same colour. Give flower a colour parameter and use t.color(colour)."
    )


def test_flower_has_a_colour_parameter(load_target):
    program = load_target()
    assert hasattr(program, "flower"), "I could not find def flower(...) in your program."
    params = list(inspect.signature(program.flower).parameters)
    assert len(params) >= 3, f"flower has the parameters {params}. Add a third one: colour."
    screen = program.__kidtest_fake_turtle__.screen
    program.flower(120, -150, "#CC79A7")
    assert "#CC79A7" in petal_colours(screen), (
        "I called flower(120, -150, \"#CC79A7\") but no purple petals appeared. Use t.color(colour)."
    )
