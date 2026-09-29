"""
Longest Distinct Run (medium) · patterns: sliding-window, hash-map

Given a list of values, find the length of the longest contiguous stretch in
which no value repeats. The stretch has to stay in one unbroken run, so you
cannot skip over an element to avoid a repeat. Return 0 when the list is
empty.

Examples:

    Input:  items = [1, 2, 3, 2, 4, 5]
    Output: 4
    Why:    the run 3, 2, 4, 5 has no repeats

    Input:  items = [7, 7, 7]
    Output: 1
    Why:    every pair repeats, so a run of one is the best possible

    Input:  items = []
    Output: 0
    Why:    edge case, there is no run at all

Approach:
    A window bounded by two indexes slides right while a map remembers where
    each value most recently appeared. When the incoming value already lives
    inside the window, the left edge jumps just past the earlier copy so the
    window stays repeat-free. Each element is visited once and the map
    lookups are constant time. Time is O(n), and space is O(d) where d is
    the number of distinct values.

The lesson behind it: Longest Unique Substring
    https://bytepatterns.com/learn/strings/longest-substring-without-repeats
    python strings/04-longest-substring-without-repeats.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/arrays/longest-distinct-run

Run it:  python problems/arrays/04-longest-distinct-run.py
"""


def longest_distinct_run(items):
    last_seen = {}                   # value -> most recent position
    start = 0                        # left edge of the current window
    best = 0
    for i, x in enumerate(items):
        # a repeat inside the window drags the left edge past the old copy
        if x in last_seen and last_seen[x] >= start:
            start = last_seen[x] + 1
        last_seen[x] = i
        best = max(best, i - start + 1)
    return best


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(longest_distinct_run([1, 2, 3, 2, 4, 5]), 4)
    check(longest_distinct_run([7, 7, 7]), 1)
    check(longest_distinct_run([]), 0)
