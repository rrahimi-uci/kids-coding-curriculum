"""Checks for Exercise 9.2 - Pick a Colour."""

import pytest


def run_with(run_target, answer):
    try:
        return run_target(inputs=[answer])
    except NameError:
        raise AssertionError(
            f"The program crashed when I typed {answer!r}: it never chose a colour. "
            "Add an elif for it, or an else: for everything else."
        ) from None


def messages(result):
    """Printed lines that are not the question (input() prompts are echoed)."""
    asked = [prompt.strip() for prompt in result.prompts if prompt.strip()]
    return [line for line in result.output_lines
            if line.strip() and not any(line.startswith(q) for q in asked)]


def colours_in(result):
    return {str(c).upper() for c in result.turtle.colors_used}


@pytest.mark.parametrize("answer, hex_code", [
    ("orange", "#E69F00"), ("blue", "#0072B2"), ("green", "#009E73"),
])
def test_known_colours_paint_the_right_colour(run_target, answer, hex_code):
    result = run_with(run_target, answer)
    assert hex_code in colours_in(result), (
        f"When I typed {answer!r}, the circle should be {hex_code}."
    )


def test_unknown_colour_gets_a_friendly_message(run_target):
    result = run_with(run_target, "pizza")
    assert messages(result), "When I typed 'pizza', the program should print a friendly message."
    assert "#000000" in colours_in(result), "For an unknown colour, use black: \"#000000\"."
