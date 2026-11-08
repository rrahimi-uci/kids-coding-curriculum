"""Checks for Homework 8 - Loop Fixer."""

BLUE = "#0072B2"
ORANGE = "#E69F00"


def lines_in(run_target, colour):
    return [line for line in run_target().turtle.lines if str(line.color).upper() == colour]


def is_closed(lines):
    return bool(lines) and abs(lines[0].start[0] - lines[-1].end[0]) < 1 \
        and abs(lines[0].start[1] - lines[-1].end[1]) < 1


def test_square_has_four_sides(run_target):
    n = len(lines_in(run_target, BLUE))
    assert n == 4, f"The blue square has {n} sides. How many times does its loop repeat?"


def test_square_is_closed(run_target):
    assert is_closed(lines_in(run_target, BLUE)), "The blue square is not closed yet."


def test_star_is_closed(run_target):
    star = lines_in(run_target, ORANGE)
    assert len(star) == 5 and is_closed(star), (
        "The orange star should have 5 lines and end where it started. "
        "Is the turn pushed in (indented) so it is inside the loop?"
    )
