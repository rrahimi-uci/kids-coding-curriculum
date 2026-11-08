"""Checks for Exercise 9.1 - Monster sorter (nearest neighbor)."""


def test_distance(load_target):
    program = load_target()
    assert program.distance((0, 0), (3, 4)) == 5, "The distance from (0, 0) to (3, 4) is 5 (a 3-4-5 triangle)."
    assert program.distance((2, 2), (2, 2)) == 0, "A card is 0 away from itself."
    assert program.distance((1, 5, "grumpy"), (4, 1)) == 5, "distance should use only the first two numbers of a card."


def test_nearest_finds_the_closest_card(load_target):
    program = load_target()
    cards = [(0, 0, "a"), (5, 5, "b"), (9, 9, "c")]
    got = program.nearest(cards, (6, 4))
    assert got == (5, 5, "b"), f"The closest card to (6, 4) is (5, 5, 'b'), but you found {got}."


def test_classify_mystery_monsters(load_target):
    program = load_target()
    assert program.classify(program.TRAINING, (7, 2)) == "friendly", "A fluffy monster with few teeth (7, 2) should be friendly."
    assert program.classify(program.TRAINING, (3, 7)) == "grumpy", "A monster with lots of teeth (3, 7) should be grumpy."
