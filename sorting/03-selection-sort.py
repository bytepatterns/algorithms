"""
Selection Sort: Find the smallest, put it in front, then do it again.

Scan the unsorted part for its smallest value and swap it into the next
position. Each round locks one element into its final home. Comparisons are
always O(n²), but there are at most n swaps.

Lesson 3 of Sorting, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/sorting/selection-sort

Short video on this lesson: https://www.youtube.com/@bytepatterns

Run it:  python sorting/03-selection-sort.py
"""


def selection_sort(nums):
    n = len(nums)
    for i in range(n):
        smallest = i
        for j in range(i + 1, n):       # scan the unsorted tail
            if nums[j] < nums[smallest]:
                smallest = j
        # one swap per round, at most n swaps in total
        nums[i], nums[smallest] = nums[smallest], nums[i]
    return nums


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(selection_sort([64, 25, 12, 22]), [12, 22, 25, 64])
