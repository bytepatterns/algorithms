"""
BPE vs WordPiece: Two ways to decide which pair of pieces becomes one piece.

Both algorithms start from single characters and repeatedly glue one
adjacent pair into a new piece. Byte-pair encoding picks the pair that
occurs most often. WordPiece picks the pair whose joint count is highest
relative to its parts' counts, which favours pairs that genuinely belong
together.

Lesson 23 of AI & ML, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/ai-ml/bpe-vs-wordpiece

Run it:  python ai-ml/23-bpe-vs-wordpiece.py
"""


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    from collections import Counter
    toks = [list(w) + ["_"] for w in ["low", "low", "low", "lower"]]
    for _ in range(2):
        pairs = Counter(a + b for t in toks for a, b in zip(t, t[1:]))
        best, n = pairs.most_common(1)[0]
        print(best, n)                      # lo 4   then   low 4
        merged = []
        for t in toks:
            out, i = [], 0
            while i < len(t):
                hit = i + 1 < len(t) and t[i] + t[i + 1] == best
                out.append(best if hit else t[i]); i += 2 if hit else 1
            merged.append(out)
        toks = merged
    check(toks[0], ['low', '_'])
