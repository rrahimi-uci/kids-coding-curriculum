# Fair or biased?
# How do we know if our monster sorter is any good? We TEST it:
#   1. Split the cards into a TRAINING pile (to learn from) and a TEST pile
#      (kept secret, used only to check the guesses).
#   2. ACCURACY = how many test cards it labels correctly / how many test cards.
# Then we see what happens when the training pile is BIASED (unbalanced).

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


# ---------------------------------------------------------------- the classifier (from 9.1)
def distance(a, b):
    # (Given code.) Steps distance, as in 9.1: the gap in fluff plus the gap
    # in teeth. abs() gives the gap between two numbers (never below 0).
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def classify(training, mystery):
    best = training[0]
    for card in training:
        if distance(card, mystery) < distance(best, mystery):
            best = card
    return best[2]


# ---------------------------------------------------------------- testing the classifier
def label_counts(cards):
    """How many cards have each label, e.g. {"friendly": 8, "grumpy": 8}."""
    counts = {}
    # TODO 1: for each card, the label is card[2]. Count each label in the
    #         dictionary (the same trick as count_by in week 8).
    return counts


def split(cards):
    """Every 4th card goes in the TEST pile; the rest are for TRAINING."""
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
        return 0
    correct = 0
    # TODO 2: for each card in test, guess = classify(training, card).
    #         If the guess equals the true label card[2], add 1 to correct.
    return correct / len(test)


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
        print(f"  test card {card[:2]} is really {card[2]:8} -> biased guess: {classify(BIASED_TRAINING, card)}")
