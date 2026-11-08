# TEACHER REFERENCE SOLUTION: Homework 8 - Survey privacy
#
# What the program does: reads a snack survey that has nicknames and clubs,
# makes an anonymous copy with only the needed columns plus a plain ID
# (R1, R2, ...), saves it as snack_survey_anonymous.csv and counts snack
# votes.
# Key ideas: data privacy (nickname plus club could identify a person),
# keeping only what the question needs, and writing a CSV file.
# Approach: anonymize builds brand-new rows so the originals are never
# changed; save_csv writes them with csv.DictWriter, header line first.

import csv

IN_FILE = "snack_survey.csv"
OUT_FILE = "snack_survey_anonymous.csv"
KEEP = ["favorite_snack", "minutes_reading"]


def load_rows(filename):
    with open(filename, newline="") as f:
        return list(csv.DictReader(f))


def anonymize(rows, keep):
    """Return NEW rows with an 'id' (R1, R2, ...) and only the keep columns."""
    safe_rows = []
    # enumerate(..., start=1) hands us the row AND a counter that begins at 1.
    for number, row in enumerate(rows, start=1):
        safe = {"id": f"R{number}"}  # a plain ID replaces the nickname
        # Copy ONLY the wanted columns. Starting from an empty dictionary
        # (instead of deleting the bad columns) is safer: a column we forgot
        # about can never leak through.
        for column in keep:
            safe[column] = row[column]
        safe_rows.append(safe)
    return safe_rows


def save_csv(rows, filename):
    """Write a list of dictionaries to a CSV file (header row first)."""
    # "w" means write (it replaces the file). newline="" stops Windows from
    # adding blank lines between the rows of a CSV file.
    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()      # the column names go on the first line
        writer.writerows(rows)    # then one line per dictionary


def count_by(rows, column):
    # (Given code.) A tally: how many rows have each value in this column.
    counts = {}
    for row in rows:
        counts[row[column]] = counts.get(row[column], 0) + 1
    return counts


if __name__ == "__main__":
    answers = load_rows(IN_FILE)
    safe = anonymize(answers, KEEP)
    save_csv(safe, OUT_FILE)
    print("Saved", len(safe), "anonymous rows to", OUT_FILE)
    print("First row now looks like:", safe[0])
    print("Snack votes:", count_by(safe, "favorite_snack"))


# Common mistakes children make here:
#   - Leaving "return rows" from the starter: the program runs but the
#     nicknames are still shared.
#   - Using "safe = row" and deleting columns: that changes the original
#     data too, because both names point to the same dictionary.
#   - Opening the file with "r" (read) or leaving out writeheader(), so the
#     saved file has no column names.
#
# Another correct way: build each safe row with a dictionary expression.
#   safe = {"id": f"R{number}", **{c: row[c] for c in keep}}
