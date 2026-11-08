# Square of Any Size
# input() asks a question in the Shell and waits for an answer.

import turtle

t = turtle.Turtle()
t.shape("turtle")
t.color("#D55E00")
t.pensize(3)

answer = input("How big should the square be? (try 50 to 250) ")

# BUG HUNT: input() always gives back TEXT, like "120".
# TODO: turn the text into a number with int( )
size = answer

print("Drawing a square with sides of", size)

for i in range(4):
    t.forward(size)
    t.left(90)

turtle.done()
