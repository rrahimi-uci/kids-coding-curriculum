# Homework 1 – Walk and Talk

**Goal:** make a sprite walk across the stage and talk, in the right order.
**Time:** about 10 minutes. **Tool:** Scratch app (offline).

## Build steps

1. Open the Scratch app. If an old project is open, click **File > New**.
   Click **Choose a Backdrop** (bottom right) and pick any place.
2. Build the script below for the cat (or any sprite). **glide** is in **Motion**.
3. Click the green flag and watch.
4. Save: **File > Save to your computer**, name `walk-and-talk`.

## The script in words

A number with a minus sign is a **negative number**. On the stage it means
"the other way": x: -180 is 180 steps **left** of the middle, and y: -100 is
100 steps **below** the middle. To type it, press the minus key, then the number.

- when green flag clicked
- go to x: -180 y: -100
- say "Hi! I am Pixel Panda" for 2 seconds (use your own nickname)
- glide 2 secs to x: 0 y: -100
- say "Look at this place!" for 2 seconds
- glide 2 secs to x: 180 y: -100
- say "Bye!" for 2 seconds

**Creative extra:** add **switch backdrop to ...** (in **Looks**) between the
glides so your sprite walks into a new place each time.

## Expected behavior

When you click the green flag, the sprite starts on the left, says hello,
glides to the middle, talks, glides to the right and says "Bye!". It starts
on the left again every time you click the flag.

## Checklist

- [ ] My script starts with **when green flag clicked**.
- [ ] My sprite always starts on the left.
- [ ] The steps happen in the same order as the script: talk, glide, talk, glide, bye.
- [ ] I used my nickname, not my real name.
- [ ] I saved my project.
