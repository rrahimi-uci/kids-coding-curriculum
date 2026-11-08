"""TEACHER REFERENCE SOLUTION: Exercise 8.2 - Test the Best Score

What it does: a set of pytest tests for best_score() (in score_tools.py):
one normal case and three edge cases. Press Run to see four PASSED lines.
Key ideas: a test is a small program that checks another program; bugs hide
at the EDGES (empty list, first item, last item, a single item).
Approach: each test calls best_score() with a list we chose and uses assert
to say what the answer must be. Together the tests catch three broken
versions: one that returns the first score, one that crashes on an empty
list, and one that never looks at the last score.
"""

from score_tools import best_score


def test_best_score_in_the_middle():
    # Normal case: the best score is in the middle of the list.
    assert best_score([3, 9, 2]) == 9, "9 is the biggest of 3, 9 and 2"


def test_empty_list():
    # Edge case: no games played yet. This catches the version that crashes
    # on an empty list (it tries to read the first item of nothing).
    assert best_score([]) == 0, "An empty list should give 0"


def test_best_score_at_the_end():
    # Edge case: the biggest score is the very last one. This catches the
    # off-by-one version that stops its loop one place too early. The best
    # score must NOT be first, or a lazy "return the first" would pass.
    assert best_score([5, 1, 8]) == 8, "8 is last but it is still the best"


def test_only_one_score():
    # Edge case: a list with just one score.
    assert best_score([40]) == 40, "With one score, that score is the best"


if __name__ == "__main__":
    import pytest
    pytest.main(["-v", __file__])


# Common mistakes children make here:
# - Writing a test with no assert (or just "pass"). It shows PASSED but
#   checks nothing, so it can never catch a bug.
# - Putting the best score FIRST in every test list, so a broken function
#   that returns the first score still passes.
# - Working out the expected answer wrongly (for example expecting the
#   biggest of [5, 1, 8] to be 5). If a test fails on the correct function,
#   the test is wrong, not score_tools.py.
# - Using the same test name twice: Python keeps only the last one.
#
# Another correct way: one more edge case, all scores the same:
#     def test_all_the_same():
#         assert best_score([7, 7, 7]) == 7, "equal scores: any of them is the best"
