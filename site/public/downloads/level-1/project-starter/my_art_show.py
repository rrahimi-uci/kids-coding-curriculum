# My Interactive Art Show
# Made by: (write a nickname here - never your real full name)
#
# My idea in one sentence:
#   TODO: describe your picture or game here
#
# My program must use ALL of these ingredients. Check them off as you go:
#   [ ] input()   - asks the viewer at least one question
#   [ ] a variable - remembers an answer or a number
#   [ ] an if      - chooses what to draw from an answer
#   [ ] a loop     - for ... in range(...): repeats something
#   [ ] random     - adds a surprise
#   [ ] def        - at least one function I made myself
#
# Work in small steps: change one thing, press Run, look, then change the next.

import random
import turtle

# ===== PART 1: MY COLORS =====
# Color-blind-safe colors. Use these names instead of typing the codes.
ORANGE = "#E69F00"
SKY_BLUE = "#56B4E9"
GREEN = "#009E73"
YELLOW = "#F0E442"
BLUE = "#0072B2"
VERMILLION = "#D55E00"
PURPLE = "#CC79A7"
BLACK = "#000000"
WHITE = "#FFFFFF"

# ===== PART 2: SET UP THE SCREEN AND THE TURTLE =====
screen = turtle.Screen()
screen.setup(800, 600)          # x goes from -400 to 400, y from -300 to 300
screen.title("My Art Show")     # TODO: put the name of your artwork here

t = turtle.Turtle()
t.speed(0)                      # 0 = fastest
t.pensize(2)


# ===== PART 3: MY OWN COMMANDS (FUNCTIONS) =====
# This example function draws a square with its bottom-left corner at (x, y).
# TODO: change it into YOUR function (a flower, a fish, a robot, a star...)
#       and give it a name that says what it draws.
def my_shape(x, y, color):
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()
    t.color(BLACK, color)
    t.begin_fill()
    for side in range(4):
        t.forward(50)
        t.left(90)
    t.end_fill()


# ===== PART 4: GREET THE VIEWER AND ASK QUESTIONS =====
print("Welcome to my art show!")    # TODO: write your own greeting

# TODO: ask your first question and keep the answer in a variable.
# Example:  answer = input("How many fish? ")
#           fish_count = int(answer)
# Remember: never ask for real names, ages, addresses or other private things.


# ===== PART 5: MAKE A CHOICE WITH IF =====
# TODO: use if / elif / else to choose something from an answer.
# Example:  if mood == "happy":
#               screen.bgcolor(YELLOW)
#           else:
#               screen.bgcolor(BLUE)


# ===== PART 6: DRAW! USE A LOOP AND RANDOM =====
# This line uses the example function once so you can see it working.
# TODO: call YOUR function inside a loop, using random places or colors.
# Example:  for i in range(5):
#               x = random.randint(-350, 350)
#               my_shape(x, 0, PURPLE)
my_shape(-25, -25, ORANGE)


# ===== PART 7: FINISHING TOUCHES =====
# TODO (optional): write a title on the screen with t.write(...),
#                  hide the turtle with t.hideturtle()

print("Thank you for visiting my art show!")
turtle.done()
