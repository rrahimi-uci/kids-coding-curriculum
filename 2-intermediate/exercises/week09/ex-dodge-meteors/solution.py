# TEACHER REFERENCE SOLUTION: Exercise 9.2 - Dodge the Meteors
#
# What it does: an arcade game. You steer a blue turtle left and right with
# the arrow keys while orange meteors fall. Each meteor that reaches the
# ground scores 1 point. One hit and the game is over.
# Key ideas: event-driven programming (keys call our functions), a game loop
# that runs one frame at a time with screen.ontimer(), and collision
# detection by measuring the distance between two points.
# Approach: the LOGIC part (move_player, is_touching) has no turtle in it, so
# it is easy to test. The DRAWING part connects keys to handlers, and
# game_loop() moves the meteors, checks for hits, then schedules itself again.
#
# Layout of the file:
#   LOGIC   - small functions with no turtle in them (easy to test)
#   DRAWING - turtles, keys and the game loop

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
    # Work out where one step would land us, then let clamp() hold the player
    # back at the walls so the turtle cannot walk off the screen.
    return clamp(x + direction * step, -limit, limit)


def is_touching(x1, y1, x2, y2, how_close):
    """True when the two points are closer than how_close."""
    # math.dist measures the straight-line distance between two points.
    # "Less than" means touching; exactly how_close apart is only just missing.
    return math.dist((x1, y1), (x2, y2)) < how_close


# ---------------------------------------- DRAWING

state = {"score": 0, "running": True}   # one dictionary so functions can change it
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
    scorer.write(f"GAME OVER!  Score: {state['score']}", align="center",
                 font=("Arial", 22, "bold"))


def game_loop():
    """One frame: move every meteor, check for hits, then plan the next frame."""
    for meteor in meteors:
        meteor.sety(meteor.ycor() - METEOR_SPEED)
        if is_touching(meteor.xcor(), meteor.ycor(), player.xcor(), player.ycor(), HIT_DISTANCE):
            state["running"] = False
        elif meteor.ycor() < BOTTOM:
            # The meteor reached the ground without hitting us: a point!
            drop_from_the_top(meteor)
            state["score"] = state["score"] + 1
            show_score()
    # tracer(0) turned off automatic drawing, so we redraw once per frame.
    screen.update()
    if state["running"]:
        # Turtle will call game_loop again after FRAME_MS milliseconds. This
        # is what keeps the game going (no while loop, which would freeze the
        # window and make the keys stop working).
        screen.ontimer(game_loop, FRAME_MS)
    else:
        # No new timer is scheduled, so the loop simply stops here.
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

    # Hand over the functions themselves: no brackets after go_left, because
    # we want turtle to call them LATER, when the key is pressed.
    screen.onkey(go_left, "Left")
    screen.onkey(go_right, "Right")
    screen.listen()         # without this the window ignores the keyboard

    show_score()
    screen.ontimer(game_loop, FRAME_MS)   # start the game loop
    turtle.done()


# Common mistakes children make here:
# - Writing screen.onkey(go_left(), "Left") with brackets. That calls
#   go_left straight away (and passes its answer to onkey) instead of
#   waiting for the key.
# - Forgetting screen.listen(): the keys do nothing at all.
# - Forgetting the screen.ontimer line at the end of game_loop(): the
#   meteors move once and then stop.
# - Comparing only the x values in is_touching(): a meteor far above the
#   player would count as a hit. The distance must use both x and y.
# - Writing the clamp the wrong way round, e.g. clamp(x, limit, -limit),
#   which makes the player stick or jump.
#
# Another correct way: is_touching() without math.dist, using Pythagoras:
#     dx, dy = x1 - x2, y1 - y2
#     return (dx * dx + dy * dy) ** 0.5 < how_close
