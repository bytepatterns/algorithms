"""
Coin Change: Fewest pieces to hit a target, one amount at a time.

Build the answer for every amount from 1 up to the target. The fewest pieces
making amount a is one more than the fewest making a minus some coin, so try
each coin and keep the smallest result. Amounts nothing can reach stay at
infinity, which is exactly how the function knows to report failure.

Lesson 5 of Dynamic Programming, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/dynamic-programming/coin-change

Short video on this lesson: https://www.youtube.com/@bytepatterns

Run it:  python dynamic-programming/05-coin-change.py
"""


def fewest(coins, target):
    INF = float("inf")
    best = [0] + [INF] * target              # best[a] = fewest coins making a
    for a in range(1, target + 1):
        for c in coins:
            if c <= a and best[a - c] + 1 < best[a]:
                best[a] = best[a - c] + 1    # one coin on top of a solved amount
    return -1 if best[target] == INF else best[target]


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(fewest([1, 5, 10], 27), 5)
    check(fewest([4, 6], 7), -1)
