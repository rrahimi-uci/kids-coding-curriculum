# Save High Scores
# Right now the program FORGETS every score when it closes.
# Your job: save each score in a file, and read the file back.
# Each line of the file holds one game:   nickname,score
# Do the TODOs in order. Press Run after each one.

import random

SCORE_FILE = "high_scores.txt"


def save_score(filename, nickname, score):
    """Add one line 'nickname,score' to the end of the file."""
    # TODO 1: open the file in "a" (append) mode and write ONE line.
    # Hint:
    #     with open(filename, "a") as file:
    #         file.write(f"{nickname},{score}\n")
    pass


def load_scores(filename):
    """Return a list of [nickname, score] pairs, one for each line.
    If the file is missing, make an empty one and return []."""
    scores = []
    try:
        with open(filename, "r") as file:
            for line in file:
                # TODO 2: 1) line = line.strip()
                #         2) if the line is not empty (""):
                #         3)     parts = line.split(",")
                #         4)     append [parts[0], int(parts[1])] to scores
                pass
    except FileNotFoundError:
        # TODO 3: the file is missing. Make an empty one by opening it
        # in "w" (write) mode and writing "" (nothing).
        pass
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
