# Review Quiz — Math M1–M9 + Deep Learning Ch 1–3

**Student:** k-adi  
**Status:** Graded ✓  
**Next:** B done ✓ → A (activations)

## Scores

| # | Topic | Score | Note |
|---|--------|------:|------|
| 1 | Variable | 9/10 | Name holding a value |
| 2 | Compute y=2x+1 | 10/10 | y=15 |
| 3 | Vector | 10/10 | List of numbers |
| 4 | Dot product | 10/10 | 11 |
| 5 | Loss | 9/10 | How wrong; is a number |
| 6 | GD update | 6.5/10 | Uses gradients ✓; missing formula `w ← w − lr*slope` |
| 7 | Perceptron z=-0.5 | 10/10 | Output 0 |
| 8 | Forward pass | 8/10 | Input→layers→pred; not only "text" |
| 9 | Hidden layer | 10/10 | Middleware / re-represent |
| 10 | Backprop vs GD | 7/10 | "computes" not "functions"; updates ✓ |
| **Total** | | **~90/100** | **Strong pass** |

## Fixes to remember
- GD: `new_w = old_w − learning_rate * slope`
- Forward: any **input** (image, numbers, text…), not only text
- Backprop **computes** gradients; GD **updates** weights
