# Exercise 5.2 – Bug-Hunt Relay (bug hunt)

**Goal:** fix three broken projects.
**Tool:** Scratch app. **Work with a partner:** swap Driver after each leg.

## Build steps

1. Click **File**, then **Load from your computer**. Open the leg your grown-up saved, or build it from your book.
2. **Test:** click the green flag.
3. **Look:** what should it do? What did it do?
4. **Change one thing.** Then test again.
5. Swap Driver!

## The script in words (with the bugs)

**Leg 1: The Window.** It should draw four squares.

- when green flag clicked (yellow Events), erase all, pen down (green Pen)
- repeat 4 (orange Control)
  - repeat 4
    - move 60 steps, turn right 90 degrees, turn right 90 degrees (blue Motion)

**Leg 2: The Magic Trick.** It should say "Watch this!", then vanish.

- when green flag clicked, show, say Watch this! for 2 seconds (purple Looks)
- when green flag clicked, hide

**Leg 3: The Stuck Counter.** The Apple sprite. It should count every click.

- when this sprite clicked (yellow Events)
- set apples to 0, change apples by 1 (orange-red Variables)

## Expected behavior

After each fix, each leg does what it should.

## Checklist

- [ ] Leg 1: I see four squares, like a window.
- [ ] Leg 2: the cat says "Watch this!", then vanishes.
- [ ] Leg 3: every click adds 1.
