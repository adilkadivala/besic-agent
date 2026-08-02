# Thread — Day 8–9: PyTorch → GPT → DL complete

**Only new material** (after Day 7 pack).  

---

### T1
```
I finished the compressed deep learning core.

Capstone: ~93%.

Here's Day 8–9 in plain English:
PyTorch → CNN → RNN → Transformer → GPT 🧵
```

### T2
```
L5 — PyTorch light

Tensor = array of numbers (inputs, weights, outputs)

Train step:
forward → loss → zero_grad → backward → step
```

### T3
```
Frameworks automate autograd.

They don't replace the loop:

guess → measure wrong → compute slopes → update
```

### T4
```
L6 — CNN (images)

Images are grids.
CNNs scan local neighborhoods
with shared filters.

Dense-only = every pixel treated as unrelated.
```

### T5
```
L7 — RNN (sequences)

Data arrives step by step.
Model keeps a hidden state = memory of the past.

Order matters → sequences need memory.
```

### T6
```
L8 — Attention vs Transformer

Attention: tokens look at other tokens
and focus on what's relevant.

Transformer: full architecture
built from attention stacks (+ more).
```

### T7
```
GPT / LLM in one line (capstone 10/10):

Decoder Transformer
+ next-token training
(cross-entropy style)
```

### T8
```
Architecture cheat sheet:

CNN → images (local structure)
RNN → sequences (time/order + memory)
Transformer → rich context via attention

Match the model to the data shape.
```

### T9
```
Capstone scoreboard:

~112/120 ≈ 93% PASS

Strong: backprop vs opt, ReLU, Softmax, CNN/RNN/TF, GPT
Fix I noted: forward = prediction path;
graph is a side effect of forward
```

### T10
```
Status:

✅ Math M1–M9
✅ Neuron → train loop → autograd → activations
✅ Losses, Adam, dropout, train/val/test
✅ PyTorch · CNN · RNN · Transformer
✅ DL COMPLETE

➡️ Next: Agents theory → StudyForge build
```

### T11
```
Locked plan still stands:

1) Deep learning foundations — done
2) Agentic AI theory — starting
3) Build StudyForge beside agents — not before

Follow for Phase 2 notes.
Reply "agents" for the first agent thread.
```
