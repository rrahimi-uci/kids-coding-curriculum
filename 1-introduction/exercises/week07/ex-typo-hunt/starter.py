# Typo Hunt!
# This program should draw a flag on a pole.
# It has 4 typos. Run it, read the red message, fix ONE typo, run again.

import turtle

t = turtle.Turtle()
t.shape("turtle")
t.color("#0072B2")
t.pensize(4)

Print("Typo hunt: fixed!")

# The pole goes up
t.left(90)
t.forwad(150)

# The flag
t.right(90)
t.forward(80)
t.Right(90)
t.forward(50)
t.right(90)
t.forward(80)

turtle.Done()
