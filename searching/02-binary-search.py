"""
Binary Search: A million records, twenty guesses. Sorted data only.

On sorted data, compare the target with the middle element and throw away
the half that cannot contain it. Repeat until one candidate remains. That
halving gives you O(log n).

Lesson 2 of Searching, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/searching/binary-search

Short video on this lesson: https://www.youtube.com/@bytepatterns

Run it:  python searching/02-binary-search.py
"""


def binary_search(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            lo = mid + 1      # target must be in the right half
        else:
            hi = mid - 1      # target must be in the left half
    return -1


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(binary_search([2, 5, 8, 12, 16, 23], 16), 4)
