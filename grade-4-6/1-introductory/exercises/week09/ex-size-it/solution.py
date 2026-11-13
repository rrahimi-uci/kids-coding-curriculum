# TEACHER REFERENCE SOLUTION: Square of Any Size
#
# What the program does: it asks "How big?" in the Shell, then the turtle
# draws a square whose sides are that many steps long.
# Key ideas: input() gives back TEXT, and int() turns text into a number the
# turtle can use.
# Approach: the starter keeps the answer as text, which crashes at
# t.forward(size). One call to int() fixes it.

import turtle

t = turtle.Turtle()
t.shape("turtle")
t.color("#D55E00")
t.pensize(3)

answer = input("How big should the square be? (try 50 to 250) ")

# FIX 1: was size = answer. input() always gives back text, like "120", and
# the turtle cannot walk the text "120" steps. int() turns the text into the
# number 120 so t.forward(size) works.
size = int(answer)

print("Drawing a square with sides of", size)

for i in range(4):
    t.forward(size)
    t.left(90)

turtle.done()

# Common mistakes children make here:
# - Writing int(answer) on its own line without saving it. The result must be
#   stored, as in size = int(answer), or used directly.
# - Typing words like "big" or "120 steps" in the Shell. int() only understands
#   whole numbers. (Handling that is a later idea.)
# - Changing the 90 or the 4 in the loop, which stops the shape closing.
#
# Another correct way: change the text to a number on the same line as the
# question.
#   size = int(input("How big should the square be? (try 50 to 250) "))
