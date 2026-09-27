"""
Cosine Similarity: Compare direction, ignore magnitude.

Cosine similarity is the cosine of the angle between two vectors: their dot
product divided by both lengths. It runs from 1 for the same direction,
through 0 for unrelated, to -1 for opposite.

Lesson 4 of AI & ML, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/ai-ml/cosine-similarity

Short video on this lesson: https://www.youtube.com/@bytepatterns

Run it:  python ai-ml/04-cosine-similarity.py
"""


import math

def cosine(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    na = math.sqrt(sum(x * x for x in a))
    nb = math.sqrt(sum(y * y for y in b))
    return round(dot / (na * nb), 2)


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    doc = [1, 2, 0]
    longer_same_topic = [3, 6, 0]        # same direction, three times the length
    other_topic = [0, 0, 5]
    check(cosine(doc, longer_same_topic), 1.0)
    check(cosine(doc, other_topic), 0.0)
