# Dodge the Meteors - reference solution
# Move the turtle left and right. Meteors fall from the sky.
# Every meteor you dodge is worth 1 point. One hit and the game is over.
#
# Two parts:
#   LOGIC   - small functions with no turtle in them (easy to test)
#   DRAWING - turtles, keys and the game loop
# The game loop is ONE frame of the game. At the end it asks turtle to run
# it again in FRAME_MS milliseconds with screen.ontimer(game_loop, FRAME_MS).

import math
import random
import turtle

WALL = 270              # the player can go from -WALL to +WALL
PLAYER_Y = -250
PLAYER_STEP = 20
TOP = 300
BOTTOM = -300
METEOR_SPEED = 8
NUMBER_OF_METEORS = 4
HIT_DISTANCE = 30
FRAME_MS = 50           # 50 milliseconds = 20 frames every second


# ---------------------------------------- LOGIC

def clamp(value, low, high):
    """Return value, but never less than low and never more than high."""
    if value < low:
        return low
    if value > high:
        return high
    return value


def move_player(x, direction, step, limit):
    """New x after moving one step. direction is -1 (left) or 1 (right).
    The player never goes past -limit or +limit."""
    return clamp(x + direction * step, -limit, limit)


def is_touching(x1, y1, x2, y2, how_close):
    """True when the two points are closer than how_close."""
    return math.dist((x1, y1), (x2, y2)) < how_close


# ---------------------------------------- DRAWING

state = {"score": 0, "running": True}
meteors = []


def drop_from_the_top(meteor):
    """Put a meteor back above the screen at a random x."""
    meteor.goto(random.randint(-WALL, WALL), random.randint(TOP, TOP + 200))


def make_meteor():
    meteor = turtle.Turtle()
    meteor.shape("circle")
    meteor.color("#D55E00")
    meteor.shapesize(1.5)
    meteor.penup()
    drop_from_the_top(meteor)
    return meteor


def show_score():
    scorer.clear()
    scorer.write(f"Score: {state['score']}", align="center", font=("Arial", 18, "bold"))


def go_left():
    player.setx(move_player(player.xcor(), -1, PLAYER_STEP, WALL))


def go_right():
    player.setx(move_player(player.xcor(), 1, PLAYER_STEP, WALL))


def game_over():
    scorer.clear()
    scorer.write(f"GAME OVER!  Score: {state['score']}", align="center", font=("Arial", 22, "bold"))


def game_loop():
    """One frame: move every meteor, check for hits, then plan the next frame."""
    for meteor in meteors:
        meteor.sety(meteor.ycor() - METEOR_SPEED)
        if is_touching(meteor.xcor(), meteor.ycor(), player.xcor(), player.ycor(), HIT_DISTANCE):
            state["running"] = False
        elif meteor.ycor() < BOTTOM:
            drop_from_the_top(meteor)
            state["score"] = state["score"] + 1
            show_score()
    screen.update()
    if state["running"]:
        screen.ontimer(game_loop, FRAME_MS)   # run me again soon
    else:
        game_over()


if __name__ == "__main__":
    screen = turtle.Screen()
    screen.title("Dodge the Meteors - Left and Right arrows")
    screen.bgcolor("#000000")
    screen.tracer(0)        # we call screen.update() once per frame instead

    scorer = turtle.Turtle()
    scorer.hideturtle()
    scorer.penup()
    scorer.color("#F0E442")
    scorer.goto(0, 250)

    player = turtle.Turtle()
    player.shape("turtle")
    player.color("#56B4E9")
    player.shapesize(1.5)
    player.setheading(90)
    player.penup()
    player.goto(0, PLAYER_Y)

    for number in range(NUMBER_OF_METEORS):
        meteors.append(make_meteor())

    screen.onkey(go_left, "Left")
    screen.onkey(go_right, "Right")
    screen.listen()

    show_score()
    screen.ontimer(game_loop, FRAME_MS)   # start the game loop
    turtle.done()
