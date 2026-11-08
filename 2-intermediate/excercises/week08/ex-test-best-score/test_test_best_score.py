"""Checks for Exercise 8.2 - Test the Best Score.

YOU write the tests (in starter.py); these checks test YOUR tests.
Good tests PASS on the correct best_score() and FAIL on each of the three
broken versions below. Each bug hides in a different place, so you need a
normal test AND edge-case tests to catch them all.
"""

import types

from kidtest import load_module

FUNCTION = "best_score"


# ---- Three broken versions of best_score()

def best_returns_the_first(scores):
    if len(scores) == 0:
        return 0
    return scores[0]


def best_crashes_on_empty(scores):
    best = scores[0]  # IndexError when the list is empty
    for score in scores:
        if score > best:
            best = score
    return best


def best_skips_the_last(scores):
    if len(scores) == 0:
        return 0
    best = scores[0]
    for i in range(len(scores) - 1):  # off by one: never looks at the last score
        if scores[i] > best:
            best = scores[i]
    return best


# ---- Helpers (their names do not start with "test", so pytest skips them)

def student_tests(module):
    return [(name, obj) for name, obj in vars(module).items()
            if name.startswith("test") and callable(obj)]


def failing_tests(module, version):
    """Run every student test with best_score swapped for `version`.
    Return the names of the tests that failed (a crash counts as a fail)."""
    saved = dict(vars(module))
    module.__dict__[FUNCTION] = version
    for key, value in saved.items():  # also handles "import score_tools"
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
    return getattr(load_module(target_path.parent / "score_tools.py"), FUNCTION)


# ---- The checks

def test_you_wrote_at_least_3_tests(load_target):
    names = [name for name, _ in student_tests(load_target())]
    assert len(names) >= 3, f"Write at least 3 test functions (names start with test_). I found {len(names)}."


def test_your_tests_pass_on_the_correct_best_score(load_target, target_path):
    failed = failing_tests(load_target(), correct_version(target_path))
    assert not failed, (
        f"These tests FAILED on the correct best_score(): {failed}. "
        "score_tools.py is right, so check the expected answer in those tests."
    )


def test_your_tests_catch_a_version_that_returns_the_first_score(load_target):
    failed = failing_tests(load_target(), best_returns_the_first)
    assert failed, "A broken best_score() that just returns the FIRST score passed all your tests."


def test_your_tests_catch_a_version_that_crashes_on_an_empty_list(load_target):
    failed = failing_tests(load_target(), best_crashes_on_empty)
    assert failed, "A broken best_score() that crashes on an EMPTY list passed all your tests. Test best_score([])."


def test_your_tests_catch_a_version_that_skips_the_last_score(load_target):
    failed = failing_tests(load_target(), best_skips_the_last)
    assert failed, (
        "A broken best_score() that never looks at the LAST score passed all your tests. "
        "Test a list where the best score is at the end."
    )
