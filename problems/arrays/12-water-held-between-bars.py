"""
Water Held Between Bars (hard) · patterns: two-pointers, running-maximum

A row of bars of width 1 stands on flat ground, with heights given as
non-negative whole numbers. After heavy rain, water settles in the dips
between bars and anything above the lower of the surrounding walls runs off.
Return the total units of water the row holds. Answer with one pass and
constant extra memory.

Examples:

    Input:  heights = [3, 0, 2, 0, 4, 1, 2]
    Output: 8
    Why:    3 + 1 + 3 units between the 3 and the 4, and 1 unit over the 1

    Input:  heights = [1, 2, 3, 4]
    Output: 0
    Why:    a staircase has no dip for water to sit in

    Input:  heights = []
    Output: 0
    Why:    edge case, no bars hold no water

Approach:
    The water above a bar is the lower of the tallest bar on its left and
    the tallest bar on its right, minus the bar's height. When the left bar
    is lower than the right bar, some bar at least that tall exists on the
    right, so the left side's running maximum is the true limit for the left
    bar even though the right side is not fully known. The mirror argument
    covers the right bar, so each step settles one bar exactly, just as the
    container problem always moves the shorter wall. Time is O(n) and space
    is O(1).

The lesson behind it: Container With Most Water
    https://bytepatterns.com/learn/arrays/container-with-most-water
    python arrays/07-container-with-most-water.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/arrays/water-held-between-bars

Run it:  python problems/arrays/12-water-held-between-bars.py
"""


def trapped(heights):
    i, j = 0, len(heights) - 1
    left_max = right_max = water = 0
    while i < j:
        if heights[i] < heights[j]:  # the right side is tall enough: left wall decides
            left_max = max(left_max, heights[i])
            water += left_max - heights[i]
            i += 1
        else:                        # the left side is tall enough: right wall decides
            right_max = max(right_max, heights[j])
            water += right_max - heights[j]
            j -= 1
    return water


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(trapped([3, 0, 2, 0, 4, 1, 2]), 8)
    check(trapped([1, 2, 3, 4]), 0)
    check(trapped([]), 0)
