# Exercise 7.3 - Dot Art from a File

**Goal:** draw a picture whose dots are stored in a file, not in the code.

Open `my_art.txt` in Thonny (**File > Open**). Each line is one dot:

```text
x,y,size,color
-150,-60,40,#009E73
```

The middle of the turtle window is `(0, 0)`. A minus sign means "the other
side of the middle": `x = -150` is 150 steps LEFT, and `y = -60` is 60 steps
DOWN. The window goes from about -300 to 300 both ways.

1. Open `starter.py` and press **Run**. The window is empty: the program
   cannot read the file yet.
2. **TODO 1** `parse_line()`: turn the text pieces into numbers with `int()`.
3. **TODO 2** `load_dots()`: read every line that is not empty and add the dot
   to the list. Press **Run**: a caterpillar under a sun should appear!
4. **TODO 3** `save_dots()`: write every dot back into a file, one per line.
   Use `"w"`: saving a design should replace the old one.
5. Change `my_art.txt`: move a dot, change a color, add a line. Save the
   file and press **Run** in `starter.py` again. (To open `my_art.txt` in
   Thonny, choose "all files" in the file-type menu of the Open window.)

**Done looks like:** the picture appears (a green caterpillar with an orange
head, a yellow sun and sky-blue clouds), the text at the bottom says
`16 dots loaded from my_art.txt`, and changing the text file changes the
picture.

**Check your work:** open `check_my_work.py` and press **Run**.

**Colors:** use the color-blind-safe palette: `#E69F00` orange,
`#56B4E9` sky blue, `#009E73` green, `#F0E442` yellow, `#0072B2` blue,
`#D55E00` vermillion, `#CC79A7` purple, `#000000` black.

**Extra:** in the main part, make a mirror copy: for every dot, make a new dot
with `-x` instead of `x`, then `save_dots("mirror_art.txt", mirrored)`.
