"""
Search in Rotated Array: Half of it is still sorted. Find that half, use it.

A sorted array that has been rotated still has one fully sorted half at
every split. Work out which side is in order, then check whether the target
falls inside it. Binary search survives intact, still O(log n).

Lesson 4 of Searching, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/searching/search-in-rotated-array

Run it:  python searching/04-search-in-rotated-array.py
"""


def search_rotated(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[lo] <= nums[mid]:              # left half is sorted
            if nums[lo] <= target < nums[mid]: hi = mid - 1
            else:                              lo = mid + 1
        else:                                  # right half is sorted
            if nums[mid] < target <= nums[hi]: lo = mid + 1
            else:                              hi = mid - 1
    return -1


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(search_rotated([6, 7, 9, 1, 2, 4], 2), 4)
