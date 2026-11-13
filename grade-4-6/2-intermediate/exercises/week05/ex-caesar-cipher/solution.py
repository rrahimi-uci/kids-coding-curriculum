# TEACHER REFERENCE SOLUTION: Caesar Cipher (Exercise 5.2)
#
# What the program does: it turns a message into a secret code by moving every
# letter a number of places along the alphabet (with a shift of 3, "a" becomes
# "d"), and it can turn the secret message back into the original.
# Key ideas practiced: a dictionary used as a lookup table (the paper cipher
# wheel), looping over the letters of a string, and "in" to test for a key.
# Approach: make_key() was given; it builds the wheel, and "% 26" makes the
# alphabet wrap around so "z" shifts back to "a". encode() looks up every letter
# in the wheel and leaves anything that is not a letter alone. decode() reuses
# encode() with a negative shift, which walks the wheel the other way.

ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def make_key(shift):
    """Return a dictionary: each letter -> the letter shift places later."""
    key = {}
    for i in range(len(ALPHABET)):
        # % 26 is the remainder after dividing by 26. It wraps the count around:
        # position 26 becomes 0 again, so "z" followed by one more step is "a".
        key[ALPHABET[i]] = ALPHABET[(i + shift) % 26]
    return key


def encode(message, shift):
    """Return the secret version of the message. Spaces and other symbols stay the same."""
    key = make_key(shift)
    secret = ""
    # .lower() because the wheel only has small letters, so "Hi" is treated as "hi".
    for letter in message.lower():
        if letter in key:                    # "in" on a dictionary checks the keys
            secret = secret + key[letter]    # swap the letter using the wheel
        else:
            secret = secret + letter         # spaces, ! and ? are copied unchanged
    return secret


def decode(secret, shift):
    """Return the original message: shifting back is the same as shifting by -shift."""
    # Decoding is encoding backwards. A negative shift works because % 26 also
    # wraps around correctly for negative numbers in Python.
    return encode(secret, -shift)


if __name__ == "__main__":
    print(make_key(3))
    choice = input("Type e to encode or d to decode: ").lower()
    message = input("Message: ")
    shift = int(input("Shift (1 to 25): "))
    if choice == "d":
        print(f"Decoded: {decode(message, shift)}")
    else:
        print(f"Secret: {encode(message, shift)}")


# Common mistakes children make here:
# - Writing secret = key[letter] instead of secret = secret + key[letter], so the
#   result only holds the last letter.
# - Looking up every character with key[letter], which crashes with KeyError on a
#   space or "!". Check "if letter in key" first.
# - Decoding with the same shift (encode(secret, shift)), which scrambles the
#   message further instead of undoing it.
# - Forgetting that the dictionary only has small letters, so capital letters
#   (without .lower()) are not found and are left as they are.
#
# Another correct way: decode by flipping the dictionary, using the original shift.
#   key = make_key(shift)
#   back = {}
#   for plain, secret_letter in key.items():
#       back[secret_letter] = plain
