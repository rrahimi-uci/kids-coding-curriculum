"""Checks for Exercise 4.2 - Pixel Art."""

SMALL = ["K.K",
         ".O."]


def test_count_pixels(load_target):
    m = load_target()
    assert m.count_pixels(SMALL, "K") == 2, "The small grid ['K.K', '.O.'] has 2 K pixels."
    assert m.count_pixels(["GG", "GG", "G."], "G") == 5, "['GG', 'GG', 'G.'] has 5 G pixels in 3 rows. Visit every row."


def test_draws_every_row(load_target):
    m = load_target()
    t = m.turtle.Turtle()
    m.draw_grid(t, SMALL, 10)
    assert len(t.fills) == 3, f"['K.K', '.O.'] has 3 coloured pixels, but {len(t.fills)} squares were drawn. Draw every row!"


def test_second_row_is_lower(load_target):
    m = load_target()
    t = m.turtle.Turtle()
    m.draw_grid(t, SMALL, 10)
    ys = [f.points[0][1] for f in t.fills]
    assert len(ys) == 3 and ys[2] < ys[0], "The second row should be drawn BELOW the first row: y = y - size."


def test_colours_match_letters(load_target):
    m = load_target()
    t = m.turtle.Turtle()
    m.draw_grid(t, SMALL, 10)
    colours = [f.color for f in t.fills]
    assert colours == ["#000000", "#000000", "#E69F00"], f"K should be black and O orange. Got {colours}."
