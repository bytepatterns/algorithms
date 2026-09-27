"""
Temperature and Sampling: One distribution, many possible answers.

The model hands back a score for every next token; sampling decides which
one is used. Temperature rescales those scores first — below one sharpens
toward the favourite, above one flattens the field. Top-k and top-p trim the
tail before sampling.

Lesson 9 of AI & ML, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/ai-ml/temperature-and-sampling

Run it:  python ai-ml/09-temperature-and-sampling.py
"""


import math

def softmax(scores, t):
    exp = [math.exp(s / t) for s in scores]
    total = sum(exp)
    return [round(e / total, 3) for e in exp]


if __name__ == "__main__":
    logits = [2.0, 1.0, 0.0]
    print(softmax(logits, 0.5))   # sharp: the favourite dominates
    print(softmax(logits, 1.0))   # the model's own distribution
    print(softmax(logits, 2.0))   # flat: rare tokens get a real chance
