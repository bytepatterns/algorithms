"""
Three Values Summing to Zero (medium) · patterns: two-pointers, sort-first, skip-duplicates

A ledger audit looks for three entries that cancel out exactly. Given a list
of integers nums, return every distinct triplet [a, b, c] of values taken
from three different positions with a + b + c = 0. Write each triplet in
ascending order and list the triplets in ascending order; two triplets with
the same values count once. The list has up to 3,000 values, so trying every
triple is too slow.

Examples:

    Input:  nums = [-1, 0, 1, 2, -1, -4]
    Output: [[-1, -1, 2], [-1, 0, 1]]
    Why:    the two -1 values can both be used, but [-1, 0, 1] is listed once

    Input:  nums = [0, 1, 1]
    Output: []

    Input:  nums = [0, 0, 0, 0]
    Output: [[0, 0, 0]]
    Why:    edge case, four zeros still give just one distinct triplet

Approach:
    After sorting, fixing the first value a turns the rest into a pair
    search for -a on the part of the list to its right, and two pointers
    from both ends find every pair in one pass because moving the left
    pointer only raises the sum and moving the right one only lowers it.
    Duplicates are skipped at both levels: a value of a equal to the one
    before it would repeat the same triplets, and after a match the left
    pointer steps past equal values, since once a and b are fixed the third
    value is fixed too. Once a is positive no triplet can sum to zero, so
    the loop stops early. Time is O(n²), and extra space is O(n) for the
    sorted copy.

The lesson behind it: Two Pointers
    https://bytepatterns.com/learn/arrays/two-pointers
    python arrays/02-two-pointers.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/arrays/three-values-summing-to-zero

Run it:  python problems/arrays/18-three-values-summing-to-zero.py
"""


def zero_triplets(nums):
    s, out = sorted(nums), []
    for i in range(len(s) - 2):
        if s[i] > 0:
            break                              # three positives never sum to zero
        if i > 0 and s[i] == s[i - 1]:
            continue                           # same first value, same triplets
        lo, hi = i + 1, len(s) - 1
        while lo < hi:
            total = s[i] + s[lo] + s[hi]
            if total < 0:
                lo += 1
            elif total > 0:
                hi -= 1
            else:
                out.append([s[i], s[lo], s[hi]])
                lo += 1
                hi -= 1
                while lo < hi and s[lo] == s[lo - 1]:
                    lo += 1                    # skip repeats of the middle value
    return out


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(zero_triplets([-1, 0, 1, 2, -1, -4]), [[-1, -1, 2], [-1, 0, 1]])
    check(zero_triplets([0, 1, 1]), [])
    check(zero_triplets([0, 0, 0, 0]), [[0, 0, 0]])
