# Thread — AI from zero through Day 7 (today)

**Post as one thread.** Tweet 1 = hook.  
**Source:** all notes Day 1 → Day 7  

---

### T1 — Hook
```
I started AI from near-zero.

No science degree.
Just notes, quizzes, and corrections.

Here's everything I locked through Day 7 🧵
```

### T2
```
Day 1 — language first

LLM = next-token prediction, not "thinking"
Token = unit of compute
Hallucination = confident fake facts (≠ data leak)
Chatbot answers · Agent acts with tools
```

### T3
```
Day 2 — math nets actually use

variables → functions → vectors → matrices
dot product → slopes → loss → gradient descent

Only what deep learning needs.
No pure-math tourism.
```

### T4
```
Core formula:

z = (w · x) + b

Weights = importance
Bias = shift
Dot product = combine inputs into one number
```

### T5
```
Days 3–4 — the network

Neuron = unit (not "a vector")
One neuron = one straight boundary
Forward = input → layers → prediction
Hidden layers = middleware that re-represents data
```

### T6
```
Training loop (tattoo this):

Forward → Loss → Gradients → Update

Backprop COMPUTES gradients
Gradient descent / optimizer UPDATES weights
```

### T7
```
ReLU = max(0, z)
Keep positives. Zero out negatives.

Hard 0/1 step? Bad for deep training —
almost no useful slope for backprop.
```

### T8
```
Day 5 — autograd

Forward builds a computational graph
("how each number was made")

Autograd tracks ops, then fills gradients on backward

data = value
grad = slope of the loss
```

### T9
```
Activations cheat sheet

Hidden layers → usually ReLU
10-class digits → Softmax (probs sum to 1)
Sigmoid → (0,1), less ideal deep in hidden stacks
```

### T10
```
Day 6 — losses + optimizers

House price → MSE
Digit class → cross-entropy

Optimizer runs AFTER grads:
updates weights (Adam = common default, adaptive steps)
```

### T11
```
Day 7 — make training survive reality

Init matters (not all zeros; not insane scale)
Dropout = randomly off neurons → less overfit
BatchNorm ≈ keep layer inputs on a nicer scale
Overfit = memorized train, failed on new data
```

### T12
```
Train / Val / Test

Train = learn
Val = tune + watch overfit
Test = final score only

I swapped val/test once in a quiz.
Never again.
```

### T13
```
Checkpoints so far

Review quiz (math + Ch1–3): ~90/100
Weak spots fixed: GD formula, forward ≠ only text,
backprop vs GD wording

DL core left: PyTorch → CNN → RNN → Transformer → capstone
Then: agents + StudyForge build
```

### T14 — Close
```
Plan (locked):

1) Finish core deep learning
2) Agents / agentic theory
3) Build StudyForge beside agents — not before

Follow for plain-English notes from the real level I'm at.

Reply "next" if you want the PyTorch light thread when I finish L5.
```
