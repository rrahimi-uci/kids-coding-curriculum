# Leaderboard - reference solution
# sorted(..., key=...) sorts by whatever the key function returns.
# Each score is a tuple: (nickname, points).

SCORES = [("Ada", 120), ("Leo", 95), ("Mei", 150), ("Omar", 95), ("Zoe", 80)]


def points_of(entry):
    """Key function: the number we sort by."""
    return entry[1]


def name_of(entry):
    """Key function: the nickname in lower case, so 'ada' and 'Ada' sort together."""
    return entry[0].lower()


def top_scores(scores, n=3):
    """Return the n best entries, highest points first."""
    best_first = sorted(scores, key=points_of, reverse=True)
    return best_first[:n]


def alphabetical(scores):
    """Return the entries sorted A to Z by nickname."""
    return sorted(scores, key=name_of)


def rank_lines(scores):
    """Return lines like '1. Mei - 150'. Equal points share the same place."""
    lines = []
    best_first = sorted(scores, key=points_of, reverse=True)
    place = 0
    previous_points = None
    for position, entry in enumerate(best_first, start=1):
        if entry[1] != previous_points:
            place = position  # a new score starts a new place
        previous_points = entry[1]
        lines.append(f"{place}. {entry[0]} - {entry[1]}")
    return lines


if __name__ == "__main__":
    print("Top 3:", top_scores(SCORES))
    print("A to Z:", alphabetical(SCORES))
    print("Full board:")
    for line in rank_lines(SCORES):
        print("  " + line)
