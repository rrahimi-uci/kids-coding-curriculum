"""Checks for Homework 7 - Triangle Time."""


def test_draws_three_sides(run_target):
    n = len(run_target().turtle.lines)
    assert n == 3, f"A triangle has 3 sides, but your turtle drew {n}."


def test_all_sides_are_the_same_length(run_target):
    lengths = sorted({round(line.length) for line in run_target().turtle.lines})
    assert len(lengths) == 1, f"All three sides should be the same length. Yours were: {lengths}"


def test_triangle_is_closed(run_target):
    t = run_target().turtle
    assert t.is_back_at_start(), (
        "The triangle is not closed. Did you turn 120 degrees at every corner?"
    )
