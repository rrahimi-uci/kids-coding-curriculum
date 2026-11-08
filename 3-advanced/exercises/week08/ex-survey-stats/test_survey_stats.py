"""Checks for Exercise 8.2 - Survey stats."""

from pathlib import Path

DATA = Path(__file__).parent / "favorite_games.csv"
TINY = [{"genre": "puzzle"}, {"genre": "racing"}, {"genre": "puzzle"}]


def test_count_by_counts_each_value(load_target):
    program = load_target()
    got = program.count_by(TINY, "genre")
    assert got == {"puzzle": 2, "racing": 1}, f"count_by should give {{'puzzle': 2, 'racing': 1}}, not {got}."
    games = program.count_by(program.load_survey(DATA), "favorite_game")
    assert games.get("Block Craft") == 5, f"Block Craft has 5 votes in the survey, you counted {games.get('Block Craft')}."


def test_average(load_target):
    program = load_target()
    assert program.average([2, 4, 6]) == 4, "The average of 2, 4 and 6 is 4."
    assert program.average([1, 2]) == 1.5, "The average of 1 and 2 is 1.5 - did you divide by how many there are?"
    assert program.average([]) == 0, "An empty list should give 0 (and not crash)."


def test_average_hours_skips_missing_numbers(load_target):
    program = load_target()
    hours = program.numbers_in(program.load_survey(DATA), "hours_per_week")
    got = program.average(hours)
    assert got == 3.1, f"The average hours per week should be 3.1, not {got}."


def test_most_popular(load_target):
    program = load_target()
    assert program.most_popular({"a": 1, "b": 7, "c": 3}) == "b", "In {'a': 1, 'b': 7, 'c': 3} the biggest count belongs to 'b'."
    games = program.count_by(program.load_survey(DATA), "favorite_game")
    assert program.most_popular(games) == "Block Craft", "The most popular game in the survey is Block Craft."
