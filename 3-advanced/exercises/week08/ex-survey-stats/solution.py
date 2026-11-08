# Survey stats - reference solution
# Now the data is clean, a data detective asks questions:
#   Which game is most popular?  How long do people play, on average?
# Counting with a dictionary:  {"Block Craft": 5, "Kart Dash": 4, ...}

import csv

FILENAME = "favorite_games.csv"


# ---------------------------------------------------------------- loading
# (This is the cleaner from Exercise 8.1, ready to use.)
def to_number(text):
    text = text.strip()
    return None if text == "" else int(text)


def load_survey(filename):
    rows = []
    with open(filename, newline="") as f:
        for row in csv.DictReader(f):
            if row["favorite_game"].strip() == "":
                continue
            rows.append({
                "age_group": row["age_group"].strip(),
                "favorite_game": row["favorite_game"].strip().title(),
                "genre": row["genre"].strip().lower(),
                "hours_per_week": to_number(row["hours_per_week"]),
                "stars": to_number(row["stars"]),
            })
    return rows


def numbers_in(rows, column):
    """All the numbers in one column, leaving out missing ones (None)."""
    return [row[column] for row in rows if row[column] is not None]


# ---------------------------------------------------------------- your detective work
def count_by(rows, column):
    """Count how many rows have each value in this column.
    Example: count_by(rows, "genre") -> {"building": 5, "racing": 4, ...}"""
    counts = {}
    for row in rows:
        value = row[column]
        counts[value] = counts.get(value, 0) + 1   # 0 the first time we see it
    return counts


def average(numbers):
    """The mean: add them all up, divide by how many. Rounded to 1 decimal.
    An empty list has no average, so give 0."""
    if len(numbers) == 0:
        return 0
    return round(sum(numbers) / len(numbers), 1)


def most_popular(counts):
    """The key with the biggest count, e.g. 'Block Craft'."""
    best = None
    for key in counts:
        if best is None or counts[key] > counts[best]:
            best = key
    return best


if __name__ == "__main__":
    survey = load_survey(FILENAME)
    games = count_by(survey, "favorite_game")
    winner = most_popular(games)
    print("Answers:", len(survey))
    print("Votes per game:", games)
    print(f"Most popular game: {winner} with {games.get(winner, 0)} votes")
    print("Average hours per week:", average(numbers_in(survey, "hours_per_week")))
    print("Average stars:", average(numbers_in(survey, "stars")))
    for genre in count_by(survey, "genre"):
        same_genre = [row for row in survey if row["genre"] == genre]
        print(f"  {genre}: {average(numbers_in(same_genre, 'stars'))} stars on average")
