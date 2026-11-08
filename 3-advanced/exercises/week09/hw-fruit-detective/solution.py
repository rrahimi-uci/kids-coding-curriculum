# Fruit detective - reference solution
# k-NEAREST NEIGHBORS: instead of trusting only the single closest card,
# look at the k closest cards (k = 3) and let them VOTE.
# One wrongly-labeled card can fool k = 1, but it gets outvoted with k = 3.

import math

# (size 1-10, sweetness 1-10, label) - made-up fruit cards
TRAINING = [
    (7, 8, "apple"), (6, 7, "apple"), (8, 7, "apple"), (7, 6, "apple"),
    (5, 2, "lemon"), (6, 1, "lemon"), (4, 2, "lemon"), (5, 1, "lemon"),
    (1, 9, "grape"), (2, 8, "grape"), (1, 7, "grape"), (2, 9, "grape"),
    (5, 3, "apple"),   # oops: someone labeled a lemon as an apple!
]


def distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def k_nearest(training, point, k):
    """The k training cards closest to point, closest first."""
    # sorted() with key= (week 5): sort the cards by their distance to point
    by_distance = sorted(training, key=lambda card: distance(card, point))
    return by_distance[:k]


def vote(labels):
    """The label that appears most often. If there is a tie, the label
    that appears first in the list wins."""
    counts = {}
    for label in labels:
        counts[label] = counts.get(label, 0) + 1
    winner = labels[0]
    for label in labels:
        if counts[label] > counts[winner]:
            winner = label
    return winner


def classify(training, point, k=3):
    neighbors = k_nearest(training, point, k)
    return vote([card[2] for card in neighbors])


if __name__ == "__main__":
    mystery = (5, 4)
    print("Closest 3 cards:", k_nearest(TRAINING, mystery, 3))
    print("k = 1 says:", classify(TRAINING, mystery, k=1))
    print("k = 3 says:", classify(TRAINING, mystery, k=3))
    for fruit in [(7, 7), (2, 8), (6, 2)]:
        print(fruit, "->", classify(TRAINING, fruit))
