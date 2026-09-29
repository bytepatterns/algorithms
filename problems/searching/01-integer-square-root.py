"""
Integer Square Root (easy) · patterns: binary-search, monotonic-predicate

Given a non-negative whole number, return the largest whole number whose
square does not exceed it. The fractional part is discarded rather than
rounded, so a number that is not a perfect square gives the value just below
its true root. Built-in square root functions are not allowed.

Examples:

    Input:  n = 8
    Output: 2
    Why:    2 squared is 4 and 3 squared is 9, so the answer is cut down to 2

    Input:  n = 16
    Output: 4
    Why:    a perfect square returns its exact root

    Input:  n = 0
    Output: 0
    Why:    edge case, zero is its own root

Approach:
    The test does my square fit is monotone: it holds for every candidate up
    to the answer and fails for every candidate beyond it, which is exactly
    the structure a halving search needs. Each round squares the middle
    candidate and throws away half the range, remembering the candidate
    whenever it passes so the final answer survives. Comparing squares
    rather than taking a root keeps everything in whole numbers. Time is
    O(log n), and space is O(1).

The lesson behind it: Binary Search
    https://bytepatterns.com/learn/searching/binary-search
    python searching/02-binary-search.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/searching/integer-square-root

Run it:  python problems/searching/01-integer-square-root.py
"""


def integer_sqrt(n):
    low, high, best = 0, n, 0
    while low <= high:
        mid = (low + high) // 2
        if mid * mid <= n:           # mid fits, but something larger might too
            best, low = mid, mid + 1
        else:
            high = mid - 1           # mid is too big, and so is everything above
    return best


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(integer_sqrt(8), 2)
    check(integer_sqrt(16), 4)
    check(integer_sqrt(0), 0)
