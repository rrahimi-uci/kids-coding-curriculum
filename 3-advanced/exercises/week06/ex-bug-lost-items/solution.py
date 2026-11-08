# Bug Hunt 2: Lost Scores - FIXED version (teacher)
# The three bugs:
#   1. remaining = scores           -> remaining = list(scores)   (a copy!)
#   2. while len(remaining) > 1     -> while len(remaining) > 0   (last item was lost)
#   3. if smallest not in result    -> always append               (duplicates were lost)


def sort_scores(scores):
    """Return a NEW list with the same scores from smallest to largest.
    The original list must not change."""
    remaining = list(scores)
    result = []
    while len(remaining) > 0:
        smallest = remaining[0]
        for score in remaining:
            if score < smallest:
                smallest = score
        result.append(smallest)
        remaining.remove(smallest)
    return result


if __name__ == "__main__":
    scores = [40, 10, 30, 10, 50]
    print("Sorted:  ", sort_scores(scores))
    print("Original:", scores)
