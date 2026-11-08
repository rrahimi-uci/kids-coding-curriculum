# Exercise 5.2 - Caesar Cipher

**Goal:** encode and decode secret messages with a dictionary, just like
the paper cipher wheel.

With a shift of 3, every letter moves 3 places along the alphabet:

```
plain:  a b c d e ... w x y z
secret: d e f g h ... z a b c
```

1. Open `starter.py` and press **Run**. Look at the dictionary it prints:
   `'a': 'd', 'b': 'e', ...`
2. **TODO 1:** finish `encode()`. Look up each letter in the key.
   Letters that are not in the key (spaces, `!`) stay the same.
3. **TODO 2:** finish `decode()`. Hint: shifting by `-shift` goes backwards.
4. Test it: encode a message with your partner's shift, swap computers and
   decode each other's message.

**Done looks like:** `hi there!` with shift 3 becomes `kl wkhuh!`, and
decoding `kl wkhuh!` with shift 3 gives back `hi there!`.

**Check your work:** open `check_my_work.py` and press **Run**.

**Extra:** crack this message without knowing the shift. Try every shift
from 1 to 25 with a loop: `brx fudfnhg lw`
