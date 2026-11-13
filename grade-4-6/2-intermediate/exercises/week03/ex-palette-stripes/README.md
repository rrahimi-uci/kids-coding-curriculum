# Exercise 3.1 - Palette Stripes

**Goal:** build a list of colors and draw one labeled stripe for each.

The color-blind-safe (Okabe-Ito) colors:

| name | code |
|---|---|
| orange | `#E69F00` |
| sky blue | `#56B4E9` |
| bluish green | `#009E73` |
| yellow | `#F0E442` |
| blue | `#0072B2` |
| vermillion | `#D55E00` |
| reddish purple | `#CC79A7` |
| black | `#000000` |

1. Open `starter.py` and press **Run**: only one stripe appears.
2. **TODO 1:** use `palette.append(...)` to add blue and vermillion.
3. **TODO 3:** loop over the list with `for i in range(len(colors)):` and
   draw stripe `i` with label `str(i)`. Move `x` along by `width` each time.
   (A label must be text. `str()` turns a number into text: `str(3)` gives `"3"`.)
4. **TODO 4:** print `palette[0]` and `palette[-1]`. A minus sign means
   "count from the end", so `-1` is the last color.

**Done looks like:** a row of 5 or more stripes, labeled 0, 1, 2, 3, 4 ...
Notice: the first stripe is number **0**!

**Check your work:** open `check_my_work.py` and press **Run**.

**Extra:** make the stripes thinner and use `palette * 2` to draw the
pattern twice.
