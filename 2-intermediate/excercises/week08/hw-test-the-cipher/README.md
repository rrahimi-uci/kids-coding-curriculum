# Homework 8 - Test the Cipher

**Goal:** write tests for the Caesar cipher from week 5, so nobody can break
it without you noticing.

1. Read `cipher_tools.py`. It is correct: do not change it.
2. Open `starter.py` (YOUR test file) and press **Run**. pytest shows one line
   per test with `PASSED` or `FAILED`.
3. **TODO 1** test that letters wrap round after z. Use your paper cipher
   wheel to work out the expected answer.
4. **TODO 2** test that spaces and symbols like `!` stay the same.
5. **TODO 3** write one more test of your own.
6. Press **Run**: every test should say `PASSED`.

**Done looks like:** at least 3 tests, all `PASSED`.

**Check your work:** open `check_my_work.py` and press **Run**. It tries your
tests on three BROKEN ciphers. Good tests catch every one of them.

**Remember:** if a test fails on the correct `encode()`, the TEST is wrong.
Check your expected answer with the wheel.
