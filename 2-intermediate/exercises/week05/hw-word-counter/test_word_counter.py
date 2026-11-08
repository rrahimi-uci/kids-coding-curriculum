"""Checks for Homework 5 - Word Counter."""


def test_counts_repeated_words(load_target):
    m = load_target()
    counts = m.count_words("slime slime dragon")
    assert counts.get("slime") == 2, f"'slime slime dragon' has slime 2 times, but your count is {counts.get('slime')}. (TODO 1)"
    assert counts.get("dragon") == 1, "'dragon' appears once."


def test_capital_letters_count_as_the_same_word(load_target):
    m = load_target()
    counts = m.count_words("The cat saw the hat")
    assert counts.get("the") == 2, "'The' and 'the' are the same word, so 'the' should be 2."


def test_most_common(load_target):
    m = load_target()
    answer = m.most_common({"slime": 2, "the": 3, "dragon": 1})
    assert answer == "the", f"'the' has the biggest count (3), but most_common returned {answer!r}. (TODO 2)"
