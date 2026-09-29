"""
Fewest Removals to Unclash (medium) · patterns: greedy, interval-scheduling, sorting

You are given a list of spans, each written as a start and an end, where the
end is always larger than the start. Two spans clash when one begins
strictly before the other finishes; touching at a single point is fine.
Remove as few spans as possible so that nothing left clashes, and return how
many you removed.

Examples:

    Input:  spans = [(1, 2), (2, 3), (3, 4), (1, 3)]
    Output: 1
    Why:    dropping (1, 3) leaves three spans that only touch at their ends

    Input:  spans = [(1, 2), (1, 2), (1, 2)]
    Output: 2
    Why:    three identical spans all clash, so only one can survive

    Input:  spans = [(1, 2), (2, 3)]
    Output: 0
    Why:    edge case, touching at a point is not a clash so nothing is removed

Approach:
    Maximising the kept spans is the classic interval-scheduling greedy, and
    the removals fall out as the leftover. Sorting by end time makes the
    first survivor the one that frees the timeline soonest, and an exchange
    argument shows swapping it into any optimal set never makes that set
    worse. One linear pass then keeps every span whose start clears the last
    kept end. Time is O(n log n) for the sort plus O(n) for the walk, and
    space is O(1) beyond the sort.

The lesson behind it: Interval Scheduling
    https://bytepatterns.com/learn/greedy/interval-scheduling
    python greedy/02-interval-scheduling.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/greedy/fewest-removals-to-unclash

Run it:  python problems/greedy/01-fewest-removals-to-unclash.py
"""


def fewest_removals(spans):
    spans.sort(key=lambda s: s[1])      # earliest finishing first
    kept, last_end = 0, float("-inf")
    for s, e in spans:
        if s >= last_end:               # fits after everything kept so far
            kept += 1
            last_end = e
    return len(spans) - kept


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(fewest_removals([(1, 2), (2, 3), (3, 4), (1, 3)]), 1)
    check(fewest_removals([(1, 2), (1, 2), (1, 2)]), 2)
    check(fewest_removals([(1, 2), (2, 3)]), 0)
