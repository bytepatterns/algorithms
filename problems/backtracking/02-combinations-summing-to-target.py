"""
Combinations That Sum (medium) · patterns: backtracking, pruning

Given a list of distinct positive numbers and a target, return every group
of them that adds up exactly to the target. A number may be used as many
times as you like, and two groups holding the same numbers in a different
order count as one answer.

Examples:

    Input:  nums = [2, 3, 6, 7], target = 7
    Output: [[2, 2, 3], [7]]
    Why:    2 + 2 + 3 and 7 on its own; 3 + 2 + 2 is the same group

    Input:  nums = [2], target = 4
    Output: [[2, 2]]
    Why:    the same number may be reused

    Input:  nums = [3, 5], target = 4
    Output: []
    Why:    edge case, no combination of 3 and 5 lands on 4

Approach:
    Recurse with a start index so a branch never revisits earlier values,
    which is what stops a group being reported in several orders. The
    remaining target shrinks on the way down, and hitting zero records a
    copy of the path. Sorting first turns the impossible branches into a
    single break: once a value is larger than what is left, so is every
    value after it. Time is exponential in the worst case, bounded by the
    number of valid groups times the target divided by the smallest value;
    recursion depth is that same ratio.

The lesson behind it: Subsets
    https://bytepatterns.com/learn/backtracking/subsets
    python backtracking/02-subsets.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/backtracking/combinations-summing-to-target

Run it:  python problems/backtracking/02-combinations-summing-to-target.py
"""


def combos(nums, target):
    out = []
    nums.sort()
    def build(start, left, path):
        if left == 0:                        # target hit exactly
            out.append(path[:])
            return
        for i in range(start, len(nums)):
            if nums[i] > left:               # sorted, so nothing later fits
                break
            path.append(nums[i])
            build(i, left - nums[i], path)   # i, not i+1: a value may repeat
            path.pop()
    build(0, target, [])
    return out


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(combos([2, 3, 6, 7], 7), [[2, 2, 3], [7]])
    check(combos([2], 4), [[2, 2]])
    check(combos([3, 5], 4), [])
