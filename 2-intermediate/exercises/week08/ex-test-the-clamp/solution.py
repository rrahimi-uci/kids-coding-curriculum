"""TEACHER REFERENCE SOLUTION: Exercise 8.1 - Test the Clamp

What it does: pytest tests for clamp(value, low, high), which keeps a number
between two limits (clamp(99, 0, 10) gives 10). Press Run to see four PASSED
lines.
Key ideas: writing assert lines, reading PASSED and FAILED, and testing
both sides of a range plus the edge (exactly on a limit).
Approach: one test for a normal value, one for too small, one for too big
and one for values exactly on the limits. Together they catch three broken
versions: one that forgets the low limit, one that forgets the high limit
and one that mixes up low and high.
"""

from clamp_tools import clamp


def test_middle_value_stays_the_same():
    # Normal case: 5 is already between 0 and 10.
    assert clamp(5, 0, 10) == 5, "5 is between 0 and 10, so it should stay 5"


def test_too_small_goes_up_to_low():
    # Catches the broken clamp that forgets the LOW limit (it would give -3).
    assert clamp(-3, 0, 10) == 0, "-3 is too small, so it should become 0"


def test_too_big_comes_down_to_high():
    # Catches the broken clamp that forgets the HIGH limit (it would give 99).
    assert clamp(99, 0, 10) == 10, "99 is too big, so it should become 10"


def test_values_on_the_limits_stay_the_same():
    # Edge cases: exactly on the low limit and exactly on the high limit.
    # These are the places where "<" versus "<=" mistakes hide.
    assert clamp(0, 0, 10) == 0, "0 is allowed, so it should stay 0"
    assert clamp(10, 0, 10) == 10, "10 is allowed, so it should stay 10"


if __name__ == "__main__":
    import pytest
    pytest.main(["-v", __file__])


# Common mistakes children make here:
# - Writing a test with no assert (or leaving "pass"). It shows PASSED but
#   checks nothing, so broken versions slip through.
# - Testing only one side (only too small, or only too big). Both limits
#   need a test, otherwise a clamp that forgets one limit passes.
# - Choosing a wrong expected answer, such as clamp(-3, 0, 10) == -3. If a
#   test fails on the correct clamp(), the test is wrong, not clamp_tools.py.
# - Giving two tests the same name: Python keeps only the last one.
#
# Another correct way: one test with several asserts, or a loop over cases:
#     for value, expected in [(-3, 0), (5, 5), (99, 10)]:
#         assert clamp(value, 0, 10) == expected
