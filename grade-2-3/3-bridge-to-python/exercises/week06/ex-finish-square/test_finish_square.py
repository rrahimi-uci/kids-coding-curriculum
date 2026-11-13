"""Checks for Exercise 6.2 - Finish the Square."""


def test_draws_four_sides(run_target):
    n = len(run_target().turtle.lines)
    assert n == 4, f"A square has 4 sides, but your turtle drew {n}. Add t.forward(100) for side 4."


def test_sides_are_the_same_length(run_target):
    lengths = {round(line.length) for line in run_target().turtle.lines}
    assert len(lengths) == 1, (
        "All 4 sides of a square are the same length. Use 100 in every t.forward line."
    )


def test_square_is_closed(run_target):
    assert run_target().turtle.is_back_at_start(), (
        "The turtle did not get back to where it started, so the square is open."
    )
