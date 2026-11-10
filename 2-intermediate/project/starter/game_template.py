"""MY ARCADE GAME - starter template (project option A).

Run it first! Click the window, then use the arrow keys to move the square
and touch the coin before the time runs out. Then make it YOUR game by
working through the TODOs in number order (TODO 1, TODO 2, ...).

Project checklist - your finished game needs all of these:
  [ ] functions with parameters that return values (clamp, is_touching ...)
  [ ] a dictionary  (SETTINGS - add your own keys)
  [ ] a game loop   (game_loop + countdown use ontimer)
  [ ] a list        (TODO 3)
  [ ] a file        (TODO 4: save the high score)
  [ ] 3+ tests      (my_tests.py)
"""

import math
import random
import turtle

# Okabe-Ito colors: safe for color-blind players. Use shapes too!
PALETTE = ["#E69F00", "#56B4E9", "#009E73", "#F0E442",
           "#0072B2", "#D55E00", "#CC79A7", "#000000"]

# TODO 1: change these numbers and see how the game feels.
SETTINGS = {
    "step": 20,          # pixels per key press
    "wall": 270,         # the player stays between -wall and +wall
    "reach": 25,         # this close counts as touching
    "time_limit": 30,    # seconds in one game
    "tick_ms": 50,       # milliseconds between game-loop ticks
}

game = {"score": 0, "time_left": SETTINGS["time_limit"], "running": True}
view = {}   # the screen and turtles, filled in by setup_window()


# ---------- RULES: pure functions, no turtle. Test them in my_tests.py.

def clamp(value, low, high):
    """Return value, but never less than low and never more than high."""
    if value < low:
        return low
    if value > high:
        return high
    return value


def is_touching(x1, y1, x2, y2, reach):
    """True when point (x1, y1) is within reach of point (x2, y2)."""
    distance = math.dist((x1, y1), (x2, y2))   # straight-line distance (week 9)
    return distance <= reach


def add_points(score, points):
    """Return the new score."""
    return score + points


# TODO 4: write load_high_score(filename) and save_high_score(filename, score).
# Hint: workbook chapter 11 has a recipe ("a file for your high score"), and
# your week 7 work shows the same ideas. Open with "w" to write. Reading a
# file that does not exist yet gives FileNotFoundError - use try/except and
# give back 0.


# ---------- DRAWING AND KEYS

def setup_window():
    screen = turtle.Screen()
    screen.setup(600, 600)
    screen.title("My Arcade Game")
    screen.tracer(0)

    # TODO 2: make it look like YOUR game: a new title above, other shapes
    # ("turtle", "circle", "triangle") and colors from PALETTE. Good and bad
    # things should differ in shape or size, not only in color.
    player = turtle.Turtle()
    player.shape("square")
    player.color(PALETTE[4])
    player.penup()

    coin = turtle.Turtle()
    coin.shape("circle")
    coin.color(PALETTE[0])
    coin.penup()

    hud = turtle.Turtle()
    hud.hideturtle()
    hud.penup()

    screen.onkey(go_left, "Left")
    screen.onkey(go_right, "Right")
    screen.onkey(go_up, "Up")
    screen.onkey(go_down, "Down")
    screen.listen()
    view.update(screen=screen, player=player, coin=coin, hud=hud)


def move(dx, dy):
    """Move the player, but keep it inside the walls."""
    player = view["player"]
    wall = SETTINGS["wall"]
    x = clamp(player.xcor() + dx, -wall, wall)
    y = clamp(player.ycor() + dy, -wall, wall)
    player.goto(x, y)


def go_left():
    move(-SETTINGS["step"], 0)


def go_right():
    move(SETTINGS["step"], 0)


def go_up():
    move(0, SETTINGS["step"])


def go_down():
    move(0, -SETTINGS["step"])


def place_coin():
    wall = SETTINGS["wall"]
    view["coin"].goto(random.randint(-wall, wall), random.randint(-wall, wall))


def draw_hud():
    hud = view["hud"]
    hud.clear()
    hud.goto(-280, 260)
    hud.write(f"Score: {game['score']}   Time: {game['time_left']}",
              font=("Arial", 16, "bold"))


def game_loop():
    """Runs every tick_ms milliseconds while the game is running."""
    if not game["running"]:
        return
    player, coin = view["player"], view["coin"]
    if is_touching(player.xcor(), player.ycor(), coin.xcor(), coin.ycor(),
                   SETTINGS["reach"]):
        game["score"] = add_points(game["score"], 1)
        place_coin()
    # TODO 3: make a LIST of enemies (or extra coins). Move each one here
    # with a for loop, and check if the player touches it.
    # Recipe (like the meteors in Dodge the Meteors, week 9):
    #  a) At the end of setup_window(), make the list and keep it in view:
    #         enemies = []
    #         for number in range(3):
    #             enemy = turtle.Turtle("triangle")
    #             enemy.penup()
    #             enemy.goto(random.randint(-250, 250), 300)
    #             enemies.append(enemy)
    #         view["enemies"] = enemies
    #  b) Here, for every enemy in view["enemies"]: move it down a little
    #     (enemy.sety(enemy.ycor() - 5)), check is_touching() with the
    #     player, and send it back to the top when its y is below -300.
    draw_hud()
    view["screen"].update()
    view["screen"].ontimer(game_loop, SETTINGS["tick_ms"])


def countdown():
    """Runs once a second: the clock goes down until it reaches 0."""
    game["time_left"] = game["time_left"] - 1
    if game["time_left"] <= 0:
        game["running"] = False
        draw_hud()
        view["hud"].goto(0, 0)
        view["hud"].write("TIME UP!", align="center", font=("Arial", 24, "bold"))
        # TODO 4: save the score here if it is a new high score:
        #   best = load_high_score("highscore.txt")
        #   if game["score"] > best: save_high_score("highscore.txt", ...)
        # TODO 5: press space to play again. Write play_again(): if the game
        #   is not running, set the score to 0, time_left back to the time
        #   limit and running to True, then start game_loop and countdown
        #   again with ontimer (like start_game does). Connect it in
        #   setup_window() with screen.onkey(play_again, "space").
        view["screen"].update()
    else:
        view["screen"].ontimer(countdown, 1000)


def start_game():
    setup_window()
    place_coin()
    draw_hud()
    view["screen"].ontimer(game_loop, SETTINGS["tick_ms"])
    view["screen"].ontimer(countdown, 1000)


if __name__ == "__main__":
    start_game()
    turtle.done()
