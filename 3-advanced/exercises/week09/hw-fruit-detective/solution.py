# TEACHER REFERENCE SOLUTION: Homework 9 - Fruit detective (k nearest neighbors)
#
# What the program does: guesses a fruit from its size and sweetness. With
# k = 1 one wrongly labeled card fools it (apple); with k = 3 the three
# closest cards vote and the wrong card is outvoted (lemon).
# Key ideas: k-nearest neighbors, sorting with key=, voting with a counting
# dictionary, and why one bad training example matters less with voting.
# Approach: k_nearest sorts all cards by distance to the mystery fruit and
# keeps the first k. vote counts the labels and returns the most common
# one, with ties going to the label that came first.

import math

# (size 1-10, sweetness 1-10, label) - made-up fruit cards
TRAINING = [
    (7, 8, "apple"), (6, 7, "apple"), (8, 7, "apple"), (7, 6, "apple"),
    (5, 2, "lemon"), (6, 1, "lemon"), (4, 2, "lemon"), (5, 1, "lemon"),
    (1, 9, "grape"), (2, 8, "grape"), (1, 7, "grape"), (2, 9, "grape"),
    (5, 3, "apple"),   # oops: someone labeled a lemon as an apple!
]


def distance(a, b):
    # (Given code.) Straight-line distance using the first two numbers.
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def k_nearest(training, point, k):
    """The k training cards closest to point, closest first."""
    # sorted() with key=: the lambda tells sorted() to compare cards by their
    # distance to the point, closest first. sorted() makes a new list, so
    # the TRAINING list itself is not reordered.
    by_distance = sorted(training, key=lambda card: distance(card, point))
    return by_distance[:k]  # slicing keeps just the first k cards


def vote(labels):
    """The label that appears most often. If there is a tie, the label
    that appears first in the list wins."""
    counts = {}
    for label in labels:
        counts[label] = counts.get(label, 0) + 1  # a tally chart of votes
    # Start with the first label, and change only for a STRICTLY bigger
    # count. That is why a tie goes to the label that appears first.
    winner = labels[0]
    for label in labels:
        if counts[label] > counts[winner]:
            winner = label
    return winner


def classify(training, point, k=3):
    # (Given code.) Take the k nearest cards, then let their labels vote.
    neighbors = k_nearest(training, point, k)
    return vote([card[2] for card in neighbors])


if __name__ == "__main__":
    mystery = (5, 4)
    print("Closest 3 cards:", k_nearest(TRAINING, mystery, 3))
    print("k = 1 says:", classify(TRAINING, mystery, k=1))
    print("k = 3 says:", classify(TRAINING, mystery, k=3))
    for fruit in [(7, 7), (2, 8), (6, 2)]:
        print(fruit, "->", classify(TRAINING, fruit))


# Common mistakes children make here:
#   - Sorting without key=, or comparing the whole card tuples, which sorts
#     by size first and not by distance.
#   - Returning the highest COUNT instead of the LABEL that has it, or
#     returning a list of labels from vote().
#   - Trying a very large k (like 13): every card votes, so the biggest
#     group always wins and local detail is lost.
#
# Another correct way for vote: use collections.Counter.
#   from collections import Counter
#   return Counter(labels).most_common(1)[0][0]
#   (Counter also breaks ties by first appearance.)
