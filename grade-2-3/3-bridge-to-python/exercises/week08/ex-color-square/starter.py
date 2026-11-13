# Exercise 8.1 - Color My Square
# This program works. Now make it yours!

import turtle

t = turtle.Turtle()
t.shape("turtle")
t.color("black")      # CHANGE ME: pick a color, like "blue" or "orange"
t.pensize(1)          # CHANGE ME: make the pen thicker, like 5

for i in range(4):
    t.forward(100)
    t.left(90)

turtle.done()
