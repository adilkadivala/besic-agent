# Article: From zero to Day 7 — what I actually understand now

**Publish as:** X Article (Premium) or long post  
**Coverage:** Day 1 vocabulary → Day 7 eval (through today)  
**Length:** ~900–1100 words · ~4 min read  

**Title options:**
1. I learned AI from near-zero. Here’s everything through Day 7.
2. From “what is a token?” to train/val/test — my plain-English notes
3. 7 study days of deep learning foundations (no hype stack)

**Linking post (short):**
```
7 study days.
Near-zero start.
No multi-agent cosplay yet.

Just the foundations that make later PDFs make sense.

Full notes → article.
```

---

## BODY

---

# I learned AI from near-zero. Here’s everything through Day 7.

I’m documenting AI learning in public.

Not as an expert. As a student with notes, quiz scores, and corrections.

Background: non-science path.  
Goal: practical AI / agentic engineering — after the foundations are real.

Through Day 7 I’ve finished:

- 15 core AI terms in my own words  
- Math for deep learning (M1–M9)  
- Deep learning book cores: neuron → layers → backprop → autograd → activations → losses → optimizers → init/dropout/BatchNorm → overfitting + data splits  

Next up: PyTorch light, then CNN / RNN / Transformer, then agents + a build called StudyForge.

This article is the plain-English dump of what actually stuck.

---

## Day 1 — Learn the language

Before big PDFs, I forced definitions in my own words.

**LLM** — neural net trained on lots of text; generates by predicting the next token.  
**Token** — unit of computation (not “a meaningful sentence chunk”).  
**Prompt** — input text: question + instructions + context.  
**Hallucination** — confident false facts. (I wrongly mixed this with data leaks. Score: 4/10. Fixed.)  
**Chatbot vs agent** — chatbot answers; agent plans, uses tools, takes multi-step actions toward a goal.

Also packed: tool calling, inference, context window, embeddings, RAG, fine-tuning, system prompt, latency, evaluation.

Day 1 average: **~6.7/10**. Baseline, not brand.

---

## Day 2 — Math nets actually use

I rebuilt only what deep learning needs:

variables → functions → `y = w·x + b` → vectors → matrices → dot product → slope → loss → gradient descent.

**Dot product:** pair matching components, multiply, add → one number.  
That’s how a neuron combines many inputs.

**Loss:** a number for how wrong the prediction is. Perfect → ~0.  
**Gradient descent:** use slopes of the loss to nudge weights the useful way, repeatedly:

`new_w = old_w − learning_rate × slope`

I failed this formula on a review quiz once (6.5/10). Order of operations matters: multiply `lr * slope` first.

---

## Days 3–4 — Neuron, layers, activations

**Neuron** is a unit that *uses* vectors, not “a vector”:

`z = (w · x) + b`

Classic perceptron turns `z` into 0/1.  
**Limit:** one straight decision boundary — not enough for hard patterns → stack layers.

**Forward pass:** input → layers → prediction.  
**Hidden layers:** middleware that re-represents data.

**Training step order:**

Forward → Loss → Gradients → Update

**Backprop vs gradient descent:**

- Backprop **computes** gradients  
- Gradient descent **updates** weights  

**ReLU** (Rectified Linear Unit) = `max(0, z)`  
Keep positives. Zero negatives.

Why not a hard step function for deep training?  
Almost no useful slope → backprop starves.

Activations matter because without non-linearity, deep stacks collapse into one big linear map.

---

## Day 5 — Autograd + which activation where

**Computational graph:** built during forward — the recipe of how each number was made. Used going backward for slopes.

**Autograd:** framework tracks ops on the way forward, then computes gradients on backward. You write the forward; it does the calculus.

A weight (or `Value`) carries:

- **data** — current value  
- **grad** — slope of the loss w.r.t. that value  

**Activation cheat sheet I locked:**

| Place | Usual choice |
|--------|----------------|
| Hidden layers | ReLU |
| Multi-class output (e.g. 10 digits) | Softmax (probs sum to 1) |
| Sometimes (0,1) style | Sigmoid (less ideal deep in hidden stacks) |

---

## Day 6 — Losses and optimizers

**Loss function** measures wrongness.  
Training (grads + optimizer) tries to make that measure smaller.

| Problem | Loss |
|---------|------|
| House price (regression) | MSE |
| Digit class (classification) | Cross-entropy |

**Optimizer** runs **after** gradients are computed and updates the weights.

- **SGD** — simple gradient steps  
- **Momentum** — remembers recent direction  
- **Adam** — common default today; adaptive / smart step sizes per weight  

Chain to memorize:

**Loss measures → Backprop computes grads → Optimizer updates weights**

Three jobs. Don’t merge them in your head.

---

## Day 7 — Init, regularization, honest evaluation

**Weight init matters.**  
Don’t set all weights to zero. Too big / too small also breaks training. Weights need a sensible starting point.

**Dropout:** randomly turn off some neurons during training → reduces overfitting.

**BatchNorm (rough):** keep layer inputs on a more stable / nicer scale so training is smoother.

**Overfitting:** memorized the training data; fails on new data.

**Train / Val / Test:**

| Split | Job |
|-------|-----|
| Train | Learn weights |
| Val | Tune + catch overfit |
| Test | Final score only |

I swapped val and test once on a quiz. Correction stuck harder than a clean 10.

If you tune while staring at test metrics, you no longer have a real final exam.

---

## Checkpoints and honesty

Review quiz (math + DL Ch 1–3): **~90/100** strong pass.

Fixes I still recite:

1. `new_w = old_w − lr × slope`  
2. Forward works on any input (images, numbers, text…) — not “text only”  
3. Backprop computes; optimizer / GD updates  

I’m not posting production multi-agent architecture while still locking dropout and val splits.

Learn → note → post the real level.

---

## What’s next

From my completion plan:

| Left | Goal |
|------|------|
| L5 | PyTorch light (tensors, module, train loop) |
| L6 | CNN light |
| L7 | RNN light |
| L8 | Transformer / attention → GPT idea |
| L9 | Capstone quiz |
| Then | Agents + StudyForge build (side by side) |

Locked order:

1. Finish core deep learning  
2. Agentic theory  
3. Build StudyForge with agents — not before  

---

## If you’re starting too

Don’t start with frameworks cosplay.

Start with:

1. Vocabulary you can teach  
2. The neuron formula  
3. Forward → loss → grads → update  
4. ReLU / Softmax placement  
5. MSE vs cross-entropy  
6. Train / val / test discipline  

If you can explain those in plain English, the next PDF will stop feeling like noise.

---

I’m posting the messy middle on purpose.

Follow for Day 8+ (PyTorch light when I finish it).  
Reply with the concept that still feels fuzzy — I’ll turn comment pain into the next short post.

---

## Caption options

### A
```
From "what is a token?" to train/val/test.

7 study days. Near-zero start.
Full plain-English notes in the article.
```

### B
```
Everything I actually understand in AI so far
(not the stuff I'm pretending to know).

Day 1 → Day 7.
```

### C
```
Loss measures.
Backprop computes.
Optimizer updates.

If that chain is new, the article is for you.
```

---

*Source: `notes/day-01.md` … `day-07-dl-l4-eval.md`, `quiz-review-math-ch1-3.md`, `dl-completion-plan.md`*
