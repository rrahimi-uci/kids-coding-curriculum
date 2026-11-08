"""Checks for Exercise 8.1 - Test the Clamp.

This exercise is upside down: YOU write the tests (in starter.py), and these
checks test YOUR tests. Good tests:
  * PASS when clamp() is correct, and
  * FAIL when clamp() has a bug. Below are three broken clamps.
    Your tests should catch every one of them.
"""

import types

from kidtest import load_module

FUNCTION = "clamp"


# ---- Three broken versions of clamp() (bug-catching practice)

def clamp_forgets_low(value, low, high):
    if value > high:
        return high
    return value


def clamp_forgets_high(value, low, high):
    if value < low:
        return low
    return value


def clamp_swaps_limits(value, low, high):
    if value < low:
        return high
    if value > high:
        return low
    return value


# ---- Helpers (their names do not start with "test", so pytest skips them)

def student_tests(module):
    return [(name, obj) for name, obj in vars(module).items()
            if name.startswith("test") and callable(obj)]


def failing_tests(module, version):
    """Run every student test with clamp swapped for `version`.
    Return the names of the tests that failed (a crash counts as a fail)."""
    saved = dict(vars(module))
    module.__dict__[FUNCTION] = version
    for key, value in saved.items():  # also handles "import clamp_tools"
        if isinstance(value, types.ModuleType) and hasattr(value, FUNCTION):
            module.__dict__[key] = types.SimpleNamespace(**{FUNCTION: version})
    failed = []
    try:
        for name, test in student_tests(module):
            try:
                test()
            except Exception:
                failed.append(name)
    finally:
        module.__dict__.clear()
        module.__dict__.update(saved)
    return failed


def correct_version(target_path):
    return getattr(load_module(target_path.parent / "clamp_tools.py"), FUNCTION)


# ---- The checks

def test_you_wrote_at_least_3_tests(load_target):
    names = [name for name, _ in student_tests(load_target())]
    assert len(names) >= 3, f"Write at least 3 test functions (names start with test_). I found {len(names)}."


def test_your_tests_pass_on_the_correct_clamp(load_target, target_path):
    failed = failing_tests(load_target(), correct_version(target_path))
    assert not failed, (
        f"These tests FAILED on the correct clamp(): {failed}. "
        "Check your expected answers: clamp_tools.py is right, so the test must be wrong."
    )


def test_your_tests_catch_a_clamp_that_forgets_the_low_limit(load_target):
    failed = failing_tests(load_target(), clamp_forgets_low)
    assert failed, "A broken clamp() that forgets the LOW limit passed all your tests. Test a value that is too small."


def test_your_tests_catch_a_clamp_that_forgets_the_high_limit(load_target):
    failed = failing_tests(load_target(), clamp_forgets_high)
    assert failed, "A broken clamp() that forgets the HIGH limit passed all your tests. Test a value that is too big."


def test_your_tests_catch_a_clamp_that_swaps_the_limits(load_target):
    failed = failing_tests(load_target(), clamp_swaps_limits)
    assert failed, "A broken clamp() that mixes up low and high passed all your tests. Test both sides."
