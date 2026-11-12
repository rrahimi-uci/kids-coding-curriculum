# Exercise 6.3 – The Mixed-Up Ballerina (bug hunt)

**Goal:** find two bugs in Kai's project and fix them.
**Tool:** Scratch app. **Work with a partner:** Driver and Helper.

Kai's plan: click the Ballerina and she says hi. Press space and she dances.

## Build steps

1. Click **Choose a Sprite** (the cat-face button under the stage). Pick **Ballerina**.
2. Click the **cat** in the sprite list. Build the cat's script below.
3. Click the **Ballerina** in the sprite list. Build her script below.
4. Test: click the Ballerina. Press space. What happens?
5. Find the two bugs. Fix them. Test again.

## The script in words (with the bugs)

Cat's code:

- when this sprite clicked (yellow Events)
- say Hi! for 2 seconds (purple Looks)

Ballerina's code:

- when a key pressed (yellow Events, pick **a**)
- repeat 4 (orange Control)
  - next costume (purple Looks)
  - wait 1 seconds (orange Control)

## Expected behavior

With the bugs, clicking the Ballerina does nothing, and space does nothing.
After the fixes, click the Ballerina and she says "Hi!". Press space and she dances.

## Checklist

- [ ] I found the script in the wrong sprite and moved it.
- [ ] I found the wrong key and fixed it.
- [ ] Click and space both work now.
