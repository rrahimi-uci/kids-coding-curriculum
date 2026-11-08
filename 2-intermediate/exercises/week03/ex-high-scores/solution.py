# Top 3 High Scores - reference solution
# sorted(scores, reverse=True) makes a NEW list, biggest first.
# [:3] takes the first three items (or fewer, if the list is shorter).


def add_score(scores, new_score):
    """Add a new score to the list and return the list."""
    scores.append(new_score)
    return scores


def top_three(scores):
    """Return the three highest scores, biggest first."""
    best = sorted(scores, reverse=True)
    return best[:3]


def print_leaderboard(scores):
    """Print the top three with 1st, 2nd and 3rd in front."""
    places = ["1st", "2nd", "3rd"]
    best = top_three(scores)
    for i in range(len(best)):
        print(f"{places[i]}: {best[i]}")


if __name__ == "__main__":
    scores = [120, 45, 300, 80]
    print_leaderboard(scores)
    new_score = int(input("What did you score this time? "))
    add_score(scores, new_score)
    print("New leaderboard:")
    print_leaderboard(scores)
