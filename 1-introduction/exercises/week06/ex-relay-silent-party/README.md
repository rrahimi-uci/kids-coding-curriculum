# Exercise 6.3 – Relay C: The Silent Party (bug hunt)

**Goal:** build a broken party show exactly as shown, then find and fix its **two** bugs.
**Tool:** Scratch app (offline). **Work as a relay team.**

## What it should do

After the green flag, the Ghost hides. When you press **space**, the cat says
"Party time!", then the Ghost appears, does a slow spinning dance you can
really watch (one full turn, about 2 seconds) and says "Woo!".

## Build steps

1. Start a new project. Keep the cat. Add the **Ghost** sprite.
2. Make two messages: in a **broadcast** block, click the dropdown, choose
   **New message**, type `party`. Make another called `dance`.
3. Build the scripts below **exactly** as written, bugs and all.
4. Click the green flag, then press **space**. Compare with "What it should do".
5. Use the four detective steps. Fix one thing at a time and test after each change.
6. Write both bugs and fixes on your relay baton (workbook, Exercise 6.3).

## The scripts in words (with two bugs)

**Cat**:

- when space key pressed
- say "Party time!" for 2 seconds
- broadcast party

**Ghost**, two scripts:

1. when green flag clicked
   - hide
2. when I receive dance
   - show
   - repeat 10:
     - turn right 36 degrees
     - next costume
   - say "Woo!" for 2 seconds

## Expected behavior

After your fixes: the Ghost is hidden after the green flag. Pressing space
makes the cat say "Party time!"; then the Ghost appears, spins once slowly
(about 2 seconds) while changing costume, and says "Woo!".

## Checklist

- [ ] I built the show exactly as shown and watched what went wrong.
- [ ] I found bug 1 and wrote it on my relay baton.
- [ ] I found bug 2 and wrote it on my relay baton.
- [ ] After my fixes, the Ghost appears and I can watch the whole dance.
