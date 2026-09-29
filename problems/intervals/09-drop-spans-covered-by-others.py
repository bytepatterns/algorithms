"""
Drop Spans Covered by Others (medium) · patterns: intervals, sort-by-start

A monitoring system has a list of alert windows [start, end]. A window is
redundant when another window in the list covers it completely, meaning the
other one starts no later and ends no earlier. Remove every redundant window
and return how many remain. No two windows in the list are identical.

Examples:

    Input:  spans = [[1, 4], [3, 6], [2, 8]]
    Output: 2
    Why:    [3, 6] lies inside [2, 8]; [1, 4] and [2, 8] only overlap

    Input:  spans = [[1, 2], [1, 4], [3, 4]]
    Output: 1
    Why:    [1, 4] covers both others, including the two that share an endpoint with it

    Input:  spans = [[3, 5]]
    Output: 1
    Why:    edge case, a lone window has nothing to cover it

Approach:
    After sorting by start ascending and, for ties, by end descending, every
    window that starts no later than the current one comes before it, and
    among windows with the same start the longest comes first. The current
    window is then covered exactly when some earlier window reaches at least
    as far, which is a single comparison against the furthest end seen so
    far. The tie-break matters: without it, [1, 2] would be seen before [1,
    4] and wrongly kept. Time is O(n log n) for the sort and space is O(n)
    for the sorted copy.

The lesson behind it: Interval Basics & Sorting
    https://bytepatterns.com/learn/intervals/interval-basics-and-sorting
    python intervals/01-interval-basics-and-sorting.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/intervals/drop-spans-covered-by-others

Run it:  python problems/intervals/09-drop-spans-covered-by-others.py
"""


def uncovered_count(spans):
    spans = sorted(spans, key=lambda s: (s[0], -s[1]))  # longer first on ties
    kept, reach = 0, float("-inf")
    for start, end in spans:
        if end > reach:                        # nothing earlier covers it
            kept += 1
            reach = end
    return kept


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(uncovered_count([[1, 4], [3, 6], [2, 8]]), 2)
    check(uncovered_count([[1, 2], [1, 4], [3, 4]]), 1)
    check(uncovered_count([[3, 5]]), 1)
    check(uncovered_count([[1, 4], [2, 3]]), 1)
