"""
The Missing Value (easy) · patterns: xor-cancel, single-pass

A list holds n distinct values drawn from 0 up to n, in any order, so
exactly one value of that range is absent. Find it in one pass using
constant extra space, which rules out sorting and rules out a set of
everything seen.

Examples:

    Input:  nums = [3, 0, 1]
    Output: 2

    Input:  nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    Output: 8

    Input:  nums = [0]
    Output: 1
    Why:    edge case, the missing value can be n itself

Approach:
    The indexes 0 through n-1 plus the extra value n cover the same range as
    the complete list would, so folding indexes and values together with XOR
    pairs almost everything off. A value cancels against the equal number
    contributed by the index side, leaving only the number nobody supplied.
    Starting the accumulator at n is what supplies the one index the list
    does not have. Time is O(n) in a single pass, and space is O(1).

The lesson behind it: XOR Tricks
    https://bytepatterns.com/learn/bit-manipulation/xor-tricks
    python bit-manipulation/02-xor-tricks.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/bit-manipulation/missing-value-in-range

Run it:  python problems/bit-manipulation/03-missing-value-in-range.py
"""


def missing(nums):
    answer = len(nums)            # n, the index the list does not have
    for i, v in enumerate(nums):
        answer ^= i ^ v           # each matched pair cancels itself out
    return answer


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(missing([3, 0, 1]), 2)
    check(missing([9, 6, 4, 2, 3, 5, 7, 0, 1]), 8)
    check(missing([0]), 1)
    check(missing([1]), 0)
