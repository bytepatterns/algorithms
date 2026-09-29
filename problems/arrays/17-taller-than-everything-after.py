"""
Taller Than Everything After (easy) · patterns: running-maximum, linear-scan

A row of buildings faces the sea at the right end of the row. A building has
a clear view when it is strictly taller than every building to its right.
Given the heights from left to right, return the heights of the buildings
with a clear view, in the same left-to-right order.

Examples:

    Input:  heights = [16, 17, 4, 3, 5, 2]
    Output: [17, 5, 2]
    Why:    17 and 5 beat everything after them, and the last
            building always has a view

    Input:  heights = [5, 5, 3]
    Output: [5, 3]
    Why:    the first 5 is only as tall as the second one, not strictly taller

    Input:  heights = []
    Output: []
    Why:    edge case, an empty row has no buildings to report

Approach:
    A building's view depends only on the tallest building to its right, so
    scanning from the right end with a running maximum answers every
    building in one step. A building strictly above the running maximum is
    kept, and the maximum is raised to it. The kept heights come out right
    to left, so one reversal restores the original order. Time is O(n), and
    extra space is O(1) apart from the output.

The lesson behind it: Array Basics
    https://bytepatterns.com/learn/arrays/array-basics
    python arrays/01-array-basics.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/arrays/taller-than-everything-after

Run it:  python problems/arrays/17-taller-than-everything-after.py
"""


def clear_views(heights):
    kept, tallest = [], float("-inf")
    for i in range(len(heights) - 1, -1, -1):   # right to left by index
        if heights[i] > tallest:
            kept.append(heights[i])
            tallest = heights[i]
    kept.reverse()                               # back to left-to-right order
    return kept


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(clear_views([16, 17, 4, 3, 5, 2]), [17, 5, 2])
    check(clear_views([5, 5, 3]), [5, 3])
    check(clear_views([]), [])
