"""
O(log n) and Halving: Throw away half the problem, every single step.

If every step discards half of what is left, you finish in about log2(n)
steps. A million items collapse to roughly twenty steps. Halving is the
cheapest speedup in computing.

Lesson 4 of Big-O, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/big-o/ologn-halving

Run it:  python big-o/04-ologn-halving.py
"""


def halving_steps(n):
    steps = 0
    # keep cutting n in half until nothing is left
    while n > 1:
        n = n // 2
        steps += 1
    return steps


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(halving_steps(8), 3)
    check(halving_steps(1024), 10)
    check(halving_steps(1000000), 19)
