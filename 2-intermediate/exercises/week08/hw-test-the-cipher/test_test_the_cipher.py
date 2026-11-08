"""Checks for Homework 8 - Test the Cipher.

YOU write the tests (in starter.py); these checks test YOUR tests.
Good tests PASS on the correct encode() and FAIL on each broken version below.
"""

import types

from kidtest import load_module

FUNCTION = "encode"
ALPHABET = "abcdefghijklmnopqrstuvwxyz"


# ---- Three broken versions of encode()

def encode_no_wrap(message, shift):
    secret = ""
    for letter in message:
        if letter in ALPHABET:
            secret = secret + chr(ord(letter) + shift)  # z + 1 is "{", not "a"
        else:
            secret = secret + letter
    return secret


def encode_loses_spaces(message, shift):
    secret = ""
    for letter in message:
        if letter in ALPHABET:
            secret = secret + ALPHABET[(ALPHABET.index(letter) + shift) % 26]
    return secret  # forgot the else: spaces and symbols disappear


def encode_goes_backwards(message, shift):
    secret = ""
    for letter in message:
        if letter in ALPHABET:
            secret = secret + ALPHABET[(ALPHABET.index(letter) - shift) % 26]
        else:
            secret = secret + letter
    return secret


# ---- Helpers (their names do not start with "test", so pytest skips them)

def student_tests(module):
    return [(name, obj) for name, obj in vars(module).items()
            if name.startswith("test") and callable(obj)]


def failing_tests(module, version):
    """Run every student test with encode swapped for `version`.
    Return the names of the tests that failed (a crash counts as a fail)."""
    saved = dict(vars(module))
    module.__dict__[FUNCTION] = version
    for key, value in saved.items():  # also handles "import cipher_tools"
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
    return getattr(load_module(target_path.parent / "cipher_tools.py"), FUNCTION)


# ---- The checks

def test_you_wrote_at_least_3_tests(load_target):
    names = [name for name, _ in student_tests(load_target())]
    assert len(names) >= 3, f"Write at least 3 test functions (names start with test_). I found {len(names)}."


def test_your_tests_pass_on_the_correct_encode(load_target, target_path):
    failed = failing_tests(load_target(), correct_version(target_path))
    assert not failed, (
        f"These tests FAILED on the correct encode(): {failed}. "
        "Check your expected answers with the paper cipher wheel."
    )


def test_your_tests_catch_a_cipher_that_does_not_wrap_round(load_target):
    failed = failing_tests(load_target(), encode_no_wrap)
    assert failed, "A broken encode() that does not wrap around after z passed all your tests. Try letters near z."


def test_your_tests_catch_a_cipher_that_loses_spaces(load_target):
    failed = failing_tests(load_target(), encode_loses_spaces)
    assert failed, "A broken encode() that throws away spaces and symbols passed all your tests."


def test_your_tests_catch_a_cipher_that_goes_backwards(load_target):
    failed = failing_tests(load_target(), encode_goes_backwards)
    assert failed, "A broken encode() that shifts the WRONG way passed all your tests."
