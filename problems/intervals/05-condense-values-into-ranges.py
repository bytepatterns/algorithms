"""
Condense Values Into Ranges (easy) · patterns: intervals, single-pass

You are given a sorted list of distinct integers. Describe it as the
shortest possible list of runs of consecutive integers, in order. Write a
run as "a->b" when it covers more than one value, and as just "a" when it
holds a single value.

Examples:

    Input:  nums = [0, 1, 2, 4, 5, 7]
    Output: ["0->2", "4->5", "7"]

    Input:  nums = [-3, -1, 0]
    Output: ["-3", "-1->0"]
    Why:    negative values follow the same rule

    Input:  nums = []
    Output: []
    Why:    edge case, no values means no runs

Approach:
    Sorted, distinct input means a run breaks precisely where two neighbours
    differ by more than one, so a single left-to-right sweep finds every
    boundary. The outer loop marks where a run starts, the inner loop
    stretches its end while values stay consecutive, and the pair of indexes
    is then written in whichever of the two formats applies. Each index is
    visited once by the inner loop overall, so time is O(n) and space is
    O(1) beyond the output.

The lesson behind it: Interval Basics & Sorting
    https://bytepatterns.com/learn/intervals/interval-basics-and-sorting
    python intervals/01-interval-basics-and-sorting.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/intervals/condense-values-into-ranges

Run it:  python problems/intervals/05-condense-values-into-ranges.py
"""


def condense(nums):
    out, i = [], 0
    while i < len(nums):
        j = i
        while j + 1 < len(nums) and nums[j + 1] == nums[j] + 1:
            j += 1                              # the run is still consecutive
        out.append(str(nums[i]) if i == j else f"{nums[i]}->{nums[j]}")
        i = j + 1                               # next run starts after this one
    return out


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(condense([0, 1, 2, 4, 5, 7]), ['0->2', '4->5', '7'])
    check(condense([-3, -1, 0]), ['-3', '-1->0'])
    check(condense([]), [])
