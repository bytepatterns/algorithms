"""
Cyclic Sort: When values are 1..n, every value already knows its index.

When an array holds the numbers 1 to n in some order, each value already
knows where it belongs: value v goes to index v-1. So walk the array, and
whenever the value under the cursor is not home, swap it straight there.
Keep swapping until the current slot is settled, then step forward. Every
swap parks one value permanently, so the whole thing is one linear pass —
and it finds missing or duplicated numbers for free.

Lesson 9 of Arrays, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/arrays/cyclic-sort

Run it:  python arrays/09-cyclic-sort.py
"""


def cyclic_sort(nums):
    i = 0
    while i < len(nums):
        home = nums[i] - 1          # value v belongs at index v-1
        if nums[i] != nums[home]:   # not home yet -> send it there
            nums[i], nums[home] = nums[home], nums[i]
        else:
            i += 1                  # settled, move the cursor on
    return nums


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(cyclic_sort([3, 1, 5, 4, 2]), [1, 2, 3, 4, 5])
