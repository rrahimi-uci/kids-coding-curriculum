"""Checks for Exercise 7.3 - Python Flower."""


def test_draws_at_least_four_squares(run_target):
    n = len(run_target().turtle.lines)
    assert n >= 16, (
        f"Your flower has {n // 4} square(s). Change the 2 in range(2) to 6 for 6 squares."
    )


def test_squares_have_equal_sides(run_target):
    lengths = {round(line.length) for line in run_target().turtle.lines}
    assert len(lengths) == 1, "Every side of every square should be the same length."


def test_flower_goes_all_the_way_round(run_target):
    t = run_target().turtle
    assert t.is_back_at_start() and round(t.total_turn) % 360 == 0, (
        "The turtle should end where it started, looking the same way. "
        "With a turn of 60 you need 6 squares."
    )
