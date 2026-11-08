"""Checks for Bug Hunt Station 3 - Rocket Countdown."""

import pytest


def run_countdown(m, start):
    try:
        return m.countdown(start)
    except RuntimeError:
        pytest.fail("The loop got stuck (the safety net stopped it). Something inside the loop must change n.")


def test_countdown_from_three(load_target):
    m = load_target()
    answer = run_countdown(m, 3)
    assert answer == [3, 2, 1], f"countdown(3) should be [3, 2, 1], not {answer}."


def test_countdown_from_zero_is_empty(load_target):
    m = load_target()
    assert run_countdown(m, 0) == [], "countdown(0) has nothing to count: it should be []."


def test_launch_lifts_off(run_target):
    try:
        out = run_target().stdout
    except RuntimeError:
        pytest.fail("The rocket never launched: the loop got stuck.")
    assert "5..." in out and "1..." in out and "LIFT OFF!" in out, "Count 5... down to 1... then LIFT OFF!"
