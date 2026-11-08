"""Checks for Exercise 4.2 - Guess-the-Number Bot."""


def test_check_answers(load_target):
    bot = load_target()
    assert bot.check(50, 73) == "higher", "The secret 73 is HIGHER than the guess 50."
    assert bot.check(80, 73) == "lower", "The secret 73 is LOWER than the guess 80."
    assert bot.check(73, 73) == "correct", "Guess 73 with secret 73 is correct."


def test_next_guess_is_in_the_middle(load_target):
    bot = load_target()
    for low, high in [(1, 100), (51, 100), (1, 49), (10, 11)]:
        guess = bot.next_guess(low, high)
        middle = (low + high) / 2
        assert low <= guess <= high and abs(guess - middle) <= 1, (
            f"For the range {low}..{high} the smart guess is the middle (about {middle}), not {guess}."
        )


def test_bot_finds_every_number(load_target):
    bot = load_target()
    for secret in range(1, 101):
        guesses = bot.bot_play(secret)
        assert guesses and guesses[-1] == secret, f"The bot should end on the secret {secret}. Its guesses: {guesses}"


def test_bot_never_needs_more_than_7_guesses(load_target):
    bot = load_target()
    worst = max(len(bot.bot_play(secret)) for secret in range(1, 101))
    assert worst <= 7, f"Halving 1..100 needs at most 7 guesses, but your bot once needed {worst}."


def test_play_with_human(load_target, inputs):
    bot = load_target()
    with inputs(["h", "l", "c"]):  # think of a number between 51 and 74
        tries = bot.play_with_human()
    assert tries == 3, f"After the answers h, l, c the bot should report 3 tries, not {tries}."
