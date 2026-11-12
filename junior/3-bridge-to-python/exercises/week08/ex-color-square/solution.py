"""TEACHER REFERENCE SOLUTION: Exercise 8.1 - Color My Square

What the child sees: the same square as last week, but in a color the
child picked and with a thick pen. The turtle is the same color.
Key idea: a working program is a great place to start. Change one thing,
press Run, look. Color names go inside quote marks.
"""

import turtle

t = turtle.Turtle()
t.shape("turtle")
# Change 1: "black" became "blue". Any color name Python knows is right:
# orange, blue, purple, green, gold, red, pink... The quote marks stay.
t.color("blue")
# Change 2: the pen size went from 1 to 5. Bigger numbers draw thicker
# lines. From 3 to about 20 looks good.
t.pensize(5)

# The square loop from week 7 did not change.
for i in range(4):
    t.forward(100)
    t.left(90)

turtle.done()

# Bug hunt (on paper and on the grown-up's computer): a misspelled color
# like "bleu" stops the program with red text that ends with
# "bad color string: bleu". Fix the spelling and press Run again.
# Common mistakes:
# - Deleting a quote mark: t.color("blue) gives red text about a string.
# - Spaces inside the name: "light blue" works in Tk, but keep to one word.
# - Writing the color in the comment instead of inside t.color( ).
