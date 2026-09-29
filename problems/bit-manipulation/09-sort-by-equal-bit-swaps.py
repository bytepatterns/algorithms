"""
Sort by Equal-Bit Swaps (medium) · patterns: popcount, adjacent-swaps

You may swap two neighbouring elements of a list, as often as you like, but
only when both have the same number of 1 bits in binary. Given a list of
non-negative whole numbers, return True if these swaps can sort it into
ascending order, and False otherwise.

Examples:

    Input:  nums = [6, 5, 3, 16, 8, 31]
    Output: True
    Why:    6, 5, 3 all have two 1 bits and sort to 3, 5, 6; 16 and 8 have one and sort to 8, 16

    Input:  nums = [6, 3, 1, 4, 2]
    Output: False
    Why:    6 has two 1 bits, 1 has one, so 1 can never get past 6

    Input:  nums = [7]
    Output: True
    Why:    edge case, a single value is already sorted

Approach:
    Two neighbours with different bit counts can never swap, so the
    boundaries between runs of equal bit count never move and every value
    stays inside its run. Within a run, neighbour swaps can reach any order,
    just as bubble sort sorts with nothing else, so each run can end up
    sorted. The whole list is then sorted exactly when the runs fit
    together, which means no run holds a value smaller than the largest
    value of the run before it. Time is O(n log m) for n values up to m,
    since counting bits takes O(log m) each, and space is O(1).

The lesson behind it: Bubble Sort
    https://bytepatterns.com/learn/sorting/bubble-sort
    python sorting/02-bubble-sort.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/bit-manipulation/sort-by-equal-bit-swaps

Run it:  python problems/bit-manipulation/09-sort-by-equal-bit-swaps.py
"""


def can_sort(nums):
    prev_max = -1                    # largest value in the runs already checked
    i = 0
    while i < len(nums):
        bits = bin(nums[i]).count("1")
        lo = hi = nums[i]
        j = i
        while j < len(nums) and bin(nums[j]).count("1") == bits:
            lo, hi = min(lo, nums[j]), max(hi, nums[j])   # one run of equal bit count
            j += 1
        if lo < prev_max:            # this run's smallest can never pass the earlier maximum
            return False
        prev_max, i = hi, j
    return True


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(can_sort([6, 5, 3, 16, 8, 31]), True)
    check(can_sort([6, 3, 1, 4, 2]), False)
    check(can_sort([7]), True)
