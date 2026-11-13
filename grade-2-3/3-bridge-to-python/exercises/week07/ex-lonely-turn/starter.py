# Exercise 7.2 - The Lonely Turn (bug hunt)
# This program should draw a square, but it has a bug.
# Press Run and watch: how many times does the turtle turn?

import turtle

t = turtle.Turtle()
t.shape("turtle")

for i in range(4):
    t.forward(80)
t.left(90)

turtle.done()
