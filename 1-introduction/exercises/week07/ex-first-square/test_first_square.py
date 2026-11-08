"""Checks for Exercise 7.2 - My First Square."""


def test_draws_four_sides(run_target):
    t = run_target().turtle
    sides = len(t.lines)
    assert sides == 4, f"A square has 4 sides, but your turtle drew {sides}."


def test_all_sides_are_the_same_length(run_target):
    t = run_target().turtle
    lengths = {round(line.length) for line in t.lines}
    assert len(lengths) == 1, f"All sides of a square are the same length. Yours were: {sorted(lengths)}"


def test_ends_where_it_started(run_target):
    t = run_target().turtle
    assert t.is_back_at_start(), "The square is not closed: the turtle should finish where it started."
