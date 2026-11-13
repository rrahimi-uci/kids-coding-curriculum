# Exercise 4.1 - Search Race

**Goal:** write binary search and race it against linear search by counting
steps (how many items each one looks at).

1. Open `starter.py` in Thonny. Read `linear_search` - it is done.
2. Finish `binary_search` using the steps in the `TODO`.
3. Press **Run**. You should see:

```
Searching for the LAST number in a sorted list:
   items |  linear |  binary
      10 |      10 |       4
     100 |     100 |       7
    1000 |    1000 |      10
   10000 |   10000 |      14
```

**Check your work:** open `check_my_work.py` and press **Run**.

**Extra:** add 100000 to the list of sizes. How many steps does each need?
Why does binary search only work on a SORTED list?
