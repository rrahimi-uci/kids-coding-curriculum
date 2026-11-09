# TEACHER REFERENCE SOLUTION: Bug Hunt Station 2 - High Scores
#
# What it does: finds the highest and lowest score in a list and shows the
# top three scores as a podium ("1st: 90", "2nd: 60", ...).
# Key ideas: list index numbers start at 0, so a list of 4 items has indexes
# 0 to 3 (index 4 does not exist); and a loop must not run more times than
# the list has items.
# Approach: fix the two IndexErrors. highest() asked for one place past the
# end of the list, and podium() always looped 3 times even for a short list.


def lowest(scores):
    """Return the lowest score."""
    in_order = sorted(scores)         # smallest first, so the lowest is at index 0
    return in_order[0]


def highest(scores):
    """Return the highest score."""
    in_order = sorted(scores)         # smallest first, so the highest is at the END
    # FIX 1: in_order[len(in_order)] is one place past the end (4 scores have
    # indexes 0 to 3, not 4), which crashed. -1 means "the last item".
    return in_order[-1]


def podium(scores):
    """Return up to three lines like "1st: 90", best score first."""
    places = ["1st", "2nd", "3rd"]
    best = sorted(scores, reverse=True)[:3]   # biggest first, keep at most 3
    lines = []
    # FIX 2: range(3) always went around 3 times, but with only 2 scores
    # best[2] does not exist (IndexError). len(best) is the real number of
    # scores we have, so the loop never goes past the end of the list.
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


# Common mistakes children make here:
# - Changing highest() to in_order[len(in_order) + 1] or similar: the index
#   must be one LESS than the length, not more. The last index is len - 1.
# - Fixing podium() by padding the list or catching the error, instead of
#   making the loop match the list length.
# - Fixing podium() for [70, 20] by changing range(3) to range(2), which
#   then breaks the four-score podium (it would lose "3rd").
#
# Another correct way: let a loop walk the lists together, so no index is
# needed:
#     for place, score in zip(places, best):
#         lines.append(f"{place}: {score}")
