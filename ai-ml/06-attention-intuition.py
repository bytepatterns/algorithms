"""
Attention, Intuitively: Every position decides which others to listen to.

Attention lets each position build its own mixture of the others. Relevance
scores are normalised into weights that sum to one, and the output is the
blended values. The weights are recomputed for every input.

Lesson 6 of AI & ML, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/ai-ml/attention-intuition

Short video on this lesson: https://www.youtube.com/@bytepatterns

Run it:  python ai-ml/06-attention-intuition.py
"""


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    values = {"the": [0.0, 1.0], "river": [1.0, 0.0], "bank": [0.5, 0.5]}
    weights = {"the": 0.1, "river": 0.7, "bank": 0.2}   # already sum to 1.0

    out = [0.0, 0.0]
    for word, w in weights.items():
        for i, v in enumerate(values[word]):
            out[i] += w * v                    # blend, do not choose

    check([round(x, 2) for x in out], [0.8, 0.2])  # pulled toward "river"
