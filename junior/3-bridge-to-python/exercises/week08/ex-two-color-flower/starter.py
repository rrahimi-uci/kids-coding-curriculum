# Exercise 8.2 - Two-Color Flower
# Made by: the Kids Coding course.
# Changed by: (CHANGE ME: type your nickname here)

import turtle

t = turtle.Turtle()
t.shape("turtle")
t.pensize(3)
t.speed(8)

for i in range(3):
    t.color("purple")         # first color
    for side in range(4):
        t.forward(80)
        t.left(90)
    t.left(60)

    t.color("purple")         # CHANGE ME: second color, like "gold"
    for side in range(4):
        t.forward(80)
        t.left(90)
    t.left(60)

turtle.done()
