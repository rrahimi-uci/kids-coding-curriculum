# Pick a Colour
# The program asks a question, then CHOOSES what to do with if / elif / else.

import turtle

t = turtle.Turtle()
t.shape("turtle")
t.pensize(3)

colour_name = input("Pick a colour: orange, blue or green? ")

if colour_name == "orange":
    colour = "#E69F00"
elif colour_name == "blue":
    colour = "#0072B2"
# TODO: add an elif for "green" (use "#009E73")
# TODO: add an else: print a friendly message and use black "#000000"

# Paint a circle in the chosen colour
t.color(colour)
t.begin_fill()
t.circle(80)
t.end_fill()

# Write the colour name under the circle, so colour is not the only clue
t.penup()
t.goto(0, -40)
t.write(colour_name, align="center", font=("Arial", 20, "bold"))

turtle.done()
