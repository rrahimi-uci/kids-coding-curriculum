"""Checks for Homework 7 - Triangle Time.

Only the first 3 lines are checked, so a Challenge square drawn after the
triangle does not upset the checker.
"""

import math


def triangle_lines(run_target):
    return run_target().turtle.lines[:3]


def test_draws_three_sides(run_target):
    n = len(run_target().turtle.lines)
    assert n >= 3, f"A triangle has 3 sides, but your turtle drew {n}."


def test_all_sides_are_the_same_length(run_target):
    lengths = sorted({round(line.length) for line in triangle_lines(run_target)})
    assert len(lengths) == 1, f"All three sides should be the same length. Yours were: {lengths}"


def test_triangle_is_closed(run_target):
    lines = triangle_lines(run_target)
    closed = len(lines) == 3 and math.dist(lines[0].start, lines[-1].end) < 1
    assert closed, "The triangle is not closed. Did you turn 120 degrees at every corner?"
