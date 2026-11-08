# Caesar Cipher - reference solution
# make_key() builds a dictionary that says which letter becomes which,
# like the paper cipher wheel. % 26 wraps round: after z comes a again.

ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def make_key(shift):
    """Return a dictionary: each letter -> the letter shift places later."""
    key = {}
    for i in range(len(ALPHABET)):
        key[ALPHABET[i]] = ALPHABET[(i + shift) % 26]
    return key


def encode(message, shift):
    """Return the secret version of the message. Spaces and other symbols stay the same."""
    key = make_key(shift)
    secret = ""
    for letter in message.lower():
        if letter in key:
            secret = secret + key[letter]
        else:
            secret = secret + letter
    return secret


def decode(secret, shift):
    """Return the original message: shifting back is the same as shifting by -shift."""
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
