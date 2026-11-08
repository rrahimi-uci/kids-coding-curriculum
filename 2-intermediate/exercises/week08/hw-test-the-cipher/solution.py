"""MY TESTS for encode() - reference solution.

One normal case and three edge cases. Press Run to see four PASSED lines.
"""

from cipher_tools import encode


def test_normal_word_shift_1():
    # Normal case: every letter moves one place along.
    assert encode("abc", 1) == "bcd", "a->b, b->c, c->d"


def test_wraps_round_after_z():
    # Edge case: after z comes a again.
    assert encode("xyz", 3) == "abc", "x->a, y->b, z->c (wrap round)"


def test_spaces_and_symbols_stay_the_same():
    # Edge case: only letters change.
    assert encode("hi there!", 1) == "ij uifsf!", "the space and ! must not change"


def test_shift_zero_changes_nothing():
    # Edge case: a shift of 0 gives back the same message.
    assert encode("pixel", 0) == "pixel", "shift 0 should change nothing"


if __name__ == "__main__":
    import pytest
    pytest.main(["-v", __file__])
