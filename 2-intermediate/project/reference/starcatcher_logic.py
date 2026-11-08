"""Star Catcher - the game RULES (no turtle in this file!).

Every function here takes some values and RETURNS an answer. Nothing is
drawn and no keys are read. That makes the rules easy to test with pytest
(see test_starcatcher_logic.py). The drawing lives in star_catcher.py.
"""

import random

# All the numbers that control the game live in ONE dictionary,
# so you can change how the game feels in one place.
SETTINGS = {
    "left_wall": -270,      # the basket cannot go further left than this
    "right_wall": 270,      # ... or further right than this
    "basket_y": -250,       # the basket slides along this line
    "basket_step": 30,      # pixels the basket moves per key press
    "top_y": 280,           # new stars and meteors appear here
    "bottom_y": -290,       # below this line a falling thing is gone
    "fall_speed": 5,        # pixels everything falls in one tick
    "catch_distance": 35,   # this close to the basket = "touching"
    "spawn_every": 12,      # a new star or meteor every 12 ticks
    "meteor_chance": 30,    # out of 100: how often it is a meteor
    "start_lives": 3,
    "tick_ms": 40,          # milliseconds between ticks (25 a second)
    "keep_scores": 5,       # how many high scores we remember
}

# Points for each kind of falling thing that lands in the basket.
POINTS = {"star": 1, "meteor": 0}


def new_game(settings):
    """Return a fresh game: one dict with everything that changes."""
    return {
        "basket_x": 0,
        "objects": [],          # falling things (each a small dict)
        "score": 0,
        "lives": settings["start_lives"],
        "ticks": 0,
        "game_over": False,
    }


def move_basket(x, direction, settings):
    """Return the basket's new x. direction is -1 (left) or 1 (right).
    The basket stops at the walls instead of sliding off the screen."""
    new_x = x + direction * settings["basket_step"]
    if new_x < settings["left_wall"]:
        new_x = settings["left_wall"]
    if new_x > settings["right_wall"]:
        new_x = settings["right_wall"]
    return new_x


def make_object(kind, x, settings):
    """Return one new falling thing ("star" or "meteor") at the top."""
    return {"kind": kind, "x": x, "y": settings["top_y"]}


def random_object(settings):
    """Return a star or, sometimes, a meteor at a random x position."""
    x = random.randint(settings["left_wall"], settings["right_wall"])
    if random.randint(1, 100) <= settings["meteor_chance"]:
        return make_object("meteor", x, settings)
    return make_object("star", x, settings)


def step_objects(objects, speed):
    """Return a NEW list where every object has fallen by speed pixels.
    (We build a new list so the old one is not changed by surprise.)"""
    moved = []
    for obj in objects:
        new_y = obj["y"] - speed
        moved.append({"kind": obj["kind"], "x": obj["x"], "y": new_y})
    return moved


def is_caught(obj, basket_x, settings):
    """True when the object is close enough to the basket to touch it."""
    dx = obj["x"] - basket_x
    dy = obj["y"] - settings["basket_y"]
    # Pythagoras, the same maths as turtle's distance()
    distance = (dx * dx + dy * dy) ** 0.5
    return distance <= settings["catch_distance"]


def has_fallen(obj, settings):
    """True when the object has dropped below the screen."""
    return obj["y"] < settings["bottom_y"]


def update_score(score, kind):
    """Return the new score after catching one thing of this kind."""
    return score + POINTS.get(kind, 0)


def tick(game, settings):
    """One frame of the game: maybe add a new thing, let everything fall,
    then check what landed in the basket. Changes game and returns it."""
    if game["game_over"]:
        return game
    game["ticks"] = game["ticks"] + 1
    if game["ticks"] % settings["spawn_every"] == 0:
        game["objects"].append(random_object(settings))

    still_falling = []
    for obj in step_objects(game["objects"], settings["fall_speed"]):
        if is_caught(obj, game["basket_x"], settings):
            game["score"] = update_score(game["score"], obj["kind"])
            if obj["kind"] == "meteor":
                game["lives"] = game["lives"] - 1
        elif not has_fallen(obj, settings):
            still_falling.append(obj)      # keep it for the next tick
    game["objects"] = still_falling

    if game["lives"] <= 0:
        game["game_over"] = True
    return game


def load_high_scores(filename):
    """Read high scores from a text file (one number per line).
    Return them as a list, best first.
    No file yet (first game ever)? That is fine: return an empty list."""
    try:
        with open(filename) as file:
            lines = file.readlines()
    except FileNotFoundError:
        return []
    scores = []
    for line in lines:
        line = line.strip()
        if line.isdigit():          # skip empty or broken lines
            scores.append(int(line))
    scores.sort(reverse=True)
    return scores


def add_score(scores, score, keep):
    """Return a NEW list: the old scores plus this one, best first,
    cut down to the best few (keep says how many)."""
    new_list = scores + [score]
    new_list.sort(reverse=True)
    return new_list[:keep]


def save_high_scores(filename, scores):
    """Write the scores to the file, one per line.
    Opening with "w" creates the file if it is missing."""
    with open(filename, "w") as file:
        for score in scores:
            file.write(f"{score}\n")
