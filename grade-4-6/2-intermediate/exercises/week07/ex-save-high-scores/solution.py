# TEACHER REFERENCE SOLUTION: Exercise 7.1 - Save High Scores
#
# What it does: a small dice game (Lucky Dice) that remembers every game in
# a text file, so the high score is still there after the program closes.
# Each line of the file holds one game:   nickname,score
# Key ideas: file modes ("a" adds to the end, "r" reads, "w" wipes and
# writes), turning text back into numbers with int(), and try / except to
# handle a file that does not exist yet.
# Approach: save_score() appends one line. load_scores() reads the lines
# back into [nickname, score] pairs, and if the file is missing it makes an
# empty one so the next game can start from a clean slate.

import random

SCORE_FILE = "high_scores.txt"


def save_score(filename, nickname, score):
    """Add one line 'nickname,score' to the end of the file."""
    # "a" (append) adds to the END and creates the file if it is missing.
    # "w" would wipe all earlier games every time, which is the classic bug.
    with open(filename, "a") as file:
        file.write(f"{nickname},{score}\n")


def load_scores(filename):
    """Return a list of [nickname, score] pairs, one for each line.
    If the file is missing, make an empty one and return []."""
    scores = []
    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()          # remove spaces and the "\n"
                if line != "":               # skip empty lines
                    parts = line.split(",")  # "Ada,120" -> ["Ada", "120"]
                    # The score came out of a file, so it is text. int() makes
                    # it a number, so we can compare scores later.
                    scores.append([parts[0], int(parts[1])])
    except FileNotFoundError:
        # Reading a missing file crashes, so we catch that case (first game
        # ever) and create an empty file. "w" is safe here: there is nothing
        # to wipe.
        with open(filename, "w") as file:
            file.write("")                   # an empty file
    return scores


def best_score(scores):
    """Return the [nickname, score] pair with the highest score.
    An empty list gives ["nobody yet", 0]."""
    best = ["nobody yet", 0]
    for entry in scores:
        if entry[1] > best[1]:
            best = entry
    return best


def roll_three_dice():
    """Roll three dice, print each roll, and return the total times 10."""
    total = 0
    for roll in range(3):
        die = random.randint(1, 6)
        print(f"Roll {roll + 1}: {die}")
        total = total + die
    return total * 10


if __name__ == "__main__":
    print("=== Lucky Dice: roll three dice and beat the high score! ===")
    nickname = input("Your nickname (not your real name): ")
    score = roll_three_dice()
    print(f"{nickname}, you scored {score}!")

    save_score(SCORE_FILE, nickname, score)
    scores = load_scores(SCORE_FILE)
    best = best_score(scores)
    print(f"Games saved so far: {len(scores)}")
    print(f"High score: {best[0]} with {best[1]}")


# Common mistakes children make here:
# - Opening with "w" in save_score(): only the newest game survives, because
#   "w" wipes the file first. "a" is the one that adds.
# - Forgetting "\n" when writing: all the games run together on one line.
# - Forgetting int(parts[1]): the scores stay as text, and best_score()
#   then crashes (text cannot be compared with the number 0).
# - Not skipping empty lines: an empty line has no comma, so parts[1] fails.
#
# Another correct way: unpack the two pieces with names instead of indexes:
#     name, points = line.split(",")
#     scores.append([name, int(points)])
