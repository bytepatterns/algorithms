"""
Overlap of Two Span Lists (medium) · patterns: intervals, two-pointers

Two people share their free time as lists of closed spans [start, end]. Each
list is sorted by start, and the spans within one list never overlap. Return
the spans when both are free, sorted by start. A span that shrinks to a
single point, such as [5, 5], still counts.

Examples:

    Input:  a = [[0, 2], [5, 10], [13, 23], [24, 25]], b = [[1, 5], [8, 12], [15, 24], [25, 26]]
    Output: [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]

    Input:  a = [[1, 7]], b = [[3, 10]]
    Output: [[3, 7]]
    Why:    the overlap starts at the later start and ends at the earlier end

    Input:  a = [[1, 3], [5, 9]], b = []
    Output: []
    Why:    edge case, one person is never free

Approach:
    Two closed spans overlap on [max of starts, min of ends] whenever that
    start is not after that end. Both lists are sorted and internally
    disjoint, so a two-pointer walk suffices: after comparing the current
    pair, the span that ends first has no future partner in the other list,
    since every later span there starts after the current one, and it can be
    dropped. The other span stays, because it may still overlap the next
    span of the first list. Each step drops one span, so time is O(m plus n)
    and space is O(1) beyond the output.

The lesson behind it: Merge Intervals
    https://bytepatterns.com/learn/intervals/merge-intervals
    python intervals/02-merge-intervals.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/intervals/overlap-of-two-span-lists

Run it:  python problems/intervals/08-overlap-of-two-span-lists.py
"""


def overlaps(a, b):
    out, i, j = [], 0, 0
    while i < len(a) and j < len(b):
        lo = max(a[i][0], b[j][0])
        hi = min(a[i][1], b[j][1])
        if lo <= hi:
            out.append([lo, hi])               # they share [lo, hi]
        if a[i][1] < b[j][1]:
            i += 1                             # a's span is finished
        else:
            j += 1
    return out


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(overlaps([[0, 2], [5, 10], [13, 23]], [[1, 5], [8, 12], [15, 24]]), [[1, 2], [5, 5], [8, 10], [15, 23]])
    check(overlaps([[1, 7]], [[3, 10]]), [[3, 7]])
    check(overlaps([[1, 3], [5, 9]], []), [])
