# Square Flower - reference solution
# The outer loop runs 8 times (once per colour).
# Each time, the inner loop draws a whole square.

import turtle

# The colour-blind-safe Okabe-Ito palette: 8 colours everyone can tell apart
PALETTE = ["#E69F00", "#56B4E9", "#009E73", "#F0E442",
           "#0072B2", "#D55E00", "#CC79A7", "#000000"]

t = turtle.Turtle()
t.shape("turtle")
t.pensize(3)
t.speed(0)

for colour in PALETTE:
    t.color(colour)
    for side in range(4):
        t.forward(100)
        t.left(90)
    t.left(45)          # 8 squares x 45 degrees = 360 degrees

turtle.done()
