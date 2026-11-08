"""MY TESTS for best_score() - reference solution.

One normal case and three edge cases. Press Run to see four PASSED lines.
"""

from score_tools import best_score


def test_best_score_in_the_middle():
    # Normal case: the best score is in the middle of the list.
    assert best_score([3, 9, 2]) == 9, "9 is the biggest of 3, 9 and 2"


def test_empty_list():
    # Edge case: no games played yet.
    assert best_score([]) == 0, "An empty list should give 0"


def test_best_score_at_the_end():
    # Edge case: the biggest score is the very last one.
    assert best_score([5, 1, 8]) == 8, "8 is last but it is still the best"


def test_only_one_score():
    # Edge case: a list with just one score.
    assert best_score([40]) == 40, "With one score, that score is the best"


if __name__ == "__main__":
    import pytest
    pytest.main(["-v", __file__])
