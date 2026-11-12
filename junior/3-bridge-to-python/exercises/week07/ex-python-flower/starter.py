# Exercise 7.3 - Python Flower
# The flower from Scratch week 1, now in Python: a repeat inside a repeat.

import turtle

t = turtle.Turtle()
t.shape("turtle")
t.speed(8)

for i in range(2):            # CHANGE ME: 2 squares. Make it 6.
    for side in range(4):     # this inner repeat draws one square
        t.forward(80)
        t.left(90)
    t.left(60)                # 60 comes from the turn card

turtle.done()
