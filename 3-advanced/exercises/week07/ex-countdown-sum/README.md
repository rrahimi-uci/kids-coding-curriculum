# Exercise 7.1 - Recursion warm-up

**Goal:** write functions that call *themselves* on a smaller problem.

Every recursive function needs:

1. a **base case** - the tiny problem you can answer straight away (stop!),
2. a **recursive case** - do one small step, then call yourself on the rest.

**Steps**

1. Open `starter.py` in Thonny and press **Run**. Read `countdown()`: it
   prints a number, then asks *itself* to count down from one less.
2. Finish `sum_to(n)` so `sum_to(5)` gives `5 + 4 + 3 + 2 + 1 = 15`.
   Use recursion: `n + sum_to(n - 1)`.
3. Finish `reverse(word)` so `reverse("turtle")` gives `"eltrut"`.

**Done looks like:** `sum_to(10) = 55` and `reverse('recursion') = noisrucer`.

**Check your work:** open `check_my_work.py` and press **Run**.

**Extra:** use Thonny's debugger (the bug button, then **Step into**, F7) on
`sum_to(3)` and watch the stack of calls grow and shrink.
