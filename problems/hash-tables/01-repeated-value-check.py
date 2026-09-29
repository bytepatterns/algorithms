"""
Repeated Value Check (easy) · patterns: hash-set, single-pass

Given a list of values, decide whether any value shows up more than once.
Return true if at least one value repeats anywhere in the list, and false
when every value is unique. The repeats do not have to be next to each
other.

Examples:

    Input:  items = [4, 1, 9, 1]
    Output: True
    Why:    the value 1 appears at two different positions

    Input:  items = [4, 1, 9]
    Output: False
    Why:    all three values differ

    Input:  items = []
    Output: False
    Why:    edge case, an empty list cannot contain a repeat

Approach:
    A set of already-seen values turns the repeated-value question into a
    constant-time membership test. Walking the list once and testing before
    inserting means the answer is returned the moment a second copy appears,
    without finishing the scan. Time is O(n) on average, and space is O(n)
    in the worst case when all values are distinct.

The lesson behind it: Frequency Counting
    https://bytepatterns.com/learn/hash-tables/frequency-counting
    python hash-tables/03-frequency-counting.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/hash-tables/repeated-value-check

Run it:  python problems/hash-tables/01-repeated-value-check.py
"""


def has_repeat(items):
    seen = set()                     # values met so far
    for x in items:
        if x in seen:                # this exact value already appeared
            return True
        seen.add(x)
    return False                     # the scan finished without a collision


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(has_repeat([4, 1, 9, 1]), True)
    check(has_repeat([4, 1, 9]), False)
    check(has_repeat([]), False)
