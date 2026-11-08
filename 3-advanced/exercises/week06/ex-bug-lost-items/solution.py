# TEACHER REFERENCE SOLUTION: Bug Hunt 2 - Lost Scores (the sort that loses items)
#
# What the program does: sort_scores returns a NEW list holding every score
# from smallest to largest, and leaves the original list untouched.
# Key ideas: copying a list, loop stopping conditions, and duplicates.
# Approach: this is a "selection sort". Again and again, find the smallest
# score still waiting, move it into the result, and remove it from the
# waiting list, until nothing is waiting. Three bugs made scores vanish.
#
# The three bugs (marked FIX below):
#   FIX 1: remaining = scores         -> remaining = list(scores)
#   FIX 2: while len(remaining) > 1   -> while len(remaining) > 0
#   FIX 3: "if smallest not in result" check removed


def sort_scores(scores):
    """Return a NEW list with the same scores from smallest to largest.
    The original list must not change."""
    # FIX 1: "remaining = scores" only gives the SAME list a second name, so
    # removing from remaining also emptied the caller's list. list(scores)
    # makes a real copy that we are free to change.
    remaining = list(scores)
    result = []
    # FIX 2: keep going until the waiting list is empty. Stopping at
    # "> 1" left the very last score behind.
    while len(remaining) > 0:
        smallest = remaining[0]  # start by guessing the first one is smallest
        for score in remaining:
            if score < smallest:
                smallest = score
        # FIX 3: always add the smallest. The old "not in result" check threw
        # away repeats, so the second 10 was lost.
        result.append(smallest)
        # remove() deletes only the FIRST matching score, so a repeated
        # score stays in the waiting list for its own turn.
        remaining.remove(smallest)
    return result


if __name__ == "__main__":
    scores = [40, 10, 30, 10, 50]
    print("Sorted:  ", sort_scores(scores))
    print("Original:", scores)


# Common mistakes children make here:
#   - Fixing the loop but forgetting the copy: the sorted answer looks right
#     but the "Original" line prints [] (the list shrank too).
#   - Removing the "not in result" check but keeping "> 1", so the output
#     is still one score short.
#   - Using sort() on the original list: it sorts correctly but changes
#     the caller's list, which the README says must stay the same.
#
# Another correct way: let Python do the sorting on a copy.
#   return sorted(scores)   # sorted() already returns a new list
