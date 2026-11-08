# Survey privacy - reference solution
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
    for number, row in enumerate(rows, start=1):
        safe = {"id": f"R{number}"}
        for column in keep:
            safe[column] = row[column]
        safe_rows.append(safe)
    return safe_rows


def save_csv(rows, filename):
    """Write a list of dictionaries to a CSV file (header row first)."""
    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


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
