"""Checks for Exercise 8.3 - My Square Block (stretch)."""


def test_the_square_block_is_still_there(run_target):
    block = run_target().namespace.get("square")
    assert callable(block), "Keep the def square(): block at the top of the program."


def test_draws_four_squares(run_target):
    n = len(run_target().turtle.lines)
    assert n >= 16, (
        f"Your window has {n // 4} square(s). Change the 1 in range(1) to 4 for 4 squares."
    )


def test_window_is_closed(run_target):
    t = run_target().turtle
    assert t.is_back_at_start() and round(t.total_turn) % 360 == 0, (
        "The turtle should end in the middle, looking the same way as at the start."
    )
