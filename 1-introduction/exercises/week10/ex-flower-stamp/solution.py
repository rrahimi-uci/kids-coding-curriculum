# Flower Stamp - reference solution

import turtle

# The color-blind-safe Okabe-Ito palette
PALETTE = ["#E69F00", "#56B4E9", "#009E73", "#F0E442",
           "#0072B2", "#D55E00", "#CC79A7", "#000000"]

t = turtle.Turtle()
t.speed(0)
t.hideturtle()


# A new command! flower(x, y, color) draws a flower with its middle at x, y.
# The lines pushed in under def are the RECIPE. They only run when we CALL it.
def flower(x, y, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    for petal in range(6):
        t.begin_fill()
        t.circle(25)
        t.end_fill()
        t.left(60)
    t.dot(20, "#F0E442")    # the yellow middle


# Call (use) the new command three times
flower(-200, 0, PALETTE[0])
flower(0, 0, PALETTE[6])
flower(200, 0, PALETTE[4])

turtle.done()
