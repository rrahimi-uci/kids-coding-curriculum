# TEACHER REFERENCE SOLUTION: Exercise 8.2 - Survey stats
#
# What the program does: loads the clean survey, then answers questions:
# how many votes each game got, which game is most popular (Block Craft,
# 5 votes), and the average hours per week (3.1) and stars.
# Key ideas: tallying with a dictionary, the average (mean), finding the
# biggest item, and leaving out missing values (None) before averaging.
# Approach: count_by builds a tally chart; average adds up and divides;
# most_popular walks through the tally and remembers the best so far.

import csv

FILENAME = "favorite_games.csv"


# ---------------------------------------- loading
# (This is the cleaner from Exercise 8.1, ready to use. Not part of the TODOs.)
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


# ---------------------------- your detective work
def count_by(rows, column):
    """Count how many rows have each value in this column.
    Example: count_by(rows, "genre") -> {"building": 5, "racing": 4, ...}"""
    counts = {}
    for row in rows:
        value = row[column]
        # get(value, 0) gives 0 the first time we meet a value, so we never
        # look up a key that is not there yet (that would crash).
        counts[value] = counts.get(value, 0) + 1
    return counts


def average(numbers):
    """The mean: add them all up, divide by how many. Rounded to 1 decimal.
    An empty list has no average, so give 0."""
    if len(numbers) == 0:
        return 0  # dividing by zero would crash, so an empty list gives 0
    return round(sum(numbers) / len(numbers), 1)


def most_popular(counts):
    """The key with the biggest count, e.g. 'Block Craft'."""
    best = None
    for key in counts:
        # The first key becomes the best at once; after that, a key only
        # takes over if it has MORE votes (so on a tie the earlier one stays).
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


# Common mistakes children make here:
#   - Writing counts[value] += 1 for a value that is not in the dictionary
#     yet, which crashes with a KeyError. Use counts.get(value, 0) + 1.
#   - In average, dividing by a fixed number or forgetting the empty-list
#     check, which gives a ZeroDivisionError.
#   - In most_popular, returning the biggest COUNT (like 5) instead of the
#     KEY (like "Block Craft"), or starting with best = 0.
#
# Another correct way for most_popular: max() with a key function.
#   return max(counts, key=counts.get) if counts else None
