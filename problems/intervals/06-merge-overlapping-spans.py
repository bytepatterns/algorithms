"""
Merge Overlapping Spans (medium) · patterns: intervals, sorting, merge

You are given closed spans [start, end] in any order. Combine every group of
spans that overlap into a single span covering the whole group, and return
the result sorted by start. Spans that share even a single point, such as
[1, 4] and [4, 5], count as overlapping.

Examples:

    Input:  spans = [[1, 3], [8, 10], [2, 6], [15, 18]]
    Output: [[1, 6], [8, 10], [15, 18]]
    Why:    [1, 3] and [2, 6] overlap; the others stand alone

    Input:  spans = [[1, 10], [2, 3], [4, 5]]
    Output: [[1, 10]]
    Why:    spans sitting entirely inside another disappear into it

    Input:  spans = [[5, 7]]
    Output: [[5, 7]]
    Why:    edge case, a single span has nothing to merge with

Approach:
    Sorting by start guarantees that once a span begins after the current
    block's end, no later span can reach back into that block, because every
    later span starts even further right. So the sweep only ever compares
    against the last block in the output: overlap extends it, a gap opens a
    new one. Taking the maximum of the two ends is what handles a span
    nested entirely inside the block, which would otherwise shrink it. Time
    is O(n log n) for the sort and O(n) for the sweep; space is O(n) for the
    output.

The lesson behind it: Merge Intervals
    https://bytepatterns.com/learn/intervals/merge-intervals
    python intervals/02-merge-intervals.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/intervals/merge-overlapping-spans

Run it:  python problems/intervals/06-merge-overlapping-spans.py
"""


def merge_spans(spans):
    out = []
    for start, end in sorted(spans):           # by start, then end
        if out and start <= out[-1][1]:        # overlaps or touches the last block
            out[-1][1] = max(out[-1][1], end)  # max, because it may sit inside
        else:
            out.append([start, end])           # a gap: open a new block
    return out


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(merge_spans([[1, 3], [8, 10], [2, 6], [15, 18]]), [[1, 6], [8, 10], [15, 18]])
    check(merge_spans([[1, 10], [2, 3], [4, 5]]), [[1, 10]])
    check(merge_spans([[1, 4], [4, 5]]), [[1, 5]])
    check(merge_spans([[5, 7]]), [[5, 7]])
