# Square Flower - a loop inside a loop

import turtle

# The color-blind-safe Okabe-Ito palette: 8 colors everyone can tell apart
PALETTE = ["#E69F00", "#56B4E9", "#009E73", "#F0E442",
           "#0072B2", "#D55E00", "#CC79A7", "#000000"]

t = turtle.Turtle()
t.shape("turtle")
t.pensize(3)
t.speed(0)

t.color(PALETTE[4])

# This loop draws ONE square.
for side in range(4):
    t.forward(100)
    t.left(90)

# TODO: put the square loop INSIDE a new loop, like this:
#   for color in PALETTE:
#       t.color(color)
#       ...the square loop, pushed in 4 more spaces...
#       t.left(45)

turtle.done()
