# Exercise 3.2 - Adventure Inventory

**Goal:** use a list as a backpack: `append`, index numbers, `len` and
`for item in backpack`.

1. Open `starter.py` and press **Run**. Read the red error from the bottom
   up: `IndexError: list index out of range`. Which line? (**TODO 3**)
2. **TODO 1:** `add_item()` should `append` the item.
3. **TODO 2:** `has_item()` loops over the backpack looking for the item.
4. **TODO 3:** fix `last_item()`. Draw the boxes on paper if it helps:

```
index:   0        1       2      3
       torch    rope    map    apple      len = 4
```

**Done looks like:**

```
- torch
- rope
- map
- apple
4 items in total.
First in: torch. Last in: apple.
You unfold the map. The treasure is to the north!
You still need a key for the chest.
```

**Check your work:** open `check_my_work.py` and press **Run**.

**Extra:** write `drop_item(backpack, item)` using `backpack.remove(item)`.
What happens if the item is not there? How could `has_item` help?
