"""
Cut a Span Out of Sorted Spans (easy) · patterns: interval-overlap, single-pass

A set of numbers is stored as a sorted list of disjoint half-open spans [a,
b), each covering every number from a up to but not including b. Given one
more span cut = [lo, hi), remove every number it covers from the set and
return what is left, again as a sorted list of disjoint spans.

Examples:

    Input:  spans = [[0, 2], [3, 4], [5, 7]], cut = [1, 6]
    Output: [[0, 1], [6, 7]]
    Why:    the cut trims the first span, swallows the second and trims the third

    Input:  spans = [[0, 5]], cut = [2, 3]
    Output: [[0, 2], [3, 5]]
    Why:    a cut inside one span splits it into two

    Input:  spans = [[-5, -4], [-3, -2], [1, 2], [3, 5], [8, 9]], cut = [-1, 4]
    Output: [[-5, -4], [-3, -2], [4, 5], [8, 9]]
    Why:    edge case, spans entirely outside the cut pass through untouched

Approach:
    The list is already sorted and disjoint, so one pass in order is enough
    and the output stays sorted without any extra work. Each span is
    compared with the cut once: if they do not overlap it is copied, and if
    they do, only the parts sticking out on the left and on the right
    survive. A span that the cut covers completely produces neither part and
    disappears, and a span that the cut lands inside produces both, which is
    the split. Using half-open spans keeps the arithmetic clean, because the
    surviving pieces end exactly at lo and start exactly at hi with no plus
    or minus one. Time is O(n) and the output holds at most n + 1 spans.

The lesson behind it: Insert Interval
    https://bytepatterns.com/learn/intervals/insert-interval
    python intervals/03-insert-interval.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/intervals/cut-a-span-out-of-sorted-spans

Run it:  python problems/intervals/13-cut-a-span-out-of-sorted-spans.py
"""


def cut_span(spans, cut):
    lo, hi = cut
    out = []
    for a, b in spans:
        if b <= lo or a >= hi:          # no overlap: keep the whole span
            out.append([a, b])
            continue
        if a < lo:
            out.append([a, lo])         # the part left of the cut survives
        if b > hi:
            out.append([hi, b])         # the part right of the cut survives
    return out


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(cut_span([[0, 2], [3, 4], [5, 7]], [1, 6]), [[0, 1], [6, 7]])
    check(cut_span([[0, 5]], [2, 3]), [[0, 2], [3, 5]])
    check(cut_span([[-5, -4], [-3, -2], [1, 2], [3, 5], [8, 9]], [-1, 4]), [[-5, -4], [-3, -2], [4, 5], [8, 9]])
