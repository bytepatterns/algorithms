"""
Pairs With the Smallest Gap (easy) · patterns: sort-first, adjacent-scan

A timing service logs event timestamps and wants the pairs of events that
happened closest together. Given a list of at least two distinct integers,
find the smallest absolute difference between any two of them and return
every pair [a, b] with a < b that has that difference, listed in ascending
order of a. The list has up to 100,000 values, so checking every pair is too
slow.

Examples:

    Input:  nums = [4, 2, 1, 3]
    Output: [[1, 2], [2, 3], [3, 4]]
    Why:    the smallest gap is 1, and three pairs have it

    Input:  nums = [3, 8, -10, 23, 19, -4, -14, 27]
    Output: [[-14, -10], [19, 23], [23, 27]]

    Input:  nums = [1, 3, 6, 10, 15]
    Output: [[1, 3]]
    Why:    edge case, only one pair has the smallest gap

Approach:
    Sorting is the right tool whenever a question is about values that are
    close together, because it puts close values next to each other. In a
    sorted list the gap between a value and any later value is at least the
    gap to its immediate neighbour, so only the n - 1 neighbouring pairs
    need checking. One scan finds the smallest gap and a second collects the
    pairs that have it, already in ascending order. Sorting dominates, so
    time is O(n log n), and extra space is O(n) for the sorted copy and the
    answer.

The lesson behind it: Which Sort When?
    https://bytepatterns.com/learn/sorting/which-sort-when
    python sorting/08-which-sort-when.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/sorting/pairs-with-the-smallest-gap

Run it:  python problems/sorting/15-pairs-with-the-smallest-gap.py
"""


def smallest_gap_pairs(nums):
    s = sorted(nums)
    best = min(b - a for a, b in zip(s, s[1:]))           # only neighbours can win
    return [[a, b] for a, b in zip(s, s[1:]) if b - a == best]


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(smallest_gap_pairs([4, 2, 1, 3]), [[1, 2], [2, 3], [3, 4]])
    check(smallest_gap_pairs([3, 8, -10, 23, 19, -4, -14, 27]), [[-14, -10], [19, 23], [23, 27]])
    check(smallest_gap_pairs([1, 3, 6, 10, 15]), [[1, 3]])
