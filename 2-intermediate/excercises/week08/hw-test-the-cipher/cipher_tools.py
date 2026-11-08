"""encode() makes a Caesar-cipher secret message (like week 5).

Each small letter moves `shift` places along the alphabet. After z it
wraps round to a again. Spaces and other symbols stay exactly the same.

    encode("abc", 1)       gives "bcd"
    encode("xyz", 3)       gives "abc"        (wraps round after z)
    encode("hi there!", 1) gives "ij uifsf!"  (space and ! stay the same)

This file is correct. Do not change it: write tests for it in starter.py.
"""

ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def encode(message, shift):
    """Return the secret version of a message written in small letters."""
    secret = ""
    for letter in message:
        if letter in ALPHABET:
            position = ALPHABET.index(letter)
            secret = secret + ALPHABET[(position + shift) % 26]
        else:
            secret = secret + letter
    return secret
