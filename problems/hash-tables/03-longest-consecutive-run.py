"""
Longest Consecutive Run (medium) · patterns: hash-set, counting

Given an unsorted list of integers, find the length of the longest group of
numbers that could be lined up as consecutive values with no gaps. The
numbers do not have to be adjacent in the list, and duplicates count only
once. Aim for a solution that does not sort the input.

Examples:

    Input:  nums = [9, 4, 2, 3, 1, 8]
    Output: 4
    Why:    1, 2, 3 and 4 form an unbroken chain

    Input:  nums = [5, 5, 5]
    Output: 1
    Why:    duplicates add nothing, the chain is just the value 5

    Input:  nums = []
    Output: 0
    Why:    edge case, there is no chain to measure

Approach:
    Loading the values into a set turns each chain step into a constant-time
    membership test, and dropping duplicates for free. Counting starts only
    at values whose predecessor is absent, which means each chain is walked
    exactly once from its head rather than once per member. That guard is
    what keeps the nested loop linear overall. Time is O(n) on average, and
    space is O(n) for the set.

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/hash-tables/longest-consecutive-run

Run it:  python problems/hash-tables/03-longest-consecutive-run.py
"""


def longest_consecutive_run(nums):
    pool = set(nums)                 # duplicates collapse, lookups are cheap
    best = 0
    for x in pool:
        if x - 1 in pool:            # only count starting from a chain head
            continue
        length = 1
        while x + length in pool:    # walk the chain upward
            length += 1
        best = max(best, length)
    return best


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(longest_consecutive_run([9, 4, 2, 3, 1, 8]), 4)
    check(longest_consecutive_run([5, 5, 5]), 1)
    check(longest_consecutive_run([]), 0)
