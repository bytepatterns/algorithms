"""
Quantization: Store the weights in fewer bits and buy back memory bandwidth.

A weight stored in sixteen bits can be stored in eight, or four, by keeping
one scale factor per group and rounding each value to the nearest step.
Decoding is limited by how fast weights can be read from memory, so fewer
bytes per weight is directly fewer milliseconds per token.

Lesson 18 of AI & ML, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/ai-ml/quantization

Run it:  python ai-ml/18-quantization.py
"""


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    w = [-0.82, -0.11, 0.0, 0.37, 0.95]
    scale = max(abs(x) for x in w) / 127        # one scale for the group
    q = [round(x / scale) for x in w]
    check(q, [-110, -15, 0, 49, 127])
    back = [v * scale for v in q]
    check(round(max(abs(a - b) for a, b in zip(w, back)), 4), 0.0035)
    q4 = [round(x / (max(abs(x) for x in w) / 7)) for x in w]
    check(q4, [-6, -1, 0, 3, 7])  # 4-bit, coarser
