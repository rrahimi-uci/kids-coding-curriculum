"""Checks for Exercise 1.2 - Commit Coach."""


def test_helpful_messages_are_good(load_target):
    coach = load_target()
    for message in ["Add jump to hero", "Fix score going below zero", "Draw the first level"]:
        assert coach.is_good_message(message), f"{message!r} is a helpful message, but is_good_message said False."


def test_empty_or_boring_messages_are_not_good(load_target):
    coach = load_target()
    for message in ["", "   ", "stuff", "Update", "fix", "asdf", "hero"]:
        assert not coach.is_good_message(message), (
            f"{message!r} does not say what changed, so is_good_message should return False."
        )


def test_too_long_message_is_not_good(load_target):
    coach = load_target()
    long_message = "Add a really really really long and detailed list of everything I did today"
    assert not coach.is_good_message(long_message), (
        f"That message has {len(long_message)} characters. More than 50 should return False."
    )


def test_make_message_builds_a_sentence(load_target):
    coach = load_target()
    result = coach.make_message("add", "star shape")
    assert result == "Add star shape", f"make_message('add', 'star shape') should give 'Add star shape', not {result!r}."


def test_find_secrets_spots_secret_lines(load_target):
    coach = load_target()
    lines = ["speed = 5", "password = 'dragon123'", "API_KEY = 'abc'", "name = 'Captain Nova'"]
    found = coach.find_secrets(lines)
    assert found == ["password = 'dragon123'", "API_KEY = 'abc'"], (
        f"find_secrets should return the 2 secret lines (in order), but returned {found!r}. "
        "Hint: compare with line.lower() so API_KEY is found too."
    )
