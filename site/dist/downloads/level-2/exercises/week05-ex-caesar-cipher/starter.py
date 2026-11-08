# Caesar Cipher
# make_key() is done: it builds the cipher wheel as a dictionary.
# Run this file first and look at the dictionary it prints.

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
    # TODO 1: for letter in message.lower():
    #             if the letter is in the key, add key[letter] to secret
    #             otherwise add the letter itself (spaces, ! and ? stay the same)
    return secret


def decode(secret, shift):
    """Return the original message."""
    # TODO 2: decoding is encoding BACKWARDS. Which shift undoes a shift of 3?
    return secret


if __name__ == "__main__":
    print(make_key(3))
    choice = input("Type e to encode or d to decode: ").lower()
    message = input("Message: ")
    shift = int(input("Shift (1 to 25): "))
    if choice == "d":
        print(f"Decoded: {decode(message, shift)}")
    else:
        print(f"Secret: {encode(message, shift)}")
