"""
0/1 Knapsack: Each item is all or nothing, so try both and keep the better.

Each item is taken whole or left behind — no halves. For every capacity,
compare the best total that ignores this item against its value plus the
best total for the capacity left over. Sweeping capacity downwards keeps a
single row honest, because a cell is only ever read before this item touched
it.

Lesson 7 of Dynamic Programming, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/dynamic-programming/knapsack-01

Run it:  python dynamic-programming/07-knapsack-01.py
"""


def knapsack(weights, values, cap):
    best = [0] * (cap + 1)                     # best[c] = best value within capacity c
    for w, v in zip(weights, values):
        for c in range(cap, w - 1, -1):        # backwards: this item stays single-use
            best[c] = max(best[c], best[c - w] + v)
    return best[cap]


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(knapsack([3, 4, 5], [30, 50, 60], 8), 90)
    check(knapsack([1, 2, 3], [10, 15, 40], 4), 50)
