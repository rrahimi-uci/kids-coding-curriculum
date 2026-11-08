# Exercise 3.1 - Enemy Family

**Goal:** make three kinds of enemy that share one parent class, `Enemy`,
but each moves in its own way.

| Class | How it moves |
|---|---|
| `Enemy` (parent) | 1 step right |
| `Guard` | stays still (done for you) |
| `Zigzagger` | 1 step right, then up, down, up, down... |
| `Sprinter` | `speed` steps right |

1. Open `starter.py` in Thonny. Read `Enemy` and `Guard` first.
2. Finish the `TODO`s in `Zigzagger`, `Sprinter` and `move_all`.
3. Press **Run**. You should see:

```
Turn 1: Blob at (1, 0) | Rocky at (0, 0) | Zig at (1, 1) | Zoom at (2, 0)
Turn 2: Blob at (2, 0) | Rocky at (0, 0) | Zig at (2, 0) | Zoom at (4, 0)
```

**Check your work:** open `check_my_work.py` and press **Run**.

**Extra:** invent a `Teleporter(Enemy)` that jumps to a random `x`
between 0 and 10 each turn (use `import random`).

**Tip:** if Run shows `AttributeError: 'Sprinter' object has no attribute
'name'`, that is the clue for TODO 2: the parent's `__init__` never ran.
