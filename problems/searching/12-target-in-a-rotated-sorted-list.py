"""
Target in a Rotated Sorted List (medium) · patterns: binary-search, rotated-array

A list of distinct integers was sorted in ascending order and then rotated
at an unknown point, so [0, 1, 2, 4, 5, 6, 7] might have become [4, 5, 6, 7,
0, 1, 2]. Given the rotated list and a target, return the index of the
target, or -1 if it is not there. The search must run in O(log n) time.

Examples:

    Input:  nums = [4, 5, 6, 7, 0, 1, 2], target = 0
    Output: 4

    Input:  nums = [4, 5, 6, 7, 0, 1, 2], target = 3
    Output: -1
    Why:    3 would sit between 2 and 4, and neither side of the rotation holds it

    Input:  nums = [3, 1], target = 1
    Output: 1
    Why:    edge case, with two values the middle index is the first one and the left half has one element

Approach:
    A plain binary search fails here because one comparison with the middle
    no longer says which half holds the target. What still holds is that
    cutting a rotated list anywhere leaves at least one half in normal
    sorted order, and nums[lo] <= nums[mid] tells you which one. For a
    sorted half, checking the target against its two ends answers "is it in
    here" exactly; if the answer is no, the target can only be in the other
    half, rotation and all. Each step still throws away half of the range,
    so time is O(log n) and space is O(1). The distinct values matter: with
    repeats, nums[lo] == nums[mid] no longer says which half is sorted and
    the worst case drops to O(n).

The lesson behind it: Search in Rotated Array
    https://bytepatterns.com/learn/searching/search-in-rotated-array
    python searching/04-search-in-rotated-array.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/searching/target-in-a-rotated-sorted-list

Run it:  python problems/searching/12-target-in-a-rotated-sorted-list.py
"""


def search_rotated(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[lo] <= nums[mid]:                  # left half lo..mid is sorted
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:                                      # right half mid..hi is sorted
            if nums[mid] < target <= nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(search_rotated([4, 5, 6, 7, 0, 1, 2], 0), 4)
    check(search_rotated([4, 5, 6, 7, 0, 1, 2], 3), -1)
    check(search_rotated([3, 1], 1), 1)
