"""
Two Lone Values (medium) · patterns: xor-cancel, bit-partition

In a list of integers, every value appears exactly twice except two
different values that appear once each. Return those two, smaller first. Use
linear time and constant extra space, so a tally of every value is not
allowed.

Examples:

    Input:  nums = [1, 2, 1, 3, 2, 5]
    Output: [3, 5]

    Input:  nums = [2, 0, 2, 6]
    Output: [0, 6]
    Why:    zero can be one of the lone values

    Input:  nums = [4, 9]
    Output: [4, 9]
    Why:    edge case, no pairs at all, only the two lone values

Approach:
    XOR-ing everything leaves a XOR b, since each pair cancels itself.
    Because a and b differ, that result has at least one set bit, and at
    that position exactly one of them has a one. Splitting the whole list on
    that bit sends both copies of every pair to the same side while
    separating a from b, so XOR-ing one side isolates one lone value, and
    XOR-ing it back into the combined result gives the other. The lowest set
    bit is found with x AND negative x. Time is O(n) over two passes and
    space is O(1).

The lesson behind it: XOR Tricks
    https://bytepatterns.com/learn/bit-manipulation/xor-tricks
    python bit-manipulation/02-xor-tricks.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/bit-manipulation/two-lone-values

Run it:  python problems/bit-manipulation/06-two-lone-values.py
"""


def two_lone(nums):
    both = 0
    for x in nums:
        both ^= x                  # pairs cancel, leaving a ^ b
    low = both & -both             # a bit where a and b disagree
    a = 0
    for x in nums:
        if x & low:                # one side of the split; pairs never straddle it
            a ^= x
    b = both ^ a
    return [min(a, b), max(a, b)]


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(two_lone([1, 2, 1, 3, 2, 5]), [3, 5])
    check(two_lone([2, 0, 2, 6]), [0, 6])
    check(two_lone([4, 9]), [4, 9])
