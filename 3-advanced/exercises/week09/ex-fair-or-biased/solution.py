# TEACHER REFERENCE SOLUTION: Exercise 9.2 - Fair or biased?
#
# What the program does: tests the nearest-neighbor monster sorter. It
# splits cards into a TRAINING pile and a secret TEST pile, measures
# accuracy, and compares a fair training pile (100%) with a biased one
# (only one friendly card, 50%).
# Key ideas: training versus test data, accuracy = correct / total, and
# how unbalanced (biased) training data makes a program unfair.
# Approach: label_counts tallies the labels so we can SEE the imbalance.
# accuracy asks the classifier to guess every test card and counts how many
# guesses match the true label. The classifier code is from Exercise 9.1.

# (fluff, teeth, label) - made-up monster cards
ALL_CARDS = [
    (9, 1, "friendly"), (2, 9, "grumpy"), (8, 2, "friendly"), (3, 8, "grumpy"),
    (1, 7, "grumpy"), (7, 3, "friendly"), (4, 9, "grumpy"), (6, 2, "friendly"),
    (8, 4, "friendly"), (2, 6, "grumpy"), (5, 3, "friendly"), (3, 6, "grumpy"),
    (1, 8, "grumpy"), (9, 3, "friendly"), (4, 7, "grumpy"), (6, 4, "friendly"),
]

# Someone collected these training cards but only ever met ONE friendly
# monster - a super-fluffy one. Lots of grumpy ones, though.
BIASED_TRAINING = [
    (10, 0, "friendly"),
    (2, 9, "grumpy"), (3, 8, "grumpy"), (1, 7, "grumpy"), (4, 9, "grumpy"),
    (2, 6, "grumpy"), (5, 6, "grumpy"), (6, 6, "grumpy"), (3, 5, "grumpy"),
]


# ---------------------- the classifier (from 9.1)
def distance(a, b):
    # (Given code.) Steps distance, as in 9.1: the gap in fluff plus the gap
    # in teeth. abs() gives the gap between two numbers (never below 0).
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def classify(training, mystery):
    # (Given code.) Copy the label of the closest training card.
    best = training[0]
    for card in training:
        if distance(card, mystery) < distance(best, mystery):
            best = card
    return best[2]


# ------------------------- testing the classifier
def label_counts(cards):
    """How many cards have each label, e.g. {"friendly": 8, "grumpy": 8}."""
    counts = {}
    for card in cards:
        label = card[2]  # each card is (fluff, teeth, label)
        # get(label, 0) gives 0 the first time a label appears.
        counts[label] = counts.get(label, 0) + 1
    return counts


def split(cards):
    """Every 4th card goes in the TEST pile; the rest are for TRAINING."""
    # (Given code.) A test card is never also a training card. Otherwise the
    # sorter could just look up the answer, which would be cheating.
    train, test = [], []
    for i, card in enumerate(cards):
        if i % 4 == 3:
            test.append(card)
        else:
            train.append(card)
    return train, test


def accuracy(training, test):
    """The fraction (0.0 to 1.0) of test cards the classifier gets right."""
    if len(test) == 0:
        return 0  # nothing to mark, and dividing by zero would crash
    correct = 0
    for card in test:
        # classify only reads the first two numbers, so the true label stored
        # in the card is not used for the guess; it is kept for marking.
        guess = classify(training, card)
        if guess == card[2]:          # card[2] is the true label
            correct += 1
    return correct / len(test)  # e.g. 3 right out of 4 -> 0.75


if __name__ == "__main__":
    train, test = split(ALL_CARDS)
    print("Training pile:", len(train), "cards", label_counts(train))
    print("Test pile:    ", len(test), "cards", label_counts(test))
    fair = accuracy(train, test)
    print(f"Fair training   -> accuracy {fair:.0%}")
    print("Biased pile:   ", label_counts(BIASED_TRAINING))
    biased = accuracy(BIASED_TRAINING, test)
    print(f"Biased training -> accuracy {biased:.0%}")
    for card in test:
        guess = classify(BIASED_TRAINING, card)
        print(f"  test card {card[:2]} is really {card[2]:8} -> biased guess: {guess}")


# Common mistakes children make here:
#   - Testing with the TRAINING cards: accuracy then looks perfect, but it
#     proves nothing because the sorter has already seen those cards.
#   - Dividing by len(training) instead of len(test), so accuracy is wrong.
#   - Using "=" instead of "==" when comparing guess and label, or putting
#     correct = 0 inside the loop so it resets every time.
#
# Another correct way for accuracy: count with a sum.
#   correct = sum(classify(training, c) == c[2] for c in test)
