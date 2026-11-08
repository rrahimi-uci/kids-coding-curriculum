"""My Data / AI App - starter template for project option (c).

This already works: press Run to load data/games.csv (made-up games, no
personal data), print a summary and draw a bar chart. Your job is to make
it YOURS: your own data, more questions, and a simple AI that predicts.
Look for the TODO comments.

Before you start, rename this file to a name nobody else uses,
for example game_guesser.py, and change the import in test_my_project.py.
"""

import csv
import turtle
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent / "data" / "games.csv"
NUMBER_COLUMNS = ["players", "minutes", "action", "puzzle", "rating"]
BAR_COLOURS = ["#0072B2", "#E69F00", "#009E73",
               "#CC79A7", "#56B4E9", "#D55E00"]


def clean_row(row):
    """Tidy one row: strip spaces, lower-case words, turn numbers into ints.
    Returns None for an empty row. A blank number becomes None."""
    row = {key: (value or "").strip() for key, value in row.items()}
    if not row["name"]:
        return None
    row["genre"] = row["genre"].lower()
    for column in NUMBER_COLUMNS:
        row[column] = int(row[column]) if row[column].isdigit() else None
    return row


class DataSet:
    """A DataSet HAS a list of rows (each row is a dictionary)."""

    def __init__(self, rows):
        self.rows = rows

    def count_by(self, column):
        """How many rows have each value? e.g. {"action": 5, "puzzle": 5}"""
        counts = {}
        for row in self.rows:
            counts[row[column]] = counts.get(row[column], 0) + 1
        return counts

    def average(self, column):
        """Average of a number column, ignoring blanks (None)."""
        values = [row[column] for row in self.rows if row[column] is not None]
        if not values:
            return 0
        return sum(values) / len(values)

    def top(self, column, n=3):
        """The n rows with the biggest value in column (a sort with key=)."""
        rows = [row for row in self.rows if row[column] is not None]
        return sorted(rows, key=lambda row: row[column], reverse=True)[:n]


def load_dataset(filename):
    with open(filename, newline="", encoding="utf-8") as file:
        rows = [clean_row(row) for row in csv.DictReader(file)]
    return DataSet([row for row in rows if row is not None])


def distance(a, b, features):
    """How different are two rows? Add up the gaps between their features."""
    return sum(abs(a[f] - b[f]) for f in features)


# TODO (AI): write nearest_neighbour(dataset, mystery, features) that finds
# the row with the SMALLEST distance to the mystery game and returns its
# genre. Try mystery = {"action": 5, "puzzle": 1}. Then test it!
# TODO (stretch): k-nearest neighbours - let the 3 closest rows vote.


def draw_bar_chart(counts, title):
    """Bars with the label AND the number written on them (not colour only)."""
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.penup()
    width, gap, scale = 60, 20, 40
    x = -(len(counts) * (width + gap)) / 2
    pen.goto(0, 180)
    pen.write(title, align="center", font=("Arial", 16, "bold"))
    for i, (label, count) in enumerate(sorted(counts.items())):
        pen.goto(x, -150)
        pen.color("black", BAR_COLOURS[i % len(BAR_COLOURS)])
        pen.pendown()
        pen.begin_fill()
        for side in [width, count * scale, width, count * scale]:
            pen.forward(side)
            pen.left(90)
        pen.end_fill()
        pen.penup()
        pen.goto(x + width / 2, -175)
        pen.write(label, align="center", font=("Arial", 12, "normal"))
        pen.goto(x + width / 2, -145 + count * scale)
        pen.write(str(count), align="center", font=("Arial", 12, "bold"))
        x += width + gap
    turtle.update()


def main():
    data = load_dataset(DATA_FILE)
    print(f"Loaded {len(data.rows)} games.")
    print("Average rating:", round(data.average("rating"), 1))
    for row in data.top("rating"):
        print(f"  {row['name']}: {row['rating']}")
    turtle.tracer(0)
    draw_bar_chart(data.count_by("genre"), "Games per genre")


if __name__ == "__main__":
    main()
    turtle.done()
