# TEACHER REFERENCE SOLUTION: Exercise 9.1 - Monster sorter (nearest neighbor)
#
# What the program does: learns from example "monster cards" (fluffiness,
# number of teeth, and a label friendly/grumpy), then guesses the label of
# new mystery monsters and draws a chart showing the guesses.
# Key ideas: machine learning from examples (no hand-written rules),
# features and labels, distance between points, and "find the smallest".
# Approach: distance measures how far apart two cards are on the chart
# (Pythagoras). nearest keeps the closest card seen so far while looping
# over all cards. classify then copies the label of that nearest card.

import math
import turtle

# (fluff, teeth, label) - made-up training cards
TRAINING = [
    (9, 1, "friendly"), (8, 2, "friendly"), (7, 3, "friendly"),
    (6, 1, "friendly"), (8, 4, "friendly"),
    (2, 9, "grumpy"), (3, 8, "grumpy"), (1, 7, "grumpy"),
    (4, 9, "grumpy"), (2, 6, "grumpy"),
]
MYSTERY = [(5, 2), (3, 6), (5, 5)]

SCALE = 36            # pixels per point on the chart
ORIGIN = (-180, -180)  # where (0, 0) goes on the screen


def distance(a, b):
    """Straight-line distance between two cards, using their first two
    numbers (fluff, teeth). Pythagoras: sqrt(dx*dx + dy*dy)."""
    dx = a[0] - b[0]  # how far apart in fluff
    dy = a[1] - b[1]  # how far apart in teeth
    # Pythagoras: the straight line between two points is the long side of a
    # right-angled triangle with sides dx and dy. We use only a[0], a[1] so
    # the label (a[2]) is ignored, which lets us compare a card with a
    # mystery monster that has no label.
    return math.sqrt(dx * dx + dy * dy)


def nearest(training, mystery):
    """The training card closest to the mystery monster."""
    best = training[0]  # start by assuming the first card is the closest
    for card in training:
        # Only a STRICTLY closer card replaces best, so on an exact tie the
        # earlier card keeps its place.
        if distance(card, mystery) < distance(best, mystery):
            best = card
    return best


def classify(training, mystery):
    """Guess the label: copy the label of the nearest card."""
    return nearest(training, mystery)[2]  # index 2 is the label


# ---------------------------------------- drawing
# Everything below is given code that draws the chart. It is not part of
# the exercise. Each card shows a LETTER and a SHAPE (F circle, G square),
# so the chart can be read without telling colors apart.
def to_screen(fluff, teeth):
    return ORIGIN[0] + fluff * SCALE, ORIGIN[1] + teeth * SCALE


def draw_axes(t):
    x0, y0 = to_screen(0, 0)
    x1, y1 = to_screen(10, 10)
    t.penup(); t.goto(x0, y0); t.pendown(); t.goto(x1, y0)
    t.penup(); t.goto(x0, y0); t.pendown(); t.goto(x0, y1)
    t.penup(); t.goto(x1 - 40, y0 - 30)
    t.write("fluff ->", align="center", font=("Arial", 12, "normal"))
    t.goto(x0 - 10, y1 + 10)
    t.write("teeth", align="center", font=("Arial", 12, "normal"))


def draw_card(t, fluff, teeth, label):
    """Friendly = orange circle with F, grumpy = blue square with G."""
    x, y = to_screen(fluff, teeth)
    t.penup()
    if label == "friendly":
        t.goto(x, y - 12)
        t.fillcolor("#E69F00")
        t.pendown(); t.begin_fill(); t.circle(12); t.end_fill()
        letter = "F"
    else:
        t.goto(x - 11, y - 11)
        t.setheading(0)
        t.fillcolor("#56B4E9")
        t.pendown(); t.begin_fill()
        for _ in range(4):
            t.forward(22); t.left(90)
        t.end_fill()
        letter = "G"
    t.penup(); t.goto(x, y - 8)
    t.write(letter, align="center", font=("Arial", 11, "bold"))


def draw_link(t, training, mystery):
    """A line from the mystery monster to its nearest neighbor."""
    near = nearest(training, mystery)
    t.penup(); t.goto(*to_screen(*mystery)); t.pendown()
    t.pensize(2)
    t.goto(*to_screen(near[0], near[1]))
    t.pensize(1)


def draw_mystery(t, training, mystery):
    """A white circle with '?', and the guess written above it."""
    x, y = to_screen(*mystery)
    t.penup(); t.goto(x, y - 12)
    t.fillcolor("white")
    t.pendown(); t.begin_fill(); t.circle(12); t.end_fill()
    t.penup(); t.goto(x, y - 9)
    t.write("?", align="center", font=("Arial", 13, "bold"))
    t.goto(x, y + 14)
    t.write("guess: " + classify(training, mystery), align="center", font=("Arial", 10, "normal"))


if __name__ == "__main__":
    for m in MYSTERY:
        print(m, "->", classify(TRAINING, m))
    screen = turtle.Screen()
    screen.title("Monster sorter: nearest neighbor")
    screen.tracer(0)
    pen = turtle.Turtle()
    pen.hideturtle()
    draw_axes(pen)
    for m in MYSTERY:
        draw_link(pen, TRAINING, m)     # lines first, so the cards sit on top
    for card in TRAINING:
        draw_card(pen, *card)
    for m in MYSTERY:
        draw_mystery(pen, TRAINING, m)
    screen.update()
    turtle.done()


# Common mistakes children make here:
#   - Forgetting the squares: sqrt(dx + dy) gives wrong distances (and
#     crashes when dx + dy is negative). Forgetting only the sqrt still
#     finds the same nearest card, but distance((0, 0), (3, 4)) is 25, not 5.
#   - Using abs(dx) + abs(dy) (taxi distance): it can pick a different
#     "nearest" card for some mystery monsters.
#   - Using ">" instead of "<" in nearest, which finds the FARTHEST card
#     (the guesses usually come out backwards).
#
# Another correct way for nearest: min() with a key function.
#   return min(training, key=lambda card: distance(card, mystery))
