"""
Unbounded Knapsack: Same table, forward loop — and every item can be taken again.

0/1 knapsack loops capacity backwards so an item cannot be reused. Unbounded
knapsack loops forwards on purpose. Reading a cell this item has already
improved is not a bug here — it is how the second and third copy get taken.
Cutting stock, coin change and rod cutting are all this one recurrence.

Lesson 11 of Dynamic Programming, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/dynamic-programming/unbounded-knapsack

Short video on this lesson: https://www.youtube.com/@bytepatterns

Run it:  python dynamic-programming/11-unbounded-knapsack.py
"""


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    weights = [3, 4, 5]
    values = [30, 50, 60]
    cap = 8

    best = [0] * (cap + 1)
    for c in range(1, cap + 1):                       # forwards, unlike 0/1
        for w, v in zip(weights, values):
            if w <= c:
                best[c] = max(best[c], best[c - w] + v)   # item stays available

    check(best, [0, 0, 0, 30, 50, 60, 60, 80, 100])
    check(best[cap], 100)  # two of the weight-4 item; 0/1 could only reach 90
