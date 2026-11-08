# Night Sky Postcard
# Reference solution for the Level 1 final project:
# "My Interactive Art Show".
#
# The program greets the viewer, asks two questions, then draws a
# postcard: a sky, a moon or a sun, random stars, green grass and
# a row of houses.
#
# Ingredients used: input(), variables, if/else, for loops, random
# and functions made with def (box and house).
#
# SMOKE: run  (lets the course's test robot open a real window)

import random
import turtle

# ===== PART 1: COLOURS =====
# Okabe-Ito colours: people with colour blindness can tell them apart.
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
screen.setup(800, 600)          # the window is 800 wide and 600 tall
screen.title("Night Sky Postcard")

t = turtle.Turtle()
t.speed(0)                      # 0 means "as fast as you can"
t.hideturtle()
t.pensize(2)


# ===== PART 3: MY OWN COMMANDS (FUNCTIONS) =====
def box(x, y, width, height, fill_colour):
    """Draw a filled rectangle with its bottom-left corner at (x, y)."""
    t.penup()
    t.goto(x, y)
    t.setheading(0)             # face right before we start
    t.pendown()
    t.color(BLACK, fill_colour)
    t.begin_fill()
    for side in range(2):       # long side, short side - twice!
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()


def house(x, y, colour):
    """Draw one house. (x, y) is the bottom-left corner of the walls."""
    # The walls: a 100 by 100 square in the house's own colour.
    box(x, y, 100, 100, colour)

    # The roof: a triangle that is a bit wider than the walls.
    t.penup()
    t.goto(x - 10, y + 100)
    t.setheading(0)
    t.pendown()
    t.color(BLACK, VERMILLION)
    t.begin_fill()
    for side in range(3):       # 3 sides, turn 360 / 3 = 120 each time
        t.forward(120)
        t.left(120)
    t.end_fill()

    # A door and two windows. The function box() does the work!
    box(x + 38, y, 25, 45, VERMILLION)
    box(x + 12, y + 60, 22, 22, YELLOW)
    box(x + 66, y + 60, 22, 22, YELLOW)


# ===== PART 4: GREET THE VIEWER AND ASK QUESTIONS =====
print("Welcome to my Interactive Art Show!")
print("Today's picture is called: Night Sky Postcard.")

answer = input("How many stars would you like? (1 to 200) ")
# isdigit() is True only for answers made of digits, like "25".
if answer.strip().isdigit():
    star_count = int(answer)
else:
    print("That is not a number, so I will draw 30 stars.")
    star_count = 30

if star_count > 200:
    print("That is a LOT of stars! I will draw 200.")
    star_count = 200

time_of_day = input("Should it be day or night? ")
time_of_day = time_of_day.strip().lower()   # "  Day " becomes "day"
if time_of_day != "day" and time_of_day != "night":
    print("Hmm, I don't know that one, so I will paint a night sky.")
    time_of_day = "night"

# ===== PART 5: CHOOSE COLOURS FOR DAY OR NIGHT =====
if time_of_day == "day":
    sky_colour = SKY_BLUE
    star_colour = WHITE         # daytime stars are pale and hard to see
else:
    sky_colour = BLACK
    star_colour = YELLOW
screen.bgcolor(sky_colour)

# ===== PART 6: SPRINKLE RANDOM STARS =====
for star in range(star_count):
    x = random.randint(-380, 380)
    y = random.randint(20, 280)     # only in the sky, above the houses
    size = random.randint(3, 9)
    t.penup()
    t.goto(x, y)
    t.dot(size, star_colour)

# ===== PART 7: THE SUN OR THE MOON =====
if time_of_day == "day":
    # Sun rays: 12 lines from the middle, turning 360 / 12 = 30.
    t.color(ORANGE)
    t.pensize(4)
    for ray in range(12):
        t.penup()
        t.goto(250, 190)
        t.setheading(ray * 30)
        t.pendown()
        t.forward(80)
    t.pensize(2)
    # The sun itself: a filled circle over the middle of the rays.
    t.penup()
    t.goto(250, 140)            # circle() starts at the bottom
    t.setheading(0)
    t.pendown()
    t.color(ORANGE, ORANGE)
    t.begin_fill()
    t.circle(50)
    t.end_fill()
else:
    # Crescent moon: a yellow circle, then a sky-coloured one on top.
    t.penup()
    t.goto(250, 140)
    t.setheading(0)
    t.pendown()
    t.color(YELLOW, YELLOW)
    t.begin_fill()
    t.circle(50)
    t.end_fill()
    t.penup()
    t.goto(275, 150)
    t.pendown()
    t.color(sky_colour, sky_colour)
    t.begin_fill()
    t.circle(45)
    t.end_fill()

# ===== PART 8: GRASS AND A ROW OF HOUSES =====
box(-400, -300, 800, 160, GREEN)

house(-290, -140, ORANGE)
house(-130, -140, PURPLE)
house(30, -140, BLUE)
house(190, -140, WHITE)

# ===== PART 9: THE POSTCARD MESSAGE =====
t.penup()
t.goto(0, -250)
t.color(BLACK)
t.write("Wish you were here!", align="center",
        font=("Arial", 24, "bold"))

print("Your postcard is ready! Close the window when you are done.")
turtle.done()
