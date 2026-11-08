"""Checks for Bug Hunt Station 2 - High Scores."""

import pytest


def test_highest(load_target):
    m = load_target()
    try:
        answer = m.highest([40, 90, 15, 60])
    except IndexError:
        pytest.fail("highest() crashed with IndexError. 4 scores have the index numbers 0 to 3.")
    assert answer == 90, f"The highest of [40, 90, 15, 60] is 90, not {answer}."


def test_podium_with_four_scores(load_target):
    m = load_target()
    assert m.podium([40, 90, 15, 60]) == ["1st: 90", "2nd: 60", "3rd: 40"], "The podium should be 90, 60, 40."


def test_podium_with_two_scores(load_target):
    m = load_target()
    try:
        answer = m.podium([70, 20])
    except IndexError:
        pytest.fail("podium([70, 20]) crashed with IndexError. With only 2 scores, the loop must go round only 2 times.")
    assert answer == ["1st: 70", "2nd: 20"], f"With two scores the podium is ['1st: 70', '2nd: 20'], not {answer}."
