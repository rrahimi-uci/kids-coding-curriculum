"""clamp() keeps a number between a LOW limit and a HIGH limit.

Games use it to stop a player walking off the screen.

    clamp(5, 0, 10)   gives 5    (already inside, so it stays the same)
    clamp(-3, 0, 10)  gives 0    (too small, so it goes UP to the low limit)
    clamp(99, 0, 10)  gives 10   (too big, so it comes DOWN to the high limit)

This file is correct. Do not change it: write tests for it in starter.py.
"""


def clamp(value, low, high):
    """Return value, but never less than low and never more than high."""
    if value < low:
        return low
    if value > high:
        return high
    return value
