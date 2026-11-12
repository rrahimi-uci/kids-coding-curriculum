# Exercise 7.1 - Repeat 4
# "for i in range(2):" is like a Scratch repeat 2 block.
# The lines pushed in under it are inside the repeat.

import turtle

t = turtle.Turtle()
t.shape("turtle")

for i in range(2):    # CHANGE ME: 2 is too few for a square. Make it 4.
    t.forward(100)
    t.left(90)

turtle.done()
