# Exercise 5.2 - Caesar Cipher

**Goal:** encode and decode secret messages with a dictionary, just like
the paper cipher wheel.

With a shift of 3, every letter moves 3 places along the alphabet:

```
plain:  a b c d e ... w x y z
secret: d e f g h ... z a b c
```

At the end the alphabet wraps around, like a clock. The starter does this
with `% 26`. The `%` sign gives the **remainder**: what is left over after
sharing out. 28 cookies shared by 26 friends: each gets 1, and 2 are left,
so `28 % 26` is 2. (Here `%` does not mean percent.)

1. Open `starter.py` and press **Run**. Look at the dictionary it prints:
   `'a': 'd', 'b': 'e', ...`
2. **TODO 1:** finish `encode()`. Look up each letter in the key.
   Letters that are not in the key (spaces, `!`) stay the same.
3. **TODO 2:** finish `decode()`. Hint: shifting by `-shift` (minus shift)
   goes backwards. Going back 3 letters is the same as going forward 23,
   because 3 + 23 = 26 is one whole turn of the wheel.
4. Test it: encode a message with your partner's shift, swap computers and
   decode each other's message.

**Done looks like:** `hi there!` with shift 3 becomes `kl wkhuh!`, and
decoding `kl wkhuh!` with shift 3 gives back `hi there!`.

**Check your work:** open `check_my_work.py` and press **Run**.

**Extra:** crack this message without knowing the shift. Try every shift
from 1 to 25 with a loop: `brx fudfnhg lw`
