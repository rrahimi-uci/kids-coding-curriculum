"""Checks for Exercise 5.2 - Caesar Cipher."""


def test_encode_shifts_letters(load_target):
    m = load_target()
    answer = m.encode("abc", 1)
    assert answer == "bcd", f"'abc' with shift 1 should become 'bcd', not {answer!r}. (TODO 1)"


def test_encode_wraps_round(load_target):
    m = load_target()
    answer = m.encode("xyz", 3)
    assert answer == "abc", f"'xyz' with shift 3 wraps round to 'abc', not {answer!r}."


def test_spaces_and_symbols_stay(load_target):
    m = load_target()
    answer = m.encode("hi there!", 3)
    assert answer == "kl wkhuh!", f"'hi there!' with shift 3 should be 'kl wkhuh!', not {answer!r}. Keep spaces and '!'."


def test_decode_undoes_encode(load_target):
    m = load_target()
    answer = m.decode("kl wkhuh!", 3)
    assert answer == "hi there!", f"Decoding 'kl wkhuh!' with shift 3 should give 'hi there!', not {answer!r}. (TODO 2)"
