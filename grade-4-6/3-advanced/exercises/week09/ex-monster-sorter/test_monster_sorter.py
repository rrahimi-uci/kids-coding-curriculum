"""Checks for Exercise 9.1 - Monster sorter (nearest neighbor)."""


# Steps distance (gap + gap) is what the README asks for. The ruler distance
# from the README's Extra (math.sqrt) is accepted too.
STEPS_OR_RULER = (7, 5)


def test_distance(load_target):
    program = load_target()
    got = program.distance((0, 0), (3, 4))
    assert got in STEPS_OR_RULER, \
        f"From (0, 0) to (3, 4) is 3 steps across + 4 steps up = 7 steps. Your distance gave {got}."
    got = program.distance((5, 2), (6, 1))
    assert round(got, 2) in (2, 1.41), \
        f"From (5, 2) to (6, 1) the gaps are 1 and 1, so the steps distance is 2. Your distance gave {got}."
    assert program.distance((2, 2), (2, 2)) == 0, "A card is 0 away from itself."
    got = program.distance((1, 5, "grumpy"), (4, 1))
    assert got in STEPS_OR_RULER, \
        f"distance should use only the first two numbers of a card: (1, 5) to (4, 1) is 3 + 4 = 7. Yours gave {got}."


def test_nearest_finds_the_closest_card(load_target):
    program = load_target()
    cards = [(0, 0, "a"), (5, 5, "b"), (9, 9, "c")]
    got = program.nearest(cards, (6, 4))
    assert got == (5, 5, "b"), f"The closest card to (6, 4) is (5, 5, 'b'), but you found {got}."


def test_classify_mystery_monsters(load_target):
    program = load_target()
    assert program.classify(program.TRAINING, (7, 2)) == "friendly", "A fluffy monster with few teeth (7, 2) should be friendly."
    assert program.classify(program.TRAINING, (3, 7)) == "grumpy", "A monster with lots of teeth (3, 7) should be grumpy."
