# Top 3 High Scores
# Keep a list of scores and show only the best three.


def add_score(scores, new_score):
    """Add a new score to the list and return the list."""
    scores.append(new_score)
    return scores


def top_three(scores):
    """Return the three highest scores, biggest first."""
    # TODO 1: this takes the first three, not the BEST three.
    # Sort a copy first:  best = sorted(scores, reverse=True)
    # then return best[:3]
    return scores[:3]


def print_leaderboard(scores):
    """Print the top three with 1st, 2nd and 3rd in front."""
    places = ["1st", "2nd", "3rd"]
    best = top_three(scores)
    # TODO 2: print each score with its place, like "1st: 300".
    # Tip: for i in range(len(best)):   then use places[i] and best[i]
    print(best)


if __name__ == "__main__":
    scores = [120, 45, 300, 80]
    print_leaderboard(scores)
    new_score = int(input("What did you score this time? "))
    add_score(scores, new_score)
    print("New leaderboard:")
    print_leaderboard(scores)
