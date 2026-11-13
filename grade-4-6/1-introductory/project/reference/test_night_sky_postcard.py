"""Checks for the Level 1 reference project: Night Sky Postcard."""

from pathlib import Path

from kidtest import load_module, run_script

PROGRAM = Path(__file__).parent / "night_sky_postcard.py"

YELLOW = "#F0E442"
WHITE = "#FFFFFF"
BLACK = "#000000"
SKY_BLUE = "#56B4E9"
HOUSE_COLORS = ["#E69F00", "#CC79A7", "#0072B2", "#FFFFFF"]


def stars_drawn(result, star_color):
    """Stars are the dots drawn in the star color."""
    return [d for d in result.turtle.dots if d.color == star_color]


def test_greets_the_viewer_and_asks_two_questions():
    result = run_script(PROGRAM, inputs=["10", "night"], seed=1)
    assert "welcome" in result.stdout.lower(), "The program should greet the viewer with a welcome message."
    assert len(result.prompts) == 2, f"The program should ask 2 questions, but it asked {len(result.prompts)}."


def test_draws_the_number_of_stars_asked_for():
    for count in [1, 25, 80]:
        result = run_script(PROGRAM, inputs=[str(count), "night"], seed=2)
        drawn = len(stars_drawn(result, YELLOW))
        assert drawn == count, f"The viewer asked for {count} stars, but {drawn} were drawn."


def test_stars_are_in_random_places_inside_the_sky():
    first = run_script(PROGRAM, inputs=["20", "night"], seed=3)
    second = run_script(PROGRAM, inputs=["20", "night"], seed=4)
    places_1 = [d.pos for d in stars_drawn(first, YELLOW)]
    places_2 = [d.pos for d in stars_drawn(second, YELLOW)]
    assert places_1 != places_2, "Stars should land in random places, different each time."
    for x, y in places_1 + places_2:
        assert -400 <= x <= 400 and 0 <= y <= 300, f"A star at ({x}, {y}) is outside the sky."


def test_night_sky_is_dark_and_day_sky_is_light():
    night = run_script(PROGRAM, inputs=["5", "night"], seed=5)
    day = run_script(PROGRAM, inputs=["5", "  DAY "], seed=5)
    assert night.screen.bg == BLACK, f"A night sky should be black, not {night.screen.bg}."
    assert day.screen.bg == SKY_BLUE, f"A day sky should be sky blue, not {day.screen.bg}."
    assert len(stars_drawn(day, WHITE)) == 5, "In the day, the 5 stars should be pale (white)."
    # The sun has 12 rays; the moon has none.
    rays = [line for line in day.lines if round(line.length) == 80]
    assert len(rays) == 12, f"The sun should have 12 rays, found {len(rays)}."
    assert not [line for line in night.lines if round(line.length) == 80], "The night sky should not have sun rays."


def test_four_houses_are_drawn_in_a_row():
    result = run_script(PROGRAM, inputs=["5", "night"], seed=6)
    wall_fills = [f for f in result.turtle.fills if f.color in HOUSE_COLORS
                  and len(f.points) == 5 and round(abs(f.points[1][0] - f.points[0][0])) == 100]
    assert len(wall_fills) == 4, f"There should be 4 houses with 100-wide walls, found {len(wall_fills)}."
    bottoms = {f.points[0][1] for f in wall_fills}
    assert bottoms == {-140}, "All houses should stand on the grass at the same height (y = -140)."


def test_house_function_draws_walls_roof_door_and_windows():
    module = load_module(PROGRAM, inputs=["0", "night"], seed=7)
    pen = module.t
    before = len(pen.fills)
    module.house(0, 0, "#009E73")
    new_fills = pen.fills[before:]
    assert len(new_fills) == 5, f"house() should fill 5 shapes (walls, roof, door, 2 windows), not {len(new_fills)}."
    assert new_fills[0].color == "#009E73", "The walls should use the color given to house()."


def test_strange_answers_do_not_crash_the_program():
    result = run_script(PROGRAM, inputs=["lots", "sunset"], seed=8)
    assert len(stars_drawn(result, YELLOW)) == 30, "If the answer is not a number, 30 stars should be drawn."
    assert result.screen.bg == BLACK, "If the answer is not day or night, a night sky should be drawn."
    big = run_script(PROGRAM, inputs=["5000", "night"], seed=8)
    assert len(stars_drawn(big, YELLOW)) == 200, "Very big numbers should be limited to 200 stars."
