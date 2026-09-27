"""
Peak In Bumpy List (medium) · patterns: binary-search, slope-following

A peak is a position whose value is greater than both of its neighbours,
where a missing neighbour off either end counts as smaller than anything.
Given a non-empty list in which no two neighbouring values are equal, return
the position of any peak. The list is not sorted, and several peaks may
exist.

Examples:

    Input:  nums = [1, 2, 3, 1]
    Output: 2
    Why:    the value 3 stands above both of its neighbours

    Input:  nums = [1, 2, 1, 3, 5, 6, 4]
    Output: 5
    Why:    position 1 is also a peak, and either answer is acceptable

    Input:  nums = [1]
    Output: 0
    Why:    edge case, a lone value has two imaginary smaller neighbours

Approach:
    A single comparison between neighbours settles which half must contain a
    peak: an upward slope guarantees one to the right, since the values
    either keep rising into the end or turn over first, and a downward slope
    guarantees one at or to the left of the middle. That invariant lets the
    range halve each round even though the list is unsorted. The range
    shrinks to exactly one position, which is therefore a peak. Time is
    O(log n), and space is O(1).

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/searching/peak-in-bumpy-list

Run it:  python problems/searching/02-peak-in-bumpy-list.py
"""


def find_peak(nums):
    low, high = 0, len(nums) - 1     # this range always contains a peak
    while low < high:
        mid = (low + high) // 2
        if nums[mid] < nums[mid + 1]:
            low = mid + 1            # rising, so a peak lies strictly to the right
        else:
            high = mid               # falling, and mid may be the peak itself
    return low


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(find_peak([1, 2, 3, 1]), 2)
    check(find_peak([1, 2, 1, 3, 5, 6, 4]), 5)
    check(find_peak([1]), 0)
