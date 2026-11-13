"""Checks for Exercise 9.2 - Fair or biased?"""


def test_label_counts(load_target):
    program = load_target()
    got = program.label_counts(program.ALL_CARDS)
    assert got == {"friendly": 8, "grumpy": 8}, f"ALL_CARDS has 8 friendly and 8 grumpy cards, you counted {got}."
    got = program.label_counts(program.BIASED_TRAINING)
    assert got.get("friendly") == 1, "The biased pile has only 1 friendly card."


def test_split_keeps_test_cards_secret(load_target):
    program = load_target()
    train, test = program.split(program.ALL_CARDS)
    assert len(train) == 12 and len(test) == 4, f"16 cards should split into 12 training + 4 test, not {len(train)} + {len(test)}."
    assert not set(train) & set(test), "A card must never be in BOTH piles - that would be cheating!"


def test_accuracy_of_fair_training(load_target):
    program = load_target()
    train, test = program.split(program.ALL_CARDS)
    got = program.accuracy(train, test)
    assert got == 1.0, f"With fair training the sorter gets all 4 test cards right (accuracy 1.0). Yours says {got}."
    assert program.accuracy(train, [(9, 9, "friendly")]) == 0.0, \
        "A test card the sorter gets wrong should give accuracy 0.0."


def test_biased_training_is_worse(load_target):
    program = load_target()
    train, test = program.split(program.ALL_CARDS)
    fair = program.accuracy(train, test)
    biased = program.accuracy(program.BIASED_TRAINING, test)
    assert biased < fair, f"Biased training should give worse accuracy than fair training (biased {biased}, fair {fair})."
