"""
Set Bits For Every Number (easy) · patterns: bit-shifting, reuse-smaller-answer

Given a non-negative whole number n, return a list whose entry at index i is
the number of ones in the binary form of i, for every i from 0 up to n
inclusive. Try to fill the whole list in a single pass without looping over
the digits of each number.

Examples:

    Input:  n = 5
    Output: [0, 1, 1, 2, 1, 2]
    Why:    0, 1, 10, 11, 100, 101 in binary

    Input:  n = 2
    Output: [0, 1, 1]

    Input:  n = 0
    Output: [0]
    Why:    edge case, the list still holds the entry for zero itself

Approach:
    Dropping the lowest binary digit of i gives i shifted right by one, a
    smaller number whose count is already known, so the count for i is that
    stored count plus the dropped digit. Filling the list in increasing
    order guarantees every lookup points backwards to a finished entry. Each
    entry costs one shift, one AND and one addition. Time is O(n) and the
    output list is O(n) space.

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/bit-manipulation/set-bits-for-every-number

Run it:  python problems/bit-manipulation/05-set-bits-for-every-number.py
"""


def set_bits_up_to(n):
    counts = [0] * (n + 1)
    for i in range(1, n + 1):
        counts[i] = counts[i >> 1] + (i & 1)   # reuse the answer without the low digit
    return counts


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(set_bits_up_to(5), [0, 1, 1, 2, 1, 2])
    check(set_bits_up_to(2), [0, 1, 1])
    check(set_bits_up_to(0), [0])
