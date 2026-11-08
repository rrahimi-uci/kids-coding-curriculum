# Bug Hunt Station 2: High Scores - FIXED version (teacher)
# Bug 1: lowest() used index len(scores), one past the end. Use -1 (or len - 1).
# Bug 2: podium() always went round 3 times, even with only 2 scores.
#        Loop over len(best) instead.


def lowest(scores):
    """Return the lowest score."""
    in_order = sorted(scores)
    return in_order[0]


def highest(scores):
    """Return the highest score."""
    in_order = sorted(scores)
    return in_order[-1]


def podium(scores):
    """Return up to three lines like "1st: 90", best score first."""
    places = ["1st", "2nd", "3rd"]
    best = sorted(scores, reverse=True)[:3]
    lines = []
    for i in range(len(best)):
        lines.append(f"{places[i]}: {best[i]}")
    return lines


if __name__ == "__main__":
    scores = [40, 90, 15, 60]
    print(f"Highest: {highest(scores)}  Lowest: {lowest(scores)}")
    for line in podium(scores):
        print(line)
    for line in podium([70, 20]):          # only two players today
        print(line)
