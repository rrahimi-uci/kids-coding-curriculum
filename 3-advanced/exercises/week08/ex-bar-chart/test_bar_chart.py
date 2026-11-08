"""Checks for Exercise 8.3 - Bar chart."""

COUNTS = {"Puzzle": 2, "Racing": 6, "Pets": 3}


def bar_heights(t):
    return [max(p[1] for p in f.points) - min(p[1] for p in f.points) for f in t.fills]


def draw(program, counts=COUNTS):
    t = program.turtle.Turtle()
    program.draw_bar_chart(t, counts, "Test chart")
    return t


def test_one_bar_per_item(load_target):
    program = load_target()
    t = draw(program)
    assert len(t.fills) == 3, f"3 items should give 3 filled bars, but there are {len(t.fills)}."


def test_bars_match_their_numbers(load_target):
    program = load_target()
    heights = sorted(bar_heights(draw(program)))
    assert heights[0] < heights[1] < heights[2], \
        "Bars should have different heights: a bigger number needs a taller bar."
    ratio = heights[2] / heights[0]
    assert abs(ratio - 3) < 0.1, f"6 votes is 3 times 2 votes, so that bar should be 3 times as tall (yours: {ratio:.1f} times)."


def test_every_bar_has_a_name_label(load_target):
    program = load_target()
    words = {text.text for text in draw(program).texts}
    missing = [name for name in COUNTS if name not in words]
    assert not missing, f"Write each name under its bar so the chart does not rely on color. Missing: {missing}"


def test_every_bar_shows_its_number(load_target):
    program = load_target()
    words = {text.text for text in draw(program).texts}
    missing = [str(v) for v in COUNTS.values() if str(v) not in words]
    assert not missing, f"Write each number on top of its bar. Missing: {missing}"
