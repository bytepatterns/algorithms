"""
Closest Repeat Distance (easy) · patterns: hash-map, single-pass

You are given a list of values. Among all pairs of positions that hold the
same value, find the pair that sits closest together and return the gap
between them, measured as the difference of their indexes. If no value
appears twice, return -1.

Examples:

    Input:  values = [7, 1, 3, 7, 1, 7]
    Output: 2
    Why:    the 7s at indexes 3 and 5 are two apart; the 1s are three apart

    Input:  values = [3, 8, 8, 3]
    Output: 1
    Why:    the two 8s sit side by side

    Input:  values = [5, 6, 7]
    Output: -1
    Why:    edge case, nothing repeats

Approach:
    The closest earlier twin of any position is the most recent one, so
    remembering only the last index of each value is enough. A hash map
    answers that lookup in constant time on average, which turns the
    quadratic pair check into a single pass. The map is updated after every
    step, so it always holds the latest index of each value. Time is O(n) on
    average, and space is O(n) for the map.

The lesson behind it: What Is Big-O?
    https://bytepatterns.com/learn/big-o/what-is-big-o
    python big-o/01-what-is-big-o.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/hash-tables/closest-repeat-distance

Run it:  python problems/hash-tables/07-closest-repeat-distance.py
"""


def closest_repeat(values):
    last_seen = {}                     # value -> most recent index
    best = -1
    for i, v in enumerate(values):
        if v in last_seen:
            gap = i - last_seen[v]
            if best == -1 or gap < best:
                best = gap
        last_seen[v] = i               # only the latest index can matter later
    return best


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(closest_repeat([7, 1, 3, 7, 1, 7]), 2)
    check(closest_repeat([3, 8, 8, 3]), 1)
    check(closest_repeat([5, 6, 7]), -1)
