"""
Find a Peak: An uphill step always has a summit ahead of it.

A peak is any index at least as high as its neighbours, and an unsorted
array still has one. Compare mid with the element just right of it. If the
ground rises, a peak must lie to the right: the values either climb to the
edge or turn over on the way. If it falls, mid itself may be the peak, so
keep it. Each test halves the range and still lands on a real peak.

Lesson 7 of Searching, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/searching/find-peak-element

Run it:  python searching/07-find-peak-element.py
"""


def find_peak(nums):
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] < nums[mid + 1]:
            lo = mid + 1     # uphill: a peak sits to the right
        else:
            hi = mid         # downhill: mid may be the peak itself
    return lo                # lo == hi, and that index is a peak


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(find_peak([1, 3, 6, 4, 2]), 2)
