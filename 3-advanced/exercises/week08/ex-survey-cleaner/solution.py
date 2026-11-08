# TEACHER REFERENCE SOLUTION: Exercise 8.1 - Survey cleaner
#
# What the program does: reads a messy survey file (favorite_games.csv),
# tidies every answer, skips the empty ones, and prints how many clean
# answers there are (17) plus the first five.
# Key ideas: reading a CSV file, cleaning data (strip spaces, fix capital
# letters, turn text into numbers) and handling missing values with None.
# Approach: three small helper functions each fix one kind of mess:
# to_number (text -> number or None), is_empty (skip blank answers) and
# clean_row (tidy one row). load_survey then applies them to every row.

import csv

FILENAME = "favorite_games.csv"


def to_number(text):
    """Turn text like ' 5 ' into the number 5. Empty text gives None."""
    text = text.strip()  # int() cannot read spaces around digits
    if text == "":
        # Missing number: use None ("nothing here"), not 0. A fake 0 would
        # wrongly pull averages down later.
        return None
    return int(text)  # CSV files only hold text, so we turn it into a number


def is_empty(row):
    """A row with no favorite game is an empty answer: skip it."""
    # strip() first: an answer that is only spaces counts as empty too.
    return row["favorite_game"].strip() == ""


def clean_row(row):
    """Return a tidy copy of one row from the CSV file."""
    return {
        "response": row["response"].strip(),
        "age_group": row["age_group"].strip(),
        # strip() removes stray spaces and title() fixes the capitals, so
        # 'BLOCK CRAFT', ' block craft ' and 'Block Craft' all match when we
        # count them later.
        "favorite_game": row["favorite_game"].strip().title(),
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
            # Cleaning first, then keeping: only tidy rows reach the list.
            rows.append(clean_row(row))
    return rows


if __name__ == "__main__":
    survey = load_survey(FILENAME)
    print("Clean answers:", len(survey))
    for row in survey[:5]:
        print(row["favorite_game"], "|", row["hours_per_week"], "hours |", row["stars"], "stars")


# Common mistakes children make here:
#   - Writing text.strip() on its own line and not saving the result:
#     strings never change in place, so use text = text.strip().
#   - Writing the empty check as "text == None" or testing before strip(),
#     so a cell with only spaces gets through and int("") crashes.
#   - Forgetting that title() must be used on the cleaned value, or typing
#     .title without the () so the function itself is stored.
#
# Another correct way: check the text itself instead of comparing to "".
#   def is_empty(row):
#       return not row["favorite_game"].strip()
