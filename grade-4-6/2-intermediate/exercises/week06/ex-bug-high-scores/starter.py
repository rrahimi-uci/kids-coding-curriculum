# Bug Hunt Station 2: High Scores
# This program has TWO bugs. Both are IndexErrors.
# Tip: add print() lines to see what is inside a list, e.g.  print("best is", best)


def lowest(scores):
    """Return the lowest score."""
    in_order = sorted(scores)
    return in_order[0]


def highest(scores):
    """Return the highest score."""
    in_order = sorted(scores)
    return in_order[len(in_order)]


def podium(scores):
    """Return up to three lines like "1st: 90", best score first."""
    places = ["1st", "2nd", "3rd"]
    best = sorted(scores, reverse=True)[:3]
    lines = []
    for i in range(3):
        lines.append(f"{places[i]}: {best[i]}")
    return lines


if __name__ == "__main__":
    scores = [40, 90, 15, 60]
    print(f"Highest: {highest(scores)}  Lowest: {lowest(scores)}")
    for line in podium(scores):
        print(line)
    for line in podium([70, 20]):          # only two players today
        print(line)
