"""
Nesting Envelopes (hard) · patterns: binary-search, patience-sorting, sorting

Each envelope is given as [width, height]. One envelope fits inside another
only when it is strictly narrower and strictly shorter; rotating is not
allowed. Return the largest number of envelopes you can nest one inside the
next. The list may hold up to 100,000 envelopes, so a quadratic comparison
of every pair is too slow.

Examples:

    Input:  envelopes = [[4, 5], [4, 6], [6, 7], [2, 3], [1, 1]]
    Output: 4
    Why:    [1, 1] inside [2, 3] inside [4, 5] inside [6, 7]

    Input:  envelopes = [[3, 3], [3, 3]]
    Output: 1
    Why:    identical envelopes cannot hold each other

    Input:  envelopes = []
    Output: 0
    Why:    edge case, nothing to nest

Approach:
    Sorting by width leaves only heights to compare, except that equal
    widths must not chain, so ties are sorted by height descending, which
    makes two of them impossible in one strictly rising run. The answer is
    then the longest strictly rising subsequence of the heights. The
    patience method keeps tails, where tails[k] is the smallest height that
    can finish a nest of length k + 1; each height replaces the first tail
    that is not smaller, found by binary search, or extends the list. Time
    is O(n log n) and space is O(n).

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/dynamic-programming/nesting-envelopes

Run it:  python problems/dynamic-programming/13-nesting-envelopes.py
"""


from bisect import bisect_left
def max_nesting(envelopes):
    # equal widths cannot nest, so the tallest of them goes first
    order = sorted(envelopes, key=lambda e: (e[0], -e[1]))
    tails = []                 # tails[k] = smallest last height of a nest of k + 1
    for _, h in order:
        k = bisect_left(tails, h)          # first tail that is not smaller than h
        if k == len(tails):
            tails.append(h)                # h extends the longest nest
        else:
            tails[k] = h                   # same length, lower finish
    return len(tails)


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(max_nesting([[4, 5], [4, 6], [6, 7], [2, 3], [1, 1]]), 4)
    check(max_nesting([[3, 3], [3, 3]]), 1)
    check(max_nesting([]), 0)
