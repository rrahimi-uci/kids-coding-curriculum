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
   Try it by hand first: `sum_to(3)` is `3 + sum_to(2)`, which is
   `3 + 2 + sum_to(1)`, which is `3 + 2 + 1 + sum_to(0)`. And `sum_to(0)` is
   the base case: it gives `0`. So `sum_to(3)` is 6.
3. Finish `reverse(word)` so `reverse("turtle")` gives `"eltrut"`.
   Two Python helpers: `word[-1]` is the **last** letter (the `-1` means
   "count 1 from the end"), and `word[:-1]` is **everything except** the last
   letter. For `"cat"`: `word[-1]` is `"t"` and `word[:-1]` is `"ca"`.
   So the reverse of `"cat"` is `"t"` + the reverse of `"ca"`.

**Done looks like:** the Shell shows

```
5
4
3
2
1
Liftoff!
sum_to(10) = 55
reverse('recursion') = noisrucer
```

**Check your work:** open `check_my_work.py` and press **Run**.

**Extra:** use Thonny's debugger (the bug button, then **Step into**, F7) on
`sum_to(3)` and watch the stack of calls grow and shrink.
