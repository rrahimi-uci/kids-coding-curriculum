"""Checks for Exercise 10.2 - Random Bubble Art."""


def bubbles(run_target, seed=1):
    """Each filled shape is one bubble: (start point, height, color)."""
    found = []
    for t in run_target(seed=seed).turtles:
        for fill in t.fills:
            ys = [p[1] for p in fill.points]
            found.append((fill.points[0], round(max(ys) - min(ys)), str(fill.color).upper()))
    return found


def test_draws_lots_of_bubbles(run_target):
    n = len(bubbles(run_target))
    assert n >= 20, f"I counted {n} bubbles. Keep the loop that draws 30."


def test_bubbles_are_all_over_the_screen(run_target):
    places = {start for start, _, _ in bubbles(run_target)}
    assert len(places) >= 10, (
        "The bubbles are all in the same place. Use random.randint(...) for x and y."
    )


def test_bubbles_have_different_sizes(run_target):
    sizes = {size for _, size, _ in bubbles(run_target)}
    assert len(sizes) >= 3, "All bubbles are the same size. Use random.randint(10, 50) for size."


def test_bubbles_use_many_palette_colors(run_target):
    colors = {color for _, _, color in bubbles(run_target)}
    assert len(colors) >= 4, f"Only {len(colors)} color(s) used. Try color = random.choice(PALETTE)."


def test_new_picture_every_run(run_target):
    first = [start for start, _, _ in bubbles(run_target, seed=1)]
    second = [start for start, _, _ in bubbles(run_target, seed=2)]
    assert first != second, "Two runs drew exactly the same picture. Use random to make surprises!"
