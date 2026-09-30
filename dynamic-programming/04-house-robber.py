"""
House Robber: Take this one and skip its neighbour, or skip it and keep the best.

Values sit in a row and picking one forbids both of its neighbours. At every
position ask a single question: take this value plus the best total that
ended two positions back, or skip it and carry the best so far forward? Two
running totals hold everything the decision needs, so no array of results is
required.

Lesson 4 of Dynamic Programming, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/dynamic-programming/house-robber

Short video on this lesson: https://www.youtube.com/@bytepatterns

Run it:  python dynamic-programming/04-house-robber.py
"""


def rob(values):
    skip, take = 0, 0                              # best ending here: unused / used
    for v in values:
        skip, take = max(skip, take), skip + v     # taking v needs the previous skipped
    return max(skip, take)


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(rob([2, 7, 9, 3, 1]), 12)
    check(rob([5, 5, 10, 100, 10, 5]), 110)
