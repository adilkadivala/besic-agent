# Day 3 — Deep Learning PDF · Chapter 1 (Neuron / Perceptron)

**PDF:** `learn/deep-learning.pdf`  
**Teacher approach:** plain English + your math (M1–M9). Skip heavy notation first.

## Progress
- [x] What is a neuron / perceptron?
- [x] z = w·x + b, then step to 0/1
- [x] Threshold rule practice
- [x] One-line limit of single perceptron

## Q&A

### Q1 — What is an artificial neuron (in plain words)?
**Student answer:**
neuron is a vector that weighted sum ( + bias ) - z = (w -x) + b, and it produces an output 0 or 1

**Teacher feedback:**
- Good: weighted sum + bias, output 0 or 1 for classic perceptron
- Fix: neuron is a *unit/function*, not "a vector" (it *uses* vectors w and x)
- Fix formula: z = (w · x) + b  (dot product), NOT (w - x) + b
- Score: 6.5/10

### Q2 — Compute z and output for loan example
**Student answer:**
z = -2.6 , output will be 0

**Teacher feedback:**
- Output 0 correct (negative z → 0)
- z arithmetic: correct is -2.0 not -2.6
  3*0.2 + (-2)*0.8 + (-1) = 0.6 - 1.6 - 1 = -2.0
- Score: 8/10 — decision right, calc slightly off

### Q3 — If z=1.5, output?
**Student answer:**
1

**Teacher feedback:** 10/10 — z ≥ 0 → 1

### Q4 — One-line limit of a single perceptron
**Student answer:**
false

**Teacher feedback:** 9/10 — correct. Reason: only one straight decision boundary; fails on non-linearly separable problems (e.g. XOR).

## Chapter 1 core complete ✓
