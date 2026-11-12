"""Checks for Exercise 7.2 - The Lonely Turn."""


def test_turtle_turns_at_every_corner(run_target):
    t = run_target().turtle
    turns = t.count("left") + t.count("right")
    assert turns >= 4, (
        f"The turtle turned only {turns} time(s). Push t.left(90) in by 4 spaces "
        "so it is inside the repeat."
    )


def test_draws_four_equal_sides(run_target):
    lines = run_target().turtle.lines
    lengths = {round(line.length) for line in lines}
    assert len(lines) == 4 and len(lengths) == 1, (
        f"A square has 4 equal sides. Your turtle drew {len(lines)} line(s)."
    )


def test_square_is_closed(run_target):
    assert run_target().turtle.is_back_at_start(), (
        "The turtle walked away in a straight line and did not come back. "
        "Is t.left(90) inside the repeat?"
    )
