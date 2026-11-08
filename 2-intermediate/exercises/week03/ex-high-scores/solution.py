# TEACHER REFERENCE SOLUTION: Top 3 High Scores (Exercise 3.3)
#
# What the program does: it keeps a list of scores, prints the best three with
# "1st", "2nd" and "3rd" in front, asks for a new score, and prints the
# leaderboard again.
# Key ideas practiced: sorting a list, slicing a list, and looping with an index
# number to match two lists (places and scores) item by item.
# Approach: sorted(scores, reverse=True) makes a NEW list with the biggest first,
# and best[:3] keeps only the first three items. Because sorted() makes a copy,
# the original list of scores is not changed, so every score is remembered.


def add_score(scores, new_score):
    """Add a new score to the list and return the list."""
    scores.append(new_score)
    return scores


def top_three(scores):
    """Return the three highest scores, biggest first."""
    # The starter took scores[:3], which is just the first three in the order they
    # were added, not the best three. Sort first, then take three.
    best = sorted(scores, reverse=True)    # reverse=True puts the biggest first
    return best[:3]                        # if there are fewer than 3, this gives them all


def print_leaderboard(scores):
    """Print the top three with 1st, 2nd and 3rd in front."""
    places = ["1st", "2nd", "3rd"]
    best = top_three(scores)
    # range(len(best)) and not range(3): with fewer than 3 scores we must not run
    # past the end of the list. i is the same position in both lists.
    for i in range(len(best)):
        print(f"{places[i]}: {best[i]}")


if __name__ == "__main__":
    scores = [120, 45, 300, 80]
    print_leaderboard(scores)
    new_score = int(input("What did you score this time? "))
    add_score(scores, new_score)
    print("New leaderboard:")
    print_leaderboard(scores)


# Common mistakes children make here:
# - Forgetting reverse=True, so the three SMALLEST scores are shown.
# - Writing scores.sort() instead of sorted(scores): sort() rearranges the original
#   list and returns None, so "best = scores.sort()" leaves best empty.
# - Using range(3) in print_leaderboard: it crashes with IndexError when there are
#   fewer than three scores.
# - Slicing with best[3] instead of best[:3]: the first is one item, the second a list.
#
# Another correct way: zip pairs up two lists, so no index number is needed.
#   for place, score in zip(places, best):
#       print(f"{place}: {score}")
