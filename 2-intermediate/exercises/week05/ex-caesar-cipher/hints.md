## Hint 1: Where to look
Run the file and look at the dictionary it prints. Each letter is a key, and its secret letter is the value. Your job is to look up every letter of the message in that dictionary.

## Hint 2: Try this
Use a `for` loop to walk through the message one letter at a time. Check `if letter in key:` before you look it up, so spaces and `!` do not cause a KeyError. For `decode()`, think about which shift goes the other way.

## Hint 3: Almost there
Use this shape: `for letter in message.lower():` then `if letter in key:` add `key[____]` to `secret`, `else:` add `____`. For `decode()`, you can call `encode()` with a different shift: `return encode(secret, ____)`.
