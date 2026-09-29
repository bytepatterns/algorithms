"""
Single Value Among Triples (medium) · patterns: bit-counting, modular-arithmetic

In a list of non-negative whole numbers, every value appears exactly three
times except one, which appears once. Find that lone value. Aim for constant
extra space, so building a tally of every distinct value is off the table.

Examples:

    Input:  nums = [2, 2, 3, 2]
    Output: 3

    Input:  nums = [30, 1, 1, 1, 30, 30, 7]
    Output: 7
    Why:    the repeats do not have to sit together

    Input:  nums = [5]
    Output: 5
    Why:    edge case, a single value is trivially the lone one

Approach:
    Looking at a single binary position across the whole list, each tripled
    value contributes either three ones or none, so the count at that
    position is a multiple of three plus the lone value's own digit. Taking
    the count modulo three therefore recovers that digit exactly, and doing
    this for all 32 positions rebuilds the value. Only a fixed set of
    counters is ever held, which is what keeps the space constant. Time is
    O(32n), which is linear, and space is O(1).

The lesson behind it: XOR Tricks
    https://bytepatterns.com/learn/bit-manipulation/xor-tricks
    python bit-manipulation/02-xor-tricks.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/bit-manipulation/single-value-among-triples

Run it:  python problems/bit-manipulation/02-single-value-among-triples.py
"""


def lone_value(nums):
    answer = 0
    for position in range(32):
        # how many values carry a one at this binary position
        ones = sum((x >> position) & 1 for x in nums)
        if ones % 3:                 # the triples contribute 0 or 3, never 1 or 2
            answer |= 1 << position
    return answer


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(lone_value([2, 2, 3, 2]), 3)
    check(lone_value([30, 1, 1, 1, 30, 30, 7]), 7)
    check(lone_value([5]), 5)
