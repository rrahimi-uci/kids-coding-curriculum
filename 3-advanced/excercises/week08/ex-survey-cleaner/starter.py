# Survey cleaner
# favourite_games.csv holds made-up, anonymous answers to the question
# "What is your favourite game?" (no names - just a response number).
# Real data is messy: extra spaces, MiXeD capitals, empty rows, missing
# numbers. A data detective CLEANS the data before counting anything.

import csv

FILENAME = "favourite_games.csv"


def to_number(text):
    """Turn text like ' 5 ' into the number 5. Empty text gives None."""
    # TODO 1: strip the spaces off text.
    #         If it is now empty, return None. Otherwise return int(text).
    return text


def is_empty(row):
    """A row with no favourite game is an empty answer: skip it."""
    # TODO 2: return True if row["favourite_game"] is empty after .strip()
    return False


def clean_row(row):
    """Return a tidy copy of one row from the CSV file."""
    return {
        "response": row["response"].strip(),
        "age_group": row["age_group"].strip(),
        # TODO 3: also use .title() so 'BLOCK CRAFT' and 'block craft'
        #         both become 'Block Craft'
        "favourite_game": row["favourite_game"].strip(),
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
        print(row["favourite_game"], "|", row["hours_per_week"], "hours |", row["stars"], "stars")
