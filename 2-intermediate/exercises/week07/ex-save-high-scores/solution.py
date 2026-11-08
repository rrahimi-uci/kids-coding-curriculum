# Save High Scores - reference solution
# Each line of the file holds one game:   nickname,score
# "a" (append) adds to the END of a file, and makes the file if it is missing.
# "r" (read) crashes with FileNotFoundError if the file is missing, so
# load_scores() catches that and makes an empty file, ready for next time.

import random

SCORE_FILE = "high_scores.txt"


def save_score(filename, nickname, score):
    """Add one line 'nickname,score' to the end of the file."""
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
                    scores.append([parts[0], int(parts[1])])
    except FileNotFoundError:
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
