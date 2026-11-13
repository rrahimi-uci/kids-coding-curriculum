# TEACHER REFERENCE SOLUTION: Typo Hunt
#
# What the program does: it prints "Typo hunt: fixed!" and then draws a
# pole with a flag at the top (4 lines in total).
# Key ideas: Python is picky about capital letters and spelling, and the red
# error message tells you the line number and what it did not understand.
# Approach: the starter has 4 typos. Each fixed line is marked FIX 1 to FIX 4
# below. The rest of the program is unchanged.

import turtle

t = turtle.Turtle()
t.shape("turtle")
t.color("#0072B2")
t.pensize(4)

# FIX 1: was Print(...). Python names are case sensitive, and print is all
# small letters, so the capital P made Python say "name 'Print' is not defined".
print("Typo hunt: fixed!")

# The pole goes up
t.left(90)
# FIX 2: was t.forwad(150). The word was spelled wrong, so the turtle did not
# know that move. It must be spelled forward.
t.forward(150)

# The flag
t.right(90)
t.forward(80)
# FIX 3: was t.Right(90). The capital R made it a different, unknown name.
# Turtle moves are all small letters.
t.right(90)
t.forward(50)
t.right(90)
t.forward(80)

# FIX 4: was turtle.Done(). It must be done with a small d, like the other
# turtle commands. This keeps the drawing window open.
turtle.done()

# Common mistakes children make here:
# - Fixing the first typo and thinking the program is finished. Python stops
#   at the first error, so run again and look for the next red message.
# - Changing a line that was already correct, because the error line number
#   points at the line where Python noticed the problem.
# - Fixing capital letters but missing a spelling mistake (forwad), or the
#   other way round.
# - Changing numbers on the flag lines, so the test no longer finds 4 lines.
