"""Star Catcher - catch the falling stars, dodge the meteors!

How to play: click the game window once, then use the Left and Right
arrow keys to move your basket. Stars are small five-pointed shapes
(+1 point). Meteors are big round rocks: each one you touch costs a
life. You have 3 lives. Press space to play again. Your best scores are
saved in star_catcher_scores.txt, next to this program.

This file only DRAWS and LISTENS for keys. The rules live in
starcatcher_logic.py, so they can be tested without opening a window.
"""

import turtle
from pathlib import Path

import starcatcher_logic as logic

SETTINGS = logic.SETTINGS

# The high-score file sits in the same folder as this program.
SCORE_FILE = Path(__file__).parent / "star_catcher_scores.txt"

# Okabe-Ito colors (safe for color-blind players). Stars and meteors
# also have different SHAPES and SIZES: nobody needs color to tell them
# apart.
SKY = "#000000"
TEXT_COLOR = "#F0E442"
BASKET_COLOR = "#56B4E9"
LOOKS = {
    # kind:     (shape,    size, color)
    "star":   ("star",   1.0, "#F0E442"),
    "meteor": ("circle", 1.8, "#D55E00"),
}
FONT = ("Arial", 16, "bold")

# A five-pointed star: the corner points, going round the shape.
STAR_SHAPE = ((0, 14), (-4, 5), (-13, 4), (-6, -2), (-8, -11),
              (0, -6), (8, -11), (6, -2), (13, 4), (4, 5))

game = {}    # the current game (filled in by logic.new_game)
view = {}    # the screen and the turtles (filled in by setup_window)


def setup_window():
    """Make the window, the turtles and the key bindings (only once)."""
    screen = turtle.Screen()
    screen.setup(600, 600)
    screen.title("Star Catcher")
    screen.bgcolor(SKY)
    screen.tracer(0)                  # we update once per tick
    screen.register_shape("star", STAR_SHAPE)

    basket = turtle.Turtle()
    basket.shape("square")
    basket.shapesize(1, 4)            # 1 tall and 4 wide: a flat basket
    basket.color(BASKET_COLOR)
    basket.penup()

    pen = turtle.Turtle()             # stamps every falling thing
    pen.hideturtle()
    pen.penup()
    pen.setheading(90)                # so the star points up

    hud = turtle.Turtle()             # writes the score and messages
    hud.hideturtle()
    hud.penup()
    hud.color(TEXT_COLOR)

    screen.onkey(go_left, "Left")     # no () after go_left: we pass the
    screen.onkey(go_right, "Right")   # function, turtle calls it later
    screen.onkey(play_again, "space")
    screen.listen()                   # without this, keys do nothing
    view.update(screen=screen, basket=basket, pen=pen, hud=hud)


def go_left():
    game["basket_x"] = logic.move_basket(game["basket_x"], -1, SETTINGS)


def go_right():
    game["basket_x"] = logic.move_basket(game["basket_x"], 1, SETTINGS)


def draw():
    """Draw one frame: falling things, basket, score line."""
    pen = view["pen"]
    pen.clearstamps()                 # rub out the last frame's shapes
    for obj in game["objects"]:
        shape, size, color = LOOKS[obj["kind"]]
        pen.shape(shape)
        pen.shapesize(size)
        pen.color(color)
        pen.goto(obj["x"], obj["y"])
        pen.stamp()
    view["basket"].goto(game["basket_x"], SETTINGS["basket_y"])

    hud = view["hud"]
    hud.clear()
    hud.goto(-280, 260)
    text = f"Score: {game['score']}    Lives: {game['lives']}"
    hud.write(text, font=FONT)
    view["screen"].update()


def game_loop():
    """One tick: update the rules, draw, then ask for the next tick."""
    logic.tick(game, SETTINGS)
    draw()
    if game["game_over"]:
        end_game()
    else:
        view["screen"].ontimer(game_loop, SETTINGS["tick_ms"])


def end_game():
    """Save the score in the high-score file and show the results."""
    scores = logic.load_high_scores(view["score_file"])
    keep = SETTINGS["keep_scores"]
    scores = logic.add_score(scores, game["score"], keep)
    logic.save_high_scores(view["score_file"], scores)
    hud = view["hud"]
    hud.goto(0, 0)
    hud.write(f"GAME OVER\nScore: {game['score']}   Best: {scores[0]}\n"
              "Press space to play again", align="center", font=FONT)
    view["screen"].update()


def play_again():
    """Start a new game, unless one is already running."""
    if game and not game["game_over"]:
        return
    # Change what is INSIDE the game dictionary (instead of making a new
    # one), so every function keeps seeing the same game.
    game.clear()
    game.update(logic.new_game(SETTINGS))
    draw()
    view["screen"].ontimer(game_loop, SETTINGS["tick_ms"])


def start_game(score_file=SCORE_FILE):
    """Open the window and start the first game."""
    setup_window()
    view["score_file"] = score_file
    play_again()


if __name__ == "__main__":
    start_game()
    turtle.done()
