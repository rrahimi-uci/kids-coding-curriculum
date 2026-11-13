# Random Bubble Art
# random makes surprises: a new picture every time you press Run.

import random
import turtle

# The color-blind-safe Okabe-Ito palette
PALETTE = ["#E69F00", "#56B4E9", "#009E73", "#F0E442",
           "#0072B2", "#D55E00", "#CC79A7", "#000000"]

t = turtle.Turtle()
t.speed(0)
t.hideturtle()


# bubble(x, y, size, color) draws a filled circle with its middle at x, y
def bubble(x, y, size, color):
    t.penup()
    t.goto(x, y - size)      # start at the bottom so (x, y) is the middle
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(size)
    t.end_fill()


for i in range(30):
    x = 0          # TODO: random.randint(-350, 350)
    y = 0          # TODO: random.randint(-250, 250)
    size = 30      # TODO: random.randint(10, 50)
    color = PALETTE[4]    # TODO: random.choice(PALETTE)
    bubble(x, y, size, color)

turtle.done()
