"""
Insertion Sort Shift Count (easy) · patterns: insertion-sort, stable-sort

Insertion sort places each new value by sliding every larger value in the
sorted part one slot to the right. Given a list of numbers, return how many
single-slot slides insertion sort performs while sorting it into ascending
order. Equal values never slide past each other, and the input list must not
be modified.

Examples:

    Input:  nums = [3, 1, 2]
    Output: 2
    Why:    placing 1 slides 3 once, then placing 2 slides 3 once more

    Input:  nums = [5, 4, 3, 2, 1]
    Output: 10
    Why:    each new value slides every value already placed

    Input:  nums = [2, 2, 2]
    Output: 0
    Why:    edge case, equal values stay where they are

Approach:
    Running insertion sort on a copy and counting inside its inner loop
    answers the question exactly, because every slide is one execution of
    that loop body. The comparison must be strictly greater than, which is
    what keeps equal values from sliding and keeps the sort stable. Each
    slide also fixes one pair of values that appeared in the wrong order,
    which is why a reversed list costs the most. Time is O(n²) in the worst
    case and O(n) on a list that is already sorted, and space is O(n) for
    the copy.

The lesson behind it: Insertion Sort
    https://bytepatterns.com/learn/sorting/insertion-sort
    python sorting/04-insertion-sort.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/sorting/insertion-sort-shift-count

Run it:  python problems/sorting/06-insertion-sort-shift-count.py
"""


def count_shifts(nums):
    a = list(nums)                   # sort a copy, leave the input alone
    shifts = 0
    for i in range(1, len(a)):
        cur, j = a[i], i - 1
        while j >= 0 and a[j] > cur:  # only strictly larger values make room
            a[j + 1] = a[j]
            shifts += 1
            j -= 1
        a[j + 1] = cur               # drop the held value into the gap
    return shifts


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(count_shifts([3, 1, 2]), 2)
    check(count_shifts([5, 4, 3, 2, 1]), 10)
    check(count_shifts([2, 2, 2]), 0)
