"""MY TESTS for encode()  -  this file is YOUR test file.

Read cipher_tools.py first to see what encode() should do.
You can check your expected answers with the paper cipher wheel from week 5!
Press the green Run button to run your tests with pytest.
"""

from cipher_tools import encode


def test_normal_word_shift_1():
    # Normal case: every letter moves one place along.
    assert encode("abc", 1) == "bcd", "a->b, b->c, c->d"


def test_wraps_around_after_z():
    # TODO 1 (edge case): letters near the end of the alphabet must wrap
    #         around to the start. Use the wheel to work out encode("xyz", 3).
    pass


def test_spaces_and_symbols_stay_the_same():
    # TODO 2 (edge case): a message with a space and a ! in it.
    pass


# TODO 3: one more test of your own. Ideas: shift 0 (nothing changes),
#         or an empty message "".


if __name__ == "__main__":
    import pytest
    pytest.main(["-v", __file__])
