"""MY TESTS for clamp() - reference solution.

Four tests: one normal case, one too small, one too big, and the edge
case exactly on the limits. Press Run to see four PASSED lines.
"""

from clamp_tools import clamp


def test_middle_value_stays_the_same():
    # Normal case: 5 is already between 0 and 10.
    assert clamp(5, 0, 10) == 5, "5 is between 0 and 10, so it should stay 5"


def test_too_small_goes_up_to_low():
    assert clamp(-3, 0, 10) == 0, "-3 is too small, so it should become 0"


def test_too_big_comes_down_to_high():
    assert clamp(99, 0, 10) == 10, "99 is too big, so it should become 10"


def test_values_on_the_limits_stay_the_same():
    # Edge cases: exactly on the low limit and exactly on the high limit.
    assert clamp(0, 0, 10) == 0, "0 is allowed, so it should stay 0"
    assert clamp(10, 0, 10) == 10, "10 is allowed, so it should stay 10"


if __name__ == "__main__":
    import pytest
    pytest.main(["-v", __file__])
