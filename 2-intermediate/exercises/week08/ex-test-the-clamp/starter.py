"""MY TESTS for clamp()  -  this file is YOUR test file.

Press the green Run button: pytest runs every function whose name starts
with test_ and says PASSED or FAILED for each one.

A test calls the function with values YOU choose and checks the answer:
    assert clamp(5, 0, 10) == 5, "message to show if it is wrong"

Read clamp_tools.py first to see what clamp() should do.
"""

from clamp_tools import clamp


def test_middle_value_stays_the_same():
    # Normal case: 5 is already between 0 and 10.
    assert clamp(5, 0, 10) == 5, "5 is between 0 and 10, so it should stay 5"


def test_too_small_goes_up_to_low():
    # TODO 1: clamp(-3, 0, 10) should give 0.
    #         Write an assert line like the one in the first test.
    pass


def test_too_big_comes_down_to_high():
    # TODO 2: choose a value that is too big. What should clamp() give back?
    pass


# TODO 3 (edge case): write a 4th test for a value exactly ON a limit,
#                     like clamp(10, 0, 10). Its name must start with test_


if __name__ == "__main__":
    import pytest
    pytest.main(["-v", __file__])
