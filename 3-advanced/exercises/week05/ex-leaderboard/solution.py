"""TEACHER REFERENCE SOLUTION: Leaderboard

What the program does: it takes a list of scores, each one a (nickname, points) pair, and
shows it three ways: the top 3 players, an A to Z list, and a full board where players with
equal points share a place (1st, 2nd, 3rd, 3rd, 5th).

Key ideas practiced: sorted(..., key=...) with a small "key function" that says what to sort
by, reverse=True, slicing a list, tuples, and a fair tie rule.

Approach: a key function returns the thing to compare (points, or the lowercase name).
sorted never changes the original list; it returns a new one. For ties, we remember the
previous score and only move to a new place number when the score changes.
"""

SCORES = [("Ada", 120), ("Leo", 95), ("Mei", 150), ("Omar", 95), ("Zoe", 80)]


def points_of(entry):
    """Key function: the number we sort by."""
    return entry[1]


def name_of(entry):
    """Key function: the nickname in lower case, so 'ada' and 'Ada' sort together."""
    # Step 1: without lower(), every capital letter sorts before every small letter,
    # so "Zoe" would come before "ada". Only the sort key is lowercased; the entry
    # itself keeps its original capitals.
    return entry[0].lower()


def top_scores(scores, n=3):
    """Return the n best entries, highest points first."""
    # Step 2: reverse=True puts the biggest points first.
    best_first = sorted(scores, key=points_of, reverse=True)
    # "[:n]" keeps the first n items (and is fine even if there are fewer than n).
    return best_first[:n]


def alphabetical(scores):
    """Return the entries sorted A to Z by nickname."""
    return sorted(scores, key=name_of)


def rank_lines(scores):
    """Return lines like '1. Mei - 150'. Equal points share the same place."""
    lines = []
    best_first = sorted(scores, key=points_of, reverse=True)
    place = 0
    previous_points = None  # nothing seen yet, so the first player always differs
    for position, entry in enumerate(best_first, start=1):
        # Step 3: the place only changes when the points change. For a tie we keep the old
        # place number, but position keeps counting, so after two 3rds comes 5th.
        if entry[1] != previous_points:
            place = position
        previous_points = entry[1]
        lines.append(f"{place}. {entry[0]} - {entry[1]}")
    return lines


if __name__ == "__main__":
    print("Top 3:", top_scores(SCORES))
    print("A to Z:", alphabetical(SCORES))
    print("Full board:")
    for line in rank_lines(SCORES):
        print("  " + line)


# Common mistakes children make here:
# - Forgetting reverse=True, so the LOWEST scores come first.
# - Using scores.sort(...), which changes the original list (a test checks it does not);
#   sorted(...) makes a new list.
# - Writing key=name_of(entry) or key=points_of() with brackets: the key must be the
#   function itself, so Python can call it on every entry.
# - In rank_lines, setting place = place + 1 for every player, which gives 3, 4 instead of
#   3, 3, or forgetting to update previous_points.
#
# Another correct way for the key functions (no def needed, a short "lambda"):
#     sorted(scores, key=lambda entry: entry[1], reverse=True)
