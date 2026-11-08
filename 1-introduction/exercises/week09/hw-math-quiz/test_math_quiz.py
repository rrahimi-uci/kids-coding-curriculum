"""Checks for Homework 9 - Mini Math Quiz.

Extra answers ("999") are given in case you added a Challenge question.
"""

import re

PADDING = ["999", "999", "999"]


def last_line(result):
    lines = [line for line in result.output_lines if line.strip()]
    return lines[-1] if lines else ""


def test_asks_two_questions(run_target):
    result = run_target(inputs=["56", "24"] + PADDING)
    assert len(result.prompts) >= 2, f"The quiz asked {len(result.prompts)} question(s). Add question 2."


def test_right_answers_say_correct(run_target):
    result = run_target(inputs=["56", "24"] + PADDING)
    n = result.stdout.count("Correct")
    assert n >= 2, f"Two right answers should print 'Correct!' twice, but I saw it {n} time(s)."


def score_shown(result):
    """The number after the word 'scored' on the last line, or None."""
    match = re.search(r"scored\D*(\d+)", last_line(result), re.IGNORECASE)
    return int(match.group(1)) if match else None


def test_score_is_shown_at_the_end(run_target):
    result = run_target(inputs=["56", "24"] + PADDING)
    assert score_shown(result) == 2, (
        f"With 2 right answers the last line should say: You scored 2 out of 2. It said: {last_line(result)!r}"
    )


def test_wrong_answers_do_not_score(run_target):
    result = run_target(inputs=["50", "20"] + PADDING)
    assert "Correct" not in result.stdout, "Wrong answers should not say 'Correct!'."
    assert score_shown(result) == 0, (
        f"With 0 right answers the last line should say: You scored 0 out of 2. It said: {last_line(result)!r}"
    )
