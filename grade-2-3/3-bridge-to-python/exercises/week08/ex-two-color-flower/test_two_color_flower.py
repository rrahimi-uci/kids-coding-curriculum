"""Checks for Exercise 8.2 - Two-Color Flower."""


def test_uses_two_colors(run_target):
    colors = {str(c).lower() for c in run_target().turtle.colors_used}
    assert len(colors) >= 2, (
        f"Your flower uses {len(colors)} color(s). Change the second "
        '"purple" to another color, like "gold".'
    )


def test_still_a_flower(run_target):
    t = run_target().turtle
    assert len(t.lines) >= 16 and t.is_back_at_start(), (
        f"The flower should have at least 4 squares and end in the middle. "
        f"Your turtle drew {len(t.lines)} lines."
    )
