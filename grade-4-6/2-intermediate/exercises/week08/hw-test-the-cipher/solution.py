"""TEACHER REFERENCE SOLUTION: Homework 8 - Test the Cipher

What it does: pytest tests for encode() (the Caesar cipher in
cipher_tools.py): one normal case and three edge cases. Press Run to see
four PASSED lines.
Key ideas: edge cases for a cipher are wrapping around after z, leaving
spaces and symbols alone, and the "do nothing" shift of 0.
Approach: each test calls encode() with a message we chose and asserts the
answer worked out by hand on the paper cipher wheel. Together they catch
three broken versions: no wrap-around, spaces thrown away, and shifting
the wrong way.
"""

from cipher_tools import encode


def test_normal_word_shift_1():
    # Normal case: every letter moves one place along.
    # (A shift of 1 also tells forwards from backwards: backwards gives "zab".)
    assert encode("abc", 1) == "bcd", "a->b, b->c, c->d"


def test_wraps_around_after_z():
    # Edge case: after z comes a again. Without wrap-around, "z" + 3 would
    # become a symbol such as "}" instead of "c".
    assert encode("xyz", 3) == "abc", "x->a, y->b, z->c (wrap around)"


def test_spaces_and_symbols_stay_the_same():
    # Edge case: only letters change. A version that forgets the else branch
    # would lose the space and the "!" and give "ijuifsf".
    assert encode("hi there!", 1) == "ij uifsf!", "the space and ! must not change"


def test_shift_zero_changes_nothing():
    # Edge case: a shift of 0 gives back the same message.
    assert encode("pixel", 0) == "pixel", "shift 0 should change nothing"


if __name__ == "__main__":
    import pytest
    pytest.main(["-v", __file__])


# Common mistakes children make here:
# - Working out the expected answer wrongly, e.g. encode("xyz", 3) == "{|}"
#   (forgetting to wrap around). If a test fails on the correct encode(),
#   the test is wrong: check it with the paper wheel.
# - Only testing a shift of 0 or 13, where going forwards and backwards
#   give the same answer, so a backwards cipher slips through.
# - Writing a test with no assert (or leaving "pass"): it shows PASSED but
#   checks nothing.
# - Testing a message with no space or symbol, so the "loses spaces" bug is
#   never caught.
#
# Another correct way: one more edge case, the empty message:
#     def test_empty_message():
#         assert encode("", 5) == "", "nothing in, nothing out"
