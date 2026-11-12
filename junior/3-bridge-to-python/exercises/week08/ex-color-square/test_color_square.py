"""Checks for Exercise 8.1 - Color My Square."""

BLACK = {"black", "#000000", "#000"}


def test_square_has_a_new_color(run_target):
    colors = {str(c).lower() for c in run_target().turtle.colors_used}
    assert colors and not colors <= BLACK, (
        'Your square is still black. Change "black" to a color you like, '
        'such as "blue". Keep the quote marks!'
    )


def test_pen_is_thicker(run_target):
    widths = [line.width for line in run_target().turtle.lines]
    assert widths and min(widths) >= 3, (
        "The lines are still thin. Change t.pensize(1) to a bigger number, like 5."
    )


def test_still_a_square(run_target):
    t = run_target().turtle
    assert len(t.lines) == 4 and t.is_back_at_start(), (
        "The program should still draw a closed square with 4 sides. Change only the color "
        "and the pen size."
    )
