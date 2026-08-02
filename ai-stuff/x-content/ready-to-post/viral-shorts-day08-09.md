# Viral shorts — Day 8 → today (Day 9)

**Scope only:** L5 PyTorch · L6 CNN · L7 RNN · L8 Transformer · L9 Capstone  
**Not included:** Day 1–7 (already generated)  
**Milestone:** **DL COMPLETE ~93%** → next = Agents + StudyForge  

Mark `[x]` when live.

---

# L5 — PyTorch light

### PT1 `[x]`
```
What is a tensor?

A block/array of numbers.
1D, 2D, higher dims.

In PyTorch: inputs, weights, outputs.

#buildinpublic 
#LearningWithLeapfrog 
#LearningInPublic 
#LearnInPublic 
#LLMs 
#ai 
```

### PT2 `[x]`
```
PyTorch train step order I locked:

forward
→ loss
→ zero_grad
→ backward
→ optimizer.step

(zero_grad can also sit at the top of the loop)

#buildinpublic 
#LearningWithLeapfrog 
#LearningInPublic 
#LearnInPublic 
#LLMs 
#ai
```

### PT3 `[x]`
```
Frameworks don't replace understanding.

They automate the graph + grads.

You still need:
forward → loss → backward → step

#buildinpublic 
#LearningWithLeapfrog 
#LearningInPublic 
#LearnInPublic 
#LLMs 
#ai
```

### PT4 `[x]`
```
Tensor = the noun
Autograd = the verb that fills .grad
Optimizer = the hand that moves weights

PyTorch in three roles.

#buildinpublic 
#LearningWithLeapfrog 
#LearningInPublic 
#LearnInPublic 
#LLMs 
#ai
```

---

# L6 — CNN light

### CNN1 `[x]`
```
Why CNNs for images (not only dense layers)?

Images are grids.
CNNs look at local neighborhoods
with shared filters.

#buildinpublic 
#LearningWithLeapfrog 
#LearningInPublic 
#LearnInPublic 
#LLMs 
#ai
```

### CNN2 `[x]`
```
Dense layers treat every pixel as unrelated.

CNNs respect locality:
nearby pixels matter together.

That's the whole pitch.

#buildinpublic 
#LearningWithLeapfrog 
#LearningInPublic 
#LearnInPublic 
#LLMs 
#ai
```

### CNN3 `[x]`
```
Shared filters =

same pattern detector reused across the image.

Fewer params.
Better inductive bias for vision.

#buildinpublic 
#LearningWithLeapfrog 
#LearningInPublic 
#LearnInPublic 
#LLMs 
#ai
```

---

# L7 — RNN / sequences

### RNN1 `[x]`
```
Why RNNs for sequences?

Data comes one step after another.
The model keeps a memory / hidden state
of what came before.

#buildinpublic 
#LearningWithLeapfrog 
#LearningInPublic 
#LearnInPublic 
#LLMs 
#ai
```

### RNN2 `[x]`
```
Text, time series, speech —

order matters.
RNNs (and LSTMs) were built for that.

#buildinpublic 
#LearningWithLeapfrog 
#LearningInPublic 
#LearnInPublic 
#LLMs 
#ai
```

### RNN3 `[x]`
```
Hidden state = short-term memory of the past steps.

That's the RNN idea in one phrase.

#buildinpublic 
#LearningWithLeapfrog 
#LearningInPublic 
#LearnInPublic 
#LLMs 
#ai
```

---

# L8 — Attention / Transformers / GPT

### TF1 `[x]`
```
Attention (plain English):

Tokens can look at other tokens
and focus on what's most relevant
to build better context.

#buildinpublic 
#LearningWithLeapfrog 
#LearningInPublic 
#LearnInPublic 
#LLMs 
#ai
```

### TF2 `[x]`
```
Don't mix these:

Attention = the focus mechanism
Transformer = the full architecture
that stacks attention (and more)

#buildinpublic 
#LearningWithLeapfrog 
#LearningInPublic 
#LearnInPublic 
#LLMs 
#ai
```

### TF3 `[x]`
```
GPT / LLM in one line:

Decoder Transformer
+ next-token training
(usually with cross-entropy-style loss)

#buildinpublic 
#LearningWithLeapfrog 
#LearningInPublic 
#LearnInPublic 
#LLMs 
#ai
```

### TF4 `[x]`
```
Next-token prediction isn't a toy.

It's the training objective
that made modern LLMs possible.

#buildinpublic 
#LearningWithLeapfrog 
#LearningInPublic 
#LearnInPublic 
#LLMs 
#ai
```

### TF5 `[x]`
```
CNN → images (local grids)
RNN → sequences (memory over time)
Transformer → context via attention

Pick the tool for the data shape.

#buildinpublic 
#LearningWithLeapfrog 
#LearningInPublic 
#LearnInPublic 
#LLMs 
#ai
```

### TF6 `[x]`
```
I used to say "Transformer helps tokens look around."

More precise:

Attention is what lets tokens focus.
Transformer is the stack that uses it.

#buildinpublic 
#LearningWithLeapfrog 
#LearningInPublic 
#LearnInPublic 
#LLMs 
#ai
```

---

# L9 — Capstone + milestone

### CAP1 `[x]`
```
Deep learning capstone quiz:

~112/120 ≈ 93%

PASS.
Compressed DL core: COMPLETE.

Next: agents theory → StudyForge build.

#buildinpublic 
#LearningWithLeapfrog 
#LearningInPublic 
#LearnInPublic 
#LLMs 
#ai
```

### CAP2 `[ ]`
```
What I still correct myself on:

Forward pass = the prediction path.
The computational graph is a side effect
of going forward — not the goal itself.

#buildinpublic 
#LearningWithLeapfrog 
#LearningInPublic 
#LearnInPublic 
#LLMs 
#ai
```

### CAP3 `[ ]`
```
Capstone locks I'm proud of:

Backprop computes · optimizer updates
ReLU = Rectified Linear Unit
Softmax = multi-class probs sum to 1
GPT = decoder Transformer + next token

#buildinpublic 
#LearningWithLeapfrog 
#LearningInPublic 
#LearnInPublic 
#LLMs 
#ai
```

### CAP4 `[ ]`
```
From "what is a variable?"
to "GPT is a decoder Transformer."

Non-science start.
Compressed DL path done at ~93%.

Learning in public works if you take quizzes.


#buildinpublic 
#LearningWithLeapfrog 
#LearningInPublic 
#LearnInPublic 
#LLMs 
#ai
```

### CAP5 `[ ]`
```
Plan was locked weeks ago:

1) Core deep learning ← DONE
2) Agents / agentic theory ← NEXT
3) StudyForge beside agents (not before)

No multi-agent cosplay on day 1.
Foundations first.

#buildinpublic 
#LearningWithLeapfrog 
#LearningInPublic 
#LearnInPublic 
#LLMs 
#ai
```

### CAP6 `[x]`
```
If you're learning AI:

Finish the training loop
before you tweet agent swarms.

Guess → loss → grads → update
still runs the world under the hood.

#buildinpublic 
#LearningWithLeapfrog 
#LearningInPublic 
#LearnInPublic 
#LLMs 
#ai
```

---

# Engagement

### E1 `[x]`
```
Which architecture maps to which data?

A) CNN
B) RNN
C) Transformer

Reply with "images / sequences / context" order.
I'll tell you if you nailed it.

#buildinpublic 
#LearningWithLeapfrog 
#LearningInPublic 
#LearnInPublic 
#LLMs 
#ai
```

### E2 `[x]`
```
Attention or Transformer —
which word do people misuse more?

I mixed them until Day 9.

#buildinpublic 
#LearningWithLeapfrog 
#LearningInPublic 
#LearnInPublic 
#LLMs 
#ai
```

### E3 `[x]`
```
Reply "agents" if you want the first plain-English
agent vs chatbot thread when I start Phase next.


```

### E4 `[x]`
```
PyTorch order — without peeking:

forward / loss / zero_grad / backward / step

Did you get the same order I did?

#buildinpublic 
#LearningWithLeapfrog 
#LearningInPublic 
#LearnInPublic 
#LLMs 
#ai
```

---

## 5-day schedule (Day 8–9 content only)

| Day | Posts |
|-----|--------|
| 1 | PT2, CNN1 |
| 2 | RNN1, TF1 |
| 3 | TF2, TF3 |
| 4 | TF5, CAP1 |
| 5 | CAP5, E3 + **Article 04** or **Thread** |

Don't dump all milestone posts same hour — space CAP1 / CAP4 / CAP5 across days.
