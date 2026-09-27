"""
Bubble Sort: Swap neighbours until the big values float to the end.

Compare each adjacent pair and swap them when they are out of order. After
one pass the largest value has bubbled all the way to the end. Repeat, and
the sorted region grows from the right, all at a cost of O(n²).

Lesson 2 of Sorting, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/sorting/bubble-sort

Short video on this lesson: https://www.youtube.com/@bytepatterns

Run it:  python sorting/02-bubble-sort.py
"""


def bubble_sort(nums):
    n = len(nums)
    for end in range(n - 1, 0, -1):
        swapped = False
        for i in range(end):
            if nums[i] > nums[i + 1]:          # out of order?
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
        if not swapped:                        # already sorted
            return nums
    return nums


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(bubble_sort([5, 1, 4, 2]), [1, 2, 4, 5])
