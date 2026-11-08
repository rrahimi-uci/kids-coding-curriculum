"""MY TESTS for best_score()  -  this file is YOUR test file.

Read score_tools.py first to see what best_score() should do.
Then write tests for the NORMAL case and for the EDGE cases: the places
where bugs like to hide (empty lists, the first item, the last item...).

Press the green Run button to run your tests with pytest.
"""

from score_tools import best_score


def test_best_score_in_the_middle():
    # Normal case: the best score is in the middle of the list.
    assert best_score([3, 9, 2]) == 9, "9 is the biggest of 3, 9 and 2"


def test_empty_list():
    # TODO 1 (edge case): no games played yet. What should best_score([]) give?
    pass


def test_best_score_at_the_end():
    # TODO 2 (edge case): make a list where the biggest score is the LAST one.
    pass


# TODO 3: one more test of your own. Ideas: a list with only one score,
#         or a list where every score is the same.


if __name__ == "__main__":
    import pytest
    pytest.main(["-v", __file__])
