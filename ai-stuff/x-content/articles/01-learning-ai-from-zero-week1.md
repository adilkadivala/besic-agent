# X Article / Long thread  ( posted )

**Title options (pick one):**
1. I started learning AI from near-zero. Here’s week 1 in plain English.
2. Hallucinations, tokens, and why one neuron isn’t enough — my first week notes
3. From “what is an LLM?” to backprop intuition in 3 study days

**Format:** Paste into X Articles (Premium) *or* post as a long thread (split at `---`).  
**Source notes:** Day 1 vocab · Math M1–M9 · DL chapters 1–3  
**Status:** Ready to publish after light personal edits

---

## Suggested X Article body

### Opening

I’m learning AI in public.

Not as a fake expert. As a student with notes, quiz scores, and corrections.

Background: non-science path. Goal: become a practical AI / agentic AI engineer — systems I can build and explain, not only buzzwords I can tweet.

Week 1 was not “build a multi-agent swarm.”

It was vocabulary, the math neural nets actually use, and the first deep learning ideas in plain English.

Here’s what stuck.

---

### Day 1 — Learn the language first

Before big PDFs, I forced myself to define terms in my own words.

**LLM**  
A large language model is a neural network trained on lots of text. It generates replies by predicting the next token, again and again.  
Important correction I needed: it doesn’t “think” in the human sense — it predicts.

**Token**  
A small piece of text (word or subword). It’s the unit the model computes on.  
Text → token IDs → predict next ID → decode back to text.

**Prompt**  
The input text: question + instructions + context. Good prompts clarify intent. Users write prompts — and so do developers (system prompts, tool instructions, etc.).

**Hallucination (my worst Day 1 miss)**  
I mixed this up with data leaks / exposing sensitive docs.  
Correct definition: the model invents false facts and states them confidently.  
Privacy leaks are a different failure mode. Same danger class, different mechanism.

**Chatbot vs agent**  
- Chatbot: mostly conversational — input in, answer out.  
- Agent: multi-step actions toward a goal, often with tools (search, APIs, files).  

Reading documents can still be a chatbot + RAG. “Agent” starts when the system plans and acts, not only chats.

I also packed: tool calling, inference, context window, embeddings, RAG, fine-tuning, system prompt, latency, evaluation.

Day 1 quiz average: **~6.7/10**. Honest baseline.

---

### Day 2 — Math without the intimidation

Deep learning PDFs assume comfort with equations. I didn’t have that, so I rebuilt a short path:

variables → functions → linear `y = w·x + b` → vectors → matrices → dot product → slope → loss → gradient descent.

Only math that shows up inside networks. No pure-math tourism.

**The formula that unlocked the neuron for me:**

\[
y = (w \cdot x) + b
\]

- **w** — weights (how much each input matters)  
- **x** — inputs  
- **b** — bias (a shift)  
- **·** — combine (dot product)

**Loss** = how wrong the model is.  
**Gradient descent** (intuition): measure wrongness → find slopes → nudge weights a little → repeat.

```
new_w = old_w − learning_rate × slope
```

Once loss and slopes felt concrete, “training” stopped sounding like magic.

---

### Day 3 — Deep learning foundations (intuition first)

#### 1) The artificial neuron / perceptron

A neuron is not “a vector.”  
It’s a **unit** that **uses** vectors:

\[
z = (w \cdot x) + b
\]

Classic perceptron: turn `z` into 0 or 1 with a threshold rule.

**Limit in one line:** a single perceptron only draws one straight decision boundary. That’s why problems like XOR need more structure (layers).

#### 2) Multi-layer nets and the forward pass

One neuron isn’t enough for hard patterns.

- **Input layer** — receives data  
- **Hidden layers** — middle “middleware” that re-represents data  
- **Output layer** — prediction  

**Forward pass:** input flows through the layers and becomes a prediction.

#### 3) One training step (order matters)

1. Forward  
2. Loss  
3. Gradients  
4. Update  

#### 4) Backpropagation vs gradient descent

I used to blur these.

- **Backpropagation** computes gradients (slopes of the loss w.r.t. weights), flowing error information backward.  
- **Gradient descent** uses those gradients to update weights.  

One calculates. One steps.

That single distinction made chapter 3 click.

---

### What I optimized for this week

1. **Own words over copy-paste definitions**  
2. **Corrections over ego** (4/10 on hallucination still taught more than a clean 10)  
3. **Intuition before notation**  
4. **Notes as a product** — every study day becomes raw material for teaching others (and future-me)

---

### What’s next

Roadmap order I’m following:

1. Finish deep learning foundations + transformers intuition  
2. Ship something small with FastAPI  
3. AI system design thinking  
4. RAG for real  
5. Agents, loops, harnesses, production reliability  

I’m not rushing to post “production multi-tenant RAG architecture” before I’ve built the base.

If you’re learning too: start with language, then the one neuron formula, then forward → loss → gradients → update.

---

### Close / CTA

If this was useful:

- Follow for the next study days (mistakes included)  
- Reply with the term that confused you longest when you started  
- Bookmark if you want a plain-English companion while you study  

Week 2 will go deeper into the network — and I’ll keep publishing from real notes, not vibes.

---

## Thread-sized split (if not using X Articles)

Use each `###` section as 1–2 tweets. Hook tweet:

```
I started learning AI from near-zero.

Week 1 was not agents or RAG.

It was vocabulary, the math nets actually use, and how learning works.

Notes from 3 study days 🧵
```

End with the CTA block above.

---

## Optional image ideas (later)

1. Table: Chatbot vs Agent  
2. Formula card: `z = w·x + b`  
3. Loop diagram: Forward → Loss → Gradients → Update  
4. Your Day 1 score table (vulnerability = trust)

---

*Generated from `notes/` for k-adi’s learning-in-public series.*
