# Bug Hunt 2: Lost Scores
# sort_scores should give back EVERY score, smallest first, and leave the
# original list alone. It has 3 bugs that make scores disappear!
# Expected output when fixed:
#   Sorted:   [10, 10, 30, 40, 50]
#   Original: [40, 10, 30, 10, 50]


def sort_scores(scores):
    """Return a NEW list with the same scores from smallest to largest.
    The original list must not change."""
    remaining = scores
    result = []
    while len(remaining) > 1:
        smallest = remaining[0]
        for score in remaining:
            if score < smallest:
                smallest = score
        if smallest not in result:
            result.append(smallest)
        remaining.remove(smallest)
    return result


if __name__ == "__main__":
    scores = [40, 10, 30, 10, 50]
    print("Sorted:  ", sort_scores(scores))
    print("Original:", scores)
