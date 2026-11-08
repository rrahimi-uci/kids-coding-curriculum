"""Checks for Exercise 9.3 - How Many Stars?"""

import pytest


def stars_drawn(result):
    return len(result.turtle.fills)


def messages(result):
    """Printed lines that are not the question (input() prompts are echoed)."""
    asked = [prompt.strip() for prompt in result.prompts if prompt.strip()]
    return [line for line in result.output_lines
            if line.strip() and not any(line.startswith(q) for q in asked)]


def test_draws_the_number_you_asked_for(run_target):
    result = run_target(inputs=["3"])
    assert stars_drawn(result) == 3, f"I typed 3 but got {stars_drawn(result)} stars."


@pytest.mark.parametrize("answer", ["25", "11"])
def test_too_many_stars_becomes_ten(run_target, answer):
    result = run_target(inputs=[answer])
    n = stars_drawn(result)
    assert n == 10, f"I typed {answer}. Only 10 fit, so draw 10 - but I got {n}. Use: if stars > 10:"
    assert messages(result), "Print a message to tell the user you changed their number."


@pytest.mark.parametrize("answer", ["0", "-4"])
def test_too_few_stars_becomes_one(run_target, answer):
    result = run_target(inputs=[answer])
    n = stars_drawn(result)
    assert n == 1, f"I typed {answer}. The program should draw 1 star, but I got {n}. Use: elif stars < 1:"
