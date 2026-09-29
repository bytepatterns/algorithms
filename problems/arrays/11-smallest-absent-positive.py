"""
Smallest Absent Positive (hard) · patterns: cyclic-sort, index-as-home

A ticket machine hands out the smallest positive ticket number that is not
already taken. Given an unsorted list of whole numbers, which may include
zero, negatives, duplicates and values far larger than the list, return the
smallest positive whole number missing from it. Use O(n) time and only
constant extra memory, rearranging the list itself if that helps.

Examples:

    Input:  nums = [5, 3, -1, 1, 2]
    Output: 4
    Why:    1, 2 and 3 are all present, and 4 is not

    Input:  nums = [2, 2, 90]
    Output: 1
    Why:    1 is missing, whatever else the list holds

    Input:  nums = []
    Output: 1
    Why:    edge case, nothing is taken yet

Approach:
    With n slots, the missing positive is at most n + 1, so only the values
    1 to n matter and each has a home index. Cyclic sort sends every such
    value home with swaps, and each swap settles one value for good, so the
    total number of swaps is at most n even though a while loop sits inside
    the for loop. Checking that the home does not already hold the same
    value stops duplicates from swapping forever. After that, the first slot
    holding the wrong value names the answer. Time is O(n), and space is
    O(1) beyond the input list.

The lesson behind it: Cyclic Sort
    https://bytepatterns.com/learn/arrays/cyclic-sort
    python arrays/09-cyclic-sort.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/arrays/smallest-absent-positive

Run it:  python problems/arrays/11-smallest-absent-positive.py
"""


def first_missing(nums):
    n = len(nums)
    for i in range(n):
        # send nums[i] home while it belongs somewhere and home is not settled
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            j = nums[i] - 1
            nums[i], nums[j] = nums[j], nums[i]
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1             # the first slot without its own value
    return n + 1                     # 1..n are all present


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(first_missing([5, 3, -1, 1, 2]), 4)
    check(first_missing([2, 2, 90]), 1)
    check(first_missing([]), 1)
