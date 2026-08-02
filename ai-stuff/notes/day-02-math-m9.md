# Math M9 — Gradient descent (training loop)

**Status:** In progress  
**Goal:** Understand the loop: predict → loss → slope → update weights → repeat.

## Q&A

### Q1 — What is gradient descent in plain words?
**Student answer:**
gradient descent is process to make loss smaller, it uses slope/gradient of the loss, updates weights in the opposite direction until loss gets smaller

**Teacher feedback:** 9.5/10 — all core pieces present. Typos: gradient descent. Add: repeat many steps with learning rate.

### Q2 — Compute one weight update
**Student answer (1):** new_w = 6 → wrong (skipped lr multiply). Correct was 8.
**Student answer (2):** 10 for old_w=20, lr=0.1, slope=30 → wrong. Correct: 20 − 3 = 17.

**Teacher feedback:** Order of ops: multiply lr*slope first, then subtract from old_w. Retry with simpler numbers.

### Q2c — Simple: old_w=9, lr=1, slope=2
**Student answer:**
7

**Teacher feedback:** 10/10 — step=2, new_w=9-2=7. Update rule locked in.

## M9 complete ✓
