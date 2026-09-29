"""
Fewest Swaps to Sort (medium) · patterns: cycle-decomposition, selection-sort

Given a list of distinct integers, return the smallest number of swaps that
sorts it in ascending order. One swap exchanges the values at any two
positions, and the two positions do not have to be next to each other.

Examples:

    Input:  nums = [4, 3, 1, 2]
    Output: 3
    Why:    4 must go to index 3, the 2 there to index 1, the 3 there to
            index 2 and the 1 there to index 0: one loop of four values

    Input:  nums = [10, 30, 20]
    Output: 1
    Why:    swapping 30 and 20 is enough

    Input:  nums = [7]
    Output: 0
    Why:    edge case, a single value is already sorted

Approach:
    Sending each value to its sorted position splits the positions into
    cycles, and a sorted list is exactly n cycles of length one. Any swap
    changes the number of cycles by exactly one, so at least n minus the
    current cycle count swaps are needed, and placing one value into its
    final position per swap achieves that: a cycle of length L costs L - 1.
    Selection sort that skips swapping a value with itself follows exactly
    this plan, which is why it never makes more swaps than necessary even
    though it makes O(n²) comparisons. Time is O(n log n) for the sort that
    finds the targets, and space is O(n).

The lesson behind it: Selection Sort
    https://bytepatterns.com/learn/sorting/selection-sort
    python sorting/03-selection-sort.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/sorting/fewest-swaps-to-sort

Run it:  python problems/sorting/08-fewest-swaps-to-sort.py
"""


def fewest_swaps(nums):
    target = {v: i for i, v in enumerate(sorted(nums))}   # where each value belongs
    seen, swaps = [False] * len(nums), 0
    for start in range(len(nums)):
        length, i = 0, start
        while not seen[i]:                 # walk one cycle back to its start
            seen[i] = True
            i = target[nums[i]]
            length += 1
        swaps += max(length - 1, 0)        # a cycle of L values needs L - 1 swaps
    return swaps


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(fewest_swaps([4, 3, 1, 2]), 3)
    check(fewest_swaps([10, 30, 20]), 1)
    check(fewest_swaps([7]), 0)
