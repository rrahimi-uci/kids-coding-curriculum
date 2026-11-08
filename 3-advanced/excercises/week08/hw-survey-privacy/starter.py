# Survey privacy (homework)
# snack_survey.csv has made-up answers - but it still has NICKNAMES and
# CLUBS in it. Put together, those could tell someone exactly who answered.
# Before sharing data, a careful data detective ANONYMISES it:
#   - keep only the columns the question really needs
#   - give each row a plain ID (R1, R2, ...) instead of a name

import csv

IN_FILE = "snack_survey.csv"
OUT_FILE = "snack_survey_anonymous.csv"
KEEP = ["favourite_snack", "minutes_reading"]


def load_rows(filename):
    with open(filename, newline="") as f:
        return list(csv.DictReader(f))


def anonymise(rows, keep):
    """Return NEW rows with an 'id' (R1, R2, ...) and only the keep columns."""
    safe_rows = []
    # TODO 1: loop with  for number, row in enumerate(rows, start=1):
    #         make a new dict  safe = {"id": f"R{number}"}
    #         copy ONLY the columns listed in keep:  safe[column] = row[column]
    #         and append safe to safe_rows.
    return rows   # <- this shares the nicknames! Return safe_rows instead.


def save_csv(rows, filename):
    """Write a list of dictionaries to a CSV file (header row first)."""
    # TODO 2 (challenge): open the file with "w" and newline="",
    #   writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    #   writer.writeheader()
    #   writer.writerows(rows)
    pass


def count_by(rows, column):
    counts = {}
    for row in rows:
        counts[row[column]] = counts.get(row[column], 0) + 1
    return counts


if __name__ == "__main__":
    answers = load_rows(IN_FILE)
    safe = anonymise(answers, KEEP)
    save_csv(safe, OUT_FILE)
    print("Saved", len(safe), "anonymous rows to", OUT_FILE)
    print("First row now looks like:", safe[0])
    print("Snack votes:", count_by(safe, "favourite_snack"))
