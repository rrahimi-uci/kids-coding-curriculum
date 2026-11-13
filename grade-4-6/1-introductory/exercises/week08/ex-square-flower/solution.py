# TEACHER REFERENCE SOLUTION: Square Flower
#
# What the program does: it draws 8 squares in 8 different colors. Each square
# is turned a little more than the one before, so together they look like a
# flower.
# Key ideas: a loop inside a loop (nested loops), and looping over the colors
# in a list.
# Approach: the outer loop takes one color at a time from PALETTE. For each
# color, the inner loop draws a whole square, then the turtle turns 45 degrees.

import turtle

# The color-blind-safe Okabe-Ito palette: 8 colors everyone can tell apart
PALETTE = ["#E69F00", "#56B4E9", "#009E73", "#F0E442",
           "#0072B2", "#D55E00", "#CC79A7", "#000000"]

t = turtle.Turtle()
t.shape("turtle")
t.pensize(3)
t.speed(0)          # 0 means the fastest drawing speed

# Outer loop: runs once for each color in the list, so 8 times.
for color in PALETTE:
    t.color(color)
    # Inner loop: draws one square. It is pushed in 4 more spaces, which
    # puts it inside the outer loop.
    for side in range(4):
        t.forward(100)
        t.left(90)
    # Turn a little before the next square. 8 turns x 45 degrees = 360, one
    # full circle, so the turtle ends up where it began and facing the same way.
    t.left(45)

turtle.done()

# Common mistakes children make here:
# - Leaving the square loop outside the color loop, so only one square is
#   drawn.
# - Putting t.left(45) inside the inner loop. It then turns 45 extra degrees
#   at every corner, and the squares are not squares any more.
# - Choosing a turn that does not fit the number of colors. 8 colors need
#   45 degrees (360 / 8).
# - Forgetting t.color(color), so every square has the same color.
#
# Another correct way: count the squares instead of walking through colors.
#   for number in range(8):
#       t.color(PALETTE[number])
#       for side in range(4):
#           t.forward(100)
#           t.left(90)
#       t.left(45)
