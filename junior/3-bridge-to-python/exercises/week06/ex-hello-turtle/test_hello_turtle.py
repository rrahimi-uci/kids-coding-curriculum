"""Checks for Exercise 6.1 - Hello, Turtle!"""


def test_turtle_draws_a_long_line(run_target):
    t = run_target().turtle
    assert len(t.lines) == 1, f"The turtle should draw 1 line, but it drew {len(t.lines)}."
    length = round(t.lines[0].length)
    assert length >= 100, (
        f"The line is short ({length} steps). Change 50 to a bigger number, like 150, "
        "then press Run again."
    )


def test_line_stays_in_the_window(run_target):
    t = run_target().turtle
    longest = max((round(line.length) for line in t.lines), default=0)
    assert longest <= 300, (
        f"A line of {longest} steps walks out of the window. Try a number from 100 to 300."
    )


def test_turtle_makes_a_quarter_turn(run_target):
    t = run_target().turtle
    assert abs(round(t.total_turn)) == 90, (
        "At the end the turtle should make one quarter turn: t.left(90)."
    )
