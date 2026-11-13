# Exercise 8.3 - My Square Block (stretch)
# def makes a new block, like a My Block in Scratch.

import turtle

t = turtle.Turtle()
t.shape("turtle")
t.color("blue")
t.pensize(3)


# This is the new block. It is called square.
# The lines pushed in under it are what the block does.
def square():
    for side in range(4):
        t.forward(60)
        t.left(90)


# Here we use the block.
for i in range(1):     # CHANGE ME: 1 square. Make it 4.
    square()
    t.left(90)

turtle.done()
