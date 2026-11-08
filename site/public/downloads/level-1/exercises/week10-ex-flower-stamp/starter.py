# Flower Stamp - make your own command with def

import turtle

# The color-blind-safe Okabe-Ito palette
PALETTE = ["#E69F00", "#56B4E9", "#009E73", "#F0E442",
           "#0072B2", "#D55E00", "#CC79A7", "#000000"]

t = turtle.Turtle()
t.speed(0)
t.hideturtle()


# A new command! flower(x, y) draws a flower with its middle at x, y.
# The lines pushed in under def are the RECIPE. They only run when we CALL it.
# TODO: add a third parameter called color, and use it in t.color(...)
def flower(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("#E69F00")
    for petal in range(6):
        t.begin_fill()
        t.circle(25)
        t.end_fill()
        t.left(60)
    t.dot(20, "#F0E442")    # the yellow middle


# TODO: call flower three times at different places, for example:
#   flower(-200, 0)

turtle.done()
