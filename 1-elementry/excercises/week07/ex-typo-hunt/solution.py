# Typo Hunt! - reference solution
# The 4 typos were: Print -> print, forwad -> forward,
# Right -> right, Done -> done.

import turtle

t = turtle.Turtle()
t.shape("turtle")
t.color("#0072B2")
t.pensize(4)

print("Typo hunt: fixed!")

# The pole goes up
t.left(90)
t.forward(150)

# The flag
t.right(90)
t.forward(80)
t.right(90)
t.forward(50)
t.right(90)
t.forward(80)

turtle.done()
