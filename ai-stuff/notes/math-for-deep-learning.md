# Math for Deep Learning — From Zero

**Student:** k-adi (non-science background — ground-up path)  
**Teacher:** Grok  
**Rule:** Only math that deep learning actually uses. No pure-math fluff.

## Why this exists
The deep learning PDF assumes some comfort with equations. We build that comfort first, in plain language + tiny examples.

## Roadmap (math only)

| Day | Topic | Why DL needs it |
|-----|--------|-----------------|
| M1 | Numbers, variables, simple equations | Weights and formulas |
| M2 | Functions (input → output) | A model *is* a function |
| M3 | Linear: `y = w·x + b` | The basic neuron |
| M4 | Vectors (lists of numbers) | Data & embeddings |
| M5 | Matrices (tables of numbers) | Layers of neurons |
| M6 | Dot product | How a neuron “combines” inputs |
| M7 | Slope / derivative (intuition) | Learning = “which way to tweak” |
| M8 | Loss (error) | Measuring wrong answers |
| M9 | Gradient descent (intuition) | Training loop |
| M10 | Probability basics + softmax (light) | Classification & LLMs |

Then we re-enter `learn/deep-learning.pdf` with confidence.

## Progress
- [x] M1 Numbers & variables
- [x] M2 Functions
- [x] M3 Linear formula (y = w*x + b; weight intuition)
- [x] M4 Vectors
- [x] M5 Matrices
- [x] M6 Dot product
- [x] M7 Slope / derivative
- [x] M8 Loss
- [x] M9 Gradient descent
- [ ] M10 Softmax / probability light (optional)

## Notes
- Core neuron: y = (w · x) + b
- Loss = how wrong; training minimizes loss
- Gradient descent: new_w = old_w − lr * slope
- Student ready for deep-learning.pdf foundations with light support
