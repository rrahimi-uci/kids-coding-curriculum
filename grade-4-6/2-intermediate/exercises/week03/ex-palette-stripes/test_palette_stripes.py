"""Checks for Exercise 3.1 - Palette Stripes."""

OKABE_ITO = {"#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7", "#000000"}


def test_palette_has_at_least_five_colors(load_target):
    palette = load_target().build_palette()
    assert len(palette) >= 5, f"Your palette has {len(palette)} colors. Append more to reach 5 (TODO 1)."


def test_palette_uses_color_blind_safe_colors(load_target):
    palette = load_target().build_palette()
    odd = [c for c in palette if c.upper() not in OKABE_ITO]
    assert not odd, f"Use colors from the Okabe-Ito list in the README. These are not: {odd}"


def test_one_stripe_per_color_in_order(load_target):
    m = load_target()
    t = m.turtle.Turtle()
    colors = ["#E69F00", "#56B4E9", "#009E73"]
    m.draw_stripes(t, colors)
    drawn = [f.color for f in t.fills]
    assert drawn == colors, f"draw_stripes with 3 colors should draw 3 stripes in order. It drew: {drawn}"


def test_stripes_are_labeled_with_index_numbers(load_target):
    m = load_target()
    t = m.turtle.Turtle()
    m.draw_stripes(t, ["#E69F00", "#56B4E9", "#009E73", "#0072B2"])
    labels = [text.text for text in t.texts]
    assert labels == ["0", "1", "2", "3"], f"Label the stripes 0, 1, 2, 3 (their index numbers). Yours: {labels}"
