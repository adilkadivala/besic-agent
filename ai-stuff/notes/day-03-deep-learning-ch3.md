# Day 3/4 — Deep Learning PDF · Chapter 3 (Backpropagation)

**Goal:** Intuition only — how error slopes flow backward so every weight can update.

## Progress
- [x] Forward vs backward
- [x] Backprop = chain of local slopes
- [x] Link to gradient descent (separate jobs)
- [x] Why we need it for deep nets (slopes for every layer)

## Q&A

### Q1 — What is backpropagation (plain words)?
**Student answer:**
backward is a process that goes back from the loss to find slopes/gradients for the weights, then slopes are used to update weights

**Teacher feedback:** 9.5/10 — excellent. Name is backpropagation; it COMPUTES gradients; GD updates. Slight mix of names but idea right.

### Q2 — Backprop vs gradient descent
**Student answer:**
1 computes, 2 updates

**Teacher feedback:** 10/10 — Backprop computes gradients; GD updates weights.

## Chapter 3 core (intuition) complete ✓
