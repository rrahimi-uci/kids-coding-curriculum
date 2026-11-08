"""Checks for Exercise 9.1 - Square of Any Size."""

import pytest


def draw_with(run_target, answer):
    try:
        return run_target(inputs=[answer]).turtle
    except TypeError:
        raise AssertionError(
            "The program crashed. input() gives back text, not a number. "
            "Did you turn it into a number with int(answer)?"
        ) from None


@pytest.mark.parametrize("answer", ["80", "150"])
def test_square_is_the_size_you_typed(run_target, answer):
    t = draw_with(run_target, answer)
    lengths = sorted({round(line.length) for line in t.lines})
    assert lengths == [int(answer)], (
        f"When I typed {answer}, the sides were {lengths} long. They should all be {answer}."
    )


def test_square_has_four_sides_and_is_closed(run_target):
    t = draw_with(run_target, "100")
    assert len(t.lines) == 4 and t.is_back_at_start(), "The turtle should draw a closed square (4 sides)."
