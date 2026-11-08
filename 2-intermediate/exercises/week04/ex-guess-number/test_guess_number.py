"""Checks for Exercise 4.1 - Guess My Number."""

import pytest


def test_play_counts_the_guesses(load_target, inputs):
    m = load_target()
    with inputs(["5", "15", "12"]):
        try:
            tries = m.play(12)
        except AssertionError:
            pytest.fail("The game kept asking after the right guess (12). Use break when the result is Correct.")
    assert tries == 3, f"Guessing 5, 15, then 12 is 3 tries, but play() returned {tries}. (TODO 1)"


def test_ask_number_ignores_words(load_target, inputs):
    m = load_target()
    with inputs(["banana", "7"]):
        try:
            number = m.ask_number(1, 20)
        except ValueError:
            pytest.fail("Typing 'banana' crashed the game. Check answer.isdigit() before int(). (TODO 2)")
    assert number == 7, f"After 'banana' then '7', ask_number should return 7, not {number}."


def test_ask_number_ignores_numbers_out_of_range(load_target, inputs):
    m = load_target()
    with inputs(["99", "0", "20"]):
        number = m.ask_number(1, 20)
    assert number == 20, f"99 and 0 are outside 1 to 20, so ask again. The answer should be 20, not {number}."


def test_whole_game_finishes(run_target):
    guesses = [str(n) for n in range(1, 21)]          # try 1, 2, 3 ... 20
    try:
        out = run_target(inputs=guesses, seed=4).stdout
    except AssertionError:
        pytest.fail("The game did not stop after the right guess. Use break (TODO 3).")
    assert "Correct" in out and "tries" in out, "The game should say Correct and how many tries it took."
