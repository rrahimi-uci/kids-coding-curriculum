# My Big Build: my Python postcard
#
# This program already works. Press Run and look!
# You see an orange house with a purple roof.
#
# Make it yours! Change ONE line marked CHANGE ME.
# Press Run. Look. Then change the next one.
#
# SMOKE: run

import turtle

t = turtle.Turtle()
t.shape("turtle")
t.speed(3)          # CHANGE ME: 1 is slow, 10 is fast
t.pensize(5)        # CHANGE ME: a thinner or thicker pen

# The house: a square. 4 sides, a quarter turn (90).
t.color("orange")   # CHANGE ME: the color of the house
for i in range(4):
    t.forward(100)  # CHANGE ME: the size (all three 100s)
    t.left(90)

# Walk up the wall to the top, with the pen up.
t.penup()
t.left(90)
t.forward(100)      # the same number as the house
t.right(90)         # face right again
t.pendown()

# The roof: a triangle. The turn card says 120.
t.color("purple")   # CHANGE ME: the color of the roof
for i in range(3):
    t.forward(100)  # the same number as the house
    t.left(120)

turtle.done()
