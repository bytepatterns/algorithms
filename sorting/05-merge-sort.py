"""
Merge Sort: Split until trivial, then merge your way back up.

Split the array in half, sort each half recursively, then merge the two
sorted halves in a single pass. The splitting is log n levels deep and every
level costs O(n), so you get O(n log n) every single time.

Lesson 5 of Sorting, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/sorting/merge-sort

Run it:  python sorting/05-merge-sort.py
"""


def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left = merge_sort(nums[:mid])       # sort each half
    right = merge_sort(nums[mid:])
    out, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:         # <= is what keeps it stable
            out.append(left[i]); i += 1
        else:
            out.append(right[j]); j += 1
    return out + left[i:] + right[j:]   # drain the leftovers


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(merge_sort([5, 2, 9, 1]), [1, 2, 5, 9])
