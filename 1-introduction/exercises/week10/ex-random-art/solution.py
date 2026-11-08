# TEACHER REFERENCE SOLUTION: Random Bubble Art
#
# What the program does: it draws 30 filled bubbles with random places, sizes
# and colors, so every Run makes a brand-new picture.
# Key ideas: the random module (randint picks a whole number, choice picks from
# a list), and calling our own command, bubble(...), inside a loop.
# Approach: in each of the 30 turns of the loop, pick four random values and
# hand them to bubble.

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
    # t.circle starts drawing from the BOTTOM of the circle, so we start one
    # radius lower. That way (x, y) ends up as the middle of the bubble.
    t.goto(x, y - size)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(size)
    t.end_fill()


for i in range(30):
    # The starter had fixed numbers here, so all 30 bubbles sat on top of each
    # other. Picking new random numbers on every turn spreads them out.
    x = random.randint(-350, 350)       # left to right across the screen
    y = random.randint(-250, 250)       # bottom to top
    size = random.randint(10, 50)       # radius of the bubble
    color = random.choice(PALETTE)      # one random color from the list
    bubble(x, y, size, color)

turtle.done()

# Common mistakes children make here:
# - Picking the random numbers OUTSIDE the loop. Then all 30 bubbles share one
#   place, size and color.
# - Writing random.randint(-350, 350) inside the bubble(...) call for only some
#   values, and forgetting one, so that part stays fixed.
# - Forgetting import random at the top, which gives a NameError.
# - Using random.randint(PALETTE) for the color. randint is for numbers.
#   random.choice is for picking from a list.
#
# Another correct way: pick the numbers right inside the call.
#   for i in range(30):
#       bubble(random.randint(-350, 350), random.randint(-250, 250),
#              random.randint(10, 50), random.choice(PALETTE))
