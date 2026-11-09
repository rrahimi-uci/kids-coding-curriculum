# TEACHER REFERENCE SOLUTION: Flower Stamp
#
# What the program does: it makes a new command, flower(x, y, color), and uses
# it to stamp three flowers in three different colors, each with a yellow
# middle.
# Key ideas: def makes our own command, parameters (x, y, color) let one recipe
# draw many different flowers, and a recipe only runs when we CALL it.
# Approach: add the color parameter and use it in t.color(...). Then call
# flower three times at the bottom, with a different place and color each time.

import turtle

# The color-blind-safe Okabe-Ito palette
PALETTE = ["#E69F00", "#56B4E9", "#009E73", "#F0E442",
           "#0072B2", "#D55E00", "#CC79A7", "#000000"]

t = turtle.Turtle()
t.speed(0)
t.hideturtle()


# A new command! flower(x, y, color) draws a flower with its middle at x, y.
# The lines pushed in under def are the RECIPE. They only run when we CALL it.
# The names in the parentheses are blanks that get filled in at each call.
def flower(x, y, color):
    t.penup()               # lift the pen so moving to the spot draws nothing
    t.goto(x, y)
    t.pendown()
    t.color(color)          # uses the color given at the call, not a fixed one
    for petal in range(6):
        t.begin_fill()
        t.circle(25)        # one round petal
        t.end_fill()
        t.left(60)          # 6 petals x 60 degrees = 360, a full circle
    t.dot(20, "#F0E442")    # the yellow middle


# FIX 1: the starter never called flower, so the recipe never ran and the
# screen stayed empty. Each line below is a call. The numbers after the name
# fill in x, y and color, in that order.
flower(-200, 0, PALETTE[0])     # orange, on the left
flower(0, 0, PALETTE[6])        # pink, in the middle
flower(200, 0, PALETTE[4])      # dark blue, on the right

turtle.done()

# Common mistakes children make here:
# - Writing def flower(...) but never calling it. A recipe does nothing until
#   it is called.
# - Adding the color parameter but leaving t.color("#E69F00") inside, so every
#   flower is still orange.
# - Calling flower with only two numbers, which gives a red error because the
#   color is missing.
# - Putting the calls above the def. Python must read the recipe before it can
#   use it.
#
# Another correct way: call the command from a loop.
#   for number in range(3):
#       flower(-200 + number * 200, 0, PALETTE[number])
