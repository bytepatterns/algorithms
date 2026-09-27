"""
Embeddings: Meaning turned into a fixed list of numbers.

An embedding maps text, images or audio to a fixed-length list of numbers.
Models are trained so related items land near each other. Once meaning is
geometry, searching and grouping become arithmetic.

Lesson 3 of AI & ML, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/ai-ml/embeddings

Run it:  python ai-ml/03-embeddings.py
"""


vecs = {"cat": [0.9, 0.1], "kitten": [0.8, 0.2], "car": [0.1, 0.9]}

def embed(words):                          # crude sentence embedding
    total = [0.0, 0.0]
    for w in words:
        for i, v in enumerate(vecs[w]):
            total[i] += v
    return [round(t / len(words), 2) for t in total]


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(embed(["cat", "kitten"]), [0.85, 0.15])  # still in animal territory
    check(embed(["cat", "car"]), [0.5, 0.5])  # a meaningless midpoint
