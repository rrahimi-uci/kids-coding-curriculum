"""Checks for Exercise 8.1 - Survey cleaner."""

from pathlib import Path

DATA = Path(__file__).parent / "favourite_games.csv"


def test_to_number_turns_text_into_numbers(load_target):
    program = load_target()
    assert program.to_number(" 5 ") == 5, "to_number(' 5 ') should give the NUMBER 5 (strip, then int)."
    assert program.to_number("") is None, "to_number('') should give None: there is no number."


def test_empty_rows_are_skipped(load_target):
    program = load_target()
    rows = program.load_survey(DATA)
    assert len(rows) == 17, f"The file has 17 real answers and 2 empty rows. You kept {len(rows)} rows."


def test_numbers_are_numbers(load_target):
    program = load_target()
    for row in program.load_survey(DATA):
        hours = row["hours_per_week"]
        assert hours is None or isinstance(hours, int), \
            f"hours_per_week should be a number (or None if missing), but found {hours!r}."


def test_game_names_are_tidy(load_target):
    program = load_target()
    names = {row["favourite_game"] for row in program.load_survey(DATA)}
    assert "Block Craft" in names, "'Block Craft' should be in the clean data."
    messy = [n for n in names if n != n.strip() or n != n.title()]
    assert not messy, f"These names still have extra spaces or mixed capitals: {messy}"
    assert len(names) == 6, f"After cleaning there are 6 different games, but you have {len(names)}: {sorted(names)}"
