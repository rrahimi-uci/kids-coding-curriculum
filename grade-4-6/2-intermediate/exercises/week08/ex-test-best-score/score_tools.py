"""best_score() finds the highest score in a list of scores.

    best_score([3, 9, 2])   gives 9
    best_score([40])        gives 40   (only one score)
    best_score([])          gives 0    (no games played yet)

Scores are whole numbers, 0 or more.
This file is correct. Do not change it: write tests for it in starter.py.
"""


def best_score(scores):
    """Return the biggest number in the list. An empty list gives 0."""
    if len(scores) == 0:
        return 0
    best = scores[0]
    for score in scores:
        if score > best:
            best = score
    return best
