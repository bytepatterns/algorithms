"""
Non Overlapping Removals (medium) · patterns: intervals, greedy

Given a list of intervals [start, finish], return the smallest number of
them you must remove so that none of the survivors overlap. Intervals that
only touch at an endpoint — one finishing exactly where the next starts — do
not count as overlapping.

Examples:

    Input:  intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
    Output: 1
    Why:    dropping [1, 3] leaves three intervals that only touch at endpoints

    Input:  intervals = [[1, 2], [1, 2], [1, 2]]
    Output: 2
    Why:    all three cover the same span, so only one can stay

    Input:  intervals = []
    Output: 0
    Why:    edge case, nothing to remove

Approach:
    Sorting by finish time makes the greedy choice safe: among any set of
    mutually overlapping intervals, the one ending soonest blocks the least
    future room, so keeping it is never worse than keeping another. One
    sweep then keeps every interval whose start clears the last kept finish,
    and the removals are whatever is left over. Sorting dominates at O(n log
    n) time, with O(1) extra space beyond the sort.

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/intervals/non-overlapping-removals

Run it:  python problems/intervals/01-non-overlapping-removals.py
"""


def min_removals(intervals):
    if not intervals:
        return 0
    intervals.sort(key=lambda p: p[1])        # earliest finisher first
    kept, end = 1, intervals[0][1]
    for start, finish in intervals[1:]:
        if start >= end:                      # touching is not overlapping
            kept += 1
            end = finish
    return len(intervals) - kept


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(min_removals([[1, 2], [2, 3], [3, 4], [1, 3]]), 1)
    check(min_removals([[1, 2], [1, 2], [1, 2]]), 2)
    check(min_removals([]), 0)
