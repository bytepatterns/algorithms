"""
Insert and Merge a Span (medium) · patterns: intervals, merge

A calendar stores busy spans as [start, end] pairs, sorted by start and
never overlapping or touching. A new busy span arrives. Add it and return
the updated list, still sorted and without overlaps, merging any spans that
now overlap or share an endpoint. The list may be empty, and every span has
start no greater than end.

Examples:

    Input:  spans = [[1, 2], [4, 6], [9, 10]], new = [5, 9]
    Output: [[1, 2], [4, 10]]
    Why:    [5, 9] overlaps [4, 6] and touches [9, 10], so all three merge

    Input:  spans = [[1, 2], [5, 6]], new = [3, 4]
    Output: [[1, 2], [3, 4], [5, 6]]
    Why:    the new span fits in the gap

    Input:  spans = [], new = [2, 3]
    Output: [[2, 3]]
    Why:    edge case, an empty calendar

Approach:
    Because the stored spans are sorted and disjoint, the ones that end
    before the new span begins are untouched and come first, and the ones
    that begin after it ends are untouched and come last. Everything in
    between overlaps or touches the new span, so those spans are absorbed by
    stretching its start down and its end up. One left-to-right pass handles
    all three runs. Time is O(n) and space is O(n) for the output.

The lesson behind it: Insert Interval
    https://bytepatterns.com/learn/intervals/insert-interval
    python intervals/03-insert-interval.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/intervals/insert-and-merge-span

Run it:  python problems/intervals/07-insert-and-merge-span.py
"""


def insert_span(spans, new):
    merged, (lo, hi) = [], new
    i, n = 0, len(spans)
    while i < n and spans[i][1] < lo:        # ends before the new span starts
        merged.append(spans[i]); i += 1
    while i < n and spans[i][0] <= hi:       # overlaps or touches: absorb it
        lo, hi = min(lo, spans[i][0]), max(hi, spans[i][1]); i += 1
    merged.append([lo, hi])
    return merged + spans[i:]                # the rest start after the new end


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(insert_span([[1, 2], [4, 6], [9, 10]], [5, 9]), [[1, 2], [4, 10]])
    check(insert_span([[1, 2], [5, 6]], [3, 4]), [[1, 2], [3, 4], [5, 6]])
    check(insert_span([], [2, 3]), [[2, 3]])
