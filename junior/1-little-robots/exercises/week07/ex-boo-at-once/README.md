# Exercise 7.2 – Boo at Once (bug hunt)

**Goal:** make the Ghost wait for its turn.
**Tool:** Scratch app. **Work with a partner:** one sprite each.

Omar's joke: the cat asks "Who is there?". Then the Ghost says "Boo!".

## Build steps

1. Click **File**, then **New**. Keep the cat.
2. Click **Choose a Sprite** (the cat-face button under the stage). Pick **Ghost**. Drag it to its own spot.
3. Click the **cat** in the sprite list. Build the cat's script below.
4. Click the **Ghost** in the sprite list. Build the Ghost's script below.
5. Click the green flag. What goes wrong?
6. Find the bug. Fix it. Test again.

## The script in words (with the bug)

Cat:

- when green flag clicked (yellow Events)
- say Who is there? for 2 seconds (purple Looks)

Ghost:

- when green flag clicked (yellow Events)
- say Boo! for 2 seconds (purple Looks)

## Expected behavior

With the bug, both talk at the same time, and the joke is spoiled.
After the fix, the cat asks first. Then the Ghost says "Boo!".

## Checklist

- [ ] I found which sprite should talk second.
- [ ] I added a block from orange Control to fix it.
- [ ] Now the cat talks first, then the Ghost.
