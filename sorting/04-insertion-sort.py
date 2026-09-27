"""
Insertion Sort: Build a sorted run, slide each newcomer into place.

Treat the left side as already sorted and pick up the next element. Shift
the bigger values one slot right until a gap opens, then drop it in.
Generally O(n²), but close to O(n) on nearly sorted data.

Lesson 4 of Sorting, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/sorting/insertion-sort

Short video on this lesson: https://www.youtube.com/@bytepatterns

Run it:  python sorting/04-insertion-sort.py
"""


def insertion_sort(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        # slide bigger values one slot to the right
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key      # drop key into the gap
    return nums


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(insertion_sort([7, 3, 9, 3]), [3, 3, 7, 9])
