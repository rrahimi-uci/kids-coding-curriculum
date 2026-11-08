# Square of Any Size - reference solution
# input() asks a question in the Shell and waits for an answer.

import turtle

t = turtle.Turtle()
t.shape("turtle")
t.color("#D55E00")
t.pensize(3)

answer = input("How big should the square be? (try 50 to 250) ")

# input() always gives back TEXT, like "120".
# int() turns the text into the number 120.
size = int(answer)

print("Drawing a square with sides of", size)

for i in range(4):
    t.forward(size)
    t.left(90)

turtle.done()
