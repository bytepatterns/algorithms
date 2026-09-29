"""
Search a List of Unknown Length (medium) · patterns: binary-search, exponential-search

A sorted list of numbers, smallest first and possibly with repeats, is
hidden behind a reader. The only way to look at it is reader.get(i), which
returns the value at index i, or None once i is past the end; the length is
never given. Return the first index that holds the target, or -1 if the
target is absent, using a number of reads that grows only with the logarithm
of that index.

Examples:

    Input:  values = [2, 5, 5, 9, 14, 20, 31], target = 9
    Output: 3
    Why:    9 sits at index 3

    Input:  values = [2, 5, 5, 9, 14, 20, 31], target = 5
    Output: 1
    Why:    5 appears twice, and the first copy is at index 1

    Input:  values = [], target = 1
    Output: -1
    Why:    edge case, the very first read already returns None

Approach:
    The question is where values stop being smaller than the target, and
    past-the-end reads count as too big, so a read gives a yes-or-no answer
    that flips only once along the list. Doubling a bound finds the flip
    within a range whose size is about the answer's index, using a
    logarithmic number of reads, and a binary search inside that range finds
    the exact first index with another logarithmic number. The value there
    is the target only if the target exists. Time is O(log p) reads for an
    answer at index p, and space is O(1).

The lesson behind it: O(log n) and Halving
    https://bytepatterns.com/learn/big-o/ologn-halving
    python big-o/04-ologn-halving.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/searching/search-a-list-of-unknown-length

Run it:  python problems/searching/08-search-a-list-of-unknown-length.py
"""


class Reader:
    def __init__(self, values):
        self.values = values
    def get(self, i):
        return self.values[i] if 0 <= i < len(self.values) else None

def find_first(reader, target):
    def at_or_past(i):                   # value >= target, or past the end
        v = reader.get(i)
        return v is None or v >= target
    bound = 1
    while not at_or_past(bound - 1):     # probe 0, 1, 3, 7, 15, ...
        bound *= 2
    lo, hi = bound // 2, bound - 1       # the first yes lies in lo..hi
    while lo < hi:
        mid = (lo + hi) // 2
        if at_or_past(mid): hi = mid
        else: lo = mid + 1
    return lo if reader.get(lo) == target else -1


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(find_first(Reader([2, 5, 5, 9, 14, 20, 31]), 9), 3)
    check(find_first(Reader([2, 5, 5, 9, 14, 20, 31]), 5), 1)
    check(find_first(Reader([]), 1), -1)
