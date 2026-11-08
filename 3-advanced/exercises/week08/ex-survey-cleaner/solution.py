# Survey cleaner - reference solution
# favorite_games.csv holds made-up, anonymous answers to the question
# "What is your favorite game?" (no names - just a response number).
# Real data is messy: extra spaces, MiXeD capitals, empty rows, missing
# numbers. A data detective CLEANS the data before counting anything.

import csv

FILENAME = "favorite_games.csv"


def to_number(text):
    """Turn text like ' 5 ' into the number 5. Empty text gives None."""
    text = text.strip()
    if text == "":
        return None
    return int(text)


def is_empty(row):
    """A row with no favorite game is an empty answer: skip it."""
    return row["favorite_game"].strip() == ""


def clean_row(row):
    """Return a tidy copy of one row from the CSV file."""
    return {
        "response": row["response"].strip(),
        "age_group": row["age_group"].strip(),
        "favorite_game": row["favorite_game"].strip().title(),  # 'BLOCK CRAFT' -> 'Block Craft'
        "genre": row["genre"].strip().lower(),
        "hours_per_week": to_number(row["hours_per_week"]),
        "stars": to_number(row["stars"]),
    }


def load_survey(filename):
    """Read the CSV file and return a list of clean rows (dictionaries)."""
    rows = []
    with open(filename, newline="") as f:
        for row in csv.DictReader(f):     # each row is a dict: column -> text
            if is_empty(row):
                continue                   # skip empty answers
            rows.append(clean_row(row))
    return rows


if __name__ == "__main__":
    survey = load_survey(FILENAME)
    print("Clean answers:", len(survey))
    for row in survey[:5]:
        print(row["favorite_game"], "|", row["hours_per_week"], "hours |", row["stars"], "stars")
