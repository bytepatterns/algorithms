"""
Quick Sort: Pick a pivot, split around it, and never merge.

Choose a pivot and partition the array into a smaller group and a larger
group, then sort each group the same way. A good pivot gives O(n log n); a
terrible one degrades to O(n²). Random or median-of-three pivots keep that
rare.

Lesson 6 of Sorting, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/sorting/quick-sort

Short video on this lesson: https://www.youtube.com/@bytepatterns

Run it:  python sorting/06-quick-sort.py
"""


def quick_sort(nums):
    if len(nums) <= 1:
        return nums
    pivot = nums[len(nums) // 2]        # middle element as pivot
    smaller = [x for x in nums if x < pivot]
    equal   = [x for x in nums if x == pivot]
    larger  = [x for x in nums if x > pivot]
    # sort the two sides; the equal group is already in place
    return quick_sort(smaller) + equal + quick_sort(larger)


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(quick_sort([8, 3, 8, 1, 5]), [1, 3, 5, 8, 8])
