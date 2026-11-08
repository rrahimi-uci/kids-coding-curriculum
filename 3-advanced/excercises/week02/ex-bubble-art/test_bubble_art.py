"""Checks for Exercise 2.2 - Bubble Art."""


def test_bubble_remembers_its_attributes(load_target):
    art = load_target()
    b = art.Bubble(10, 20, 30, "#56B4E9")
    assert (b.x, b.y) == (10, 20), "A Bubble should remember its x and y."
    assert getattr(b, "size", None) == 30, "A Bubble should remember its size in self.size."
    assert getattr(b, "colour", None) == "#56B4E9", "A Bubble should remember its colour in self.colour."


def test_grow_and_move(load_target):
    art = load_target()
    b = art.Bubble(0, 0, 30, "#E69F00")
    b.grow(5)
    b.move(4, -2)
    assert b.size == 35, f"grow(5) should change size 30 into 35, not {b.size}."
    assert (b.x, b.y) == (4, -2), f"move(4, -2) should put the bubble at (4, -2), not ({b.x}, {b.y})."


def test_draw_paints_a_big_dot(load_target):
    art = load_target()
    t = art.turtle.Turtle()
    art.Bubble(50, 60, 40, "#009E73").draw(t)
    big = [d for d in t.dots if d.pos == (50, 60)]
    assert big, "draw() should paint a dot exactly at the bubble's (x, y)."
    assert big[0].size == 40 and big[0].color == "#009E73", (
        "The dot at (x, y) should use the bubble's own size and colour."
    )


def test_make_bubbles(load_target):
    art = load_target(seed=3)
    bubbles = art.make_bubbles(12)
    assert len(bubbles) == 12, f"make_bubbles(12) should return 12 bubbles, not {len(bubbles)}."
    assert all(isinstance(b, art.Bubble) for b in bubbles), "Every item in the list should be a Bubble object."
    assert all(b.colour in art.PALETTE for b in bubbles), "Use colours from PALETTE."
    assert len({(b.x, b.y) for b in bubbles}) > 1, "Bubbles should be in random (different) places."
