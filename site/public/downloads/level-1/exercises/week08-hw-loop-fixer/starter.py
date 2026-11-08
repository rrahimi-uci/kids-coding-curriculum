# Loop Fixer
# This program has 2 bugs. Run it, watch, then fix them one at a time.

import turtle

t = turtle.Turtle()
t.shape("turtle")
t.pensize(3)

# A blue square
t.penup()
t.goto(-200, -50)
t.pendown()
t.color("#0072B2")
for i in range(3):
    t.forward(100)
    t.left(90)

# An orange star with 5 points
t.penup()
t.goto(50, 0)
t.pendown()
t.color("#E69F00")
for i in range(5):
    t.forward(150)
t.right(144)

turtle.done()
