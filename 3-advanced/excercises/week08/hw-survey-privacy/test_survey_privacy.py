"""Checks for Homework 8 - Survey privacy."""

import csv
from pathlib import Path

DATA = Path(__file__).parent / "snack_survey.csv"


def test_no_nicknames_or_clubs_left(load_target):
    program = load_target()
    safe = program.anonymise(program.load_rows(DATA), ["favourite_snack", "minutes_reading"])
    for row in safe:
        assert "nickname" not in row, "The anonymous rows must NOT contain the nickname column."
        assert "club" not in row, "The club column could help identify people - leave it out."


def test_rows_get_plain_ids(load_target):
    program = load_target()
    safe = program.anonymise(program.load_rows(DATA), ["favourite_snack"])
    ids = [row.get("id") for row in safe]
    assert ids == ["R1", "R2", "R3", "R4", "R5", "R6"], f"Each row needs an id R1, R2, ... R6. Got {ids}."


def test_answers_are_kept(load_target):
    program = load_target()
    safe = program.anonymise(program.load_rows(DATA), ["favourite_snack", "minutes_reading"])
    assert safe[1]["favourite_snack"] == "popcorn", "The answers themselves must stay the same (row 2 likes popcorn)."
    assert safe[1]["minutes_reading"] == "35", "Keep the minutes_reading answers too."


def test_save_csv_writes_a_file(load_target, tmp_path):
    program = load_target()
    rows = [{"id": "R1", "favourite_snack": "popcorn"}, {"id": "R2", "favourite_snack": "crackers"}]
    out = tmp_path / "out.csv"
    program.save_csv(rows, out)
    assert out.exists(), "save_csv should create the file."
    with open(out, newline="") as f:
        back = list(csv.DictReader(f))
    assert back == rows, "Reading the saved file back should give the same rows (did you write the header row?)."
