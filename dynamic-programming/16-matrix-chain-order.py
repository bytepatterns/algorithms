"""
Interval DP: Answer every short stretch first, then split the long ones.

Some problems are indexed by a stretch rather than a prefix. The answer for
i..j depends on every way to cut it into two shorter stretches, so the table
is filled by length: pairs first, then triples, and so on. Matrix chains,
burst balloons and palindrome partitioning all wear this shape.

Lesson 16 of Dynamic Programming, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/dynamic-programming/matrix-chain-order

Run it:  python dynamic-programming/16-matrix-chain-order.py
"""


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    dims = [10, 30, 5, 60]               # 10x30, 30x5, 5x60
    n = len(dims) - 1
    best = [[0] * n for _ in range(n)]

    for length in range(2, n + 1):       # short stretches first
        for i in range(n - length + 1):
            j = i + length - 1
            best[i][j] = min(
                best[i][k] + best[k + 1][j] + dims[i] * dims[k + 1] * dims[j + 1]
                for k in range(i, j)     # every place to cut the stretch
            )

    check(best[0][n - 1], 4500)  # against 27000 for the other order
