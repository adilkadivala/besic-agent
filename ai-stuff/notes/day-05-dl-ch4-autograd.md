# Day 5 — Deep Learning Ch 4: Autograd (intuition)

**Where we left off:** Ch1 neuron, Ch2 forward, Ch3 backprop, ReLU  
**Today:** Why frameworks track a graph + what `backward()` means  
**After class (later):** small build on StudyForge or toy Value demo

## Progress
- [x] Computational graph idea
- [x] Autograd = automatic backprop
- [x] Value: data + grad
- [x] Link to training loop

## Q&A

### Q1 — What is a computational graph?
**Student answer:**
computational graph is how each number is made, created at forward pass, useful going backward to find slopes/gradients

**Teacher feedback:** 10/10 — excellent.

### Q2 — What is autograd?
**Student answer:**
autograd tracks operation during forward pass and automatically computes gradients on backward

**Teacher feedback:** 10/10 — exact. Spelling: backward.

### Q3 — data vs grad on a Value/weight
**Student answer:**
1 value, 2 slopes (slops)

**Teacher feedback:** 10/10 — data=value, grad=slope of loss. Spelling: slopes.

## Chapter 4 core (intuition) complete ✓
