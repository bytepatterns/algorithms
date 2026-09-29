"""
Largest All-Ones Rectangle (hard) · patterns: monotonic-stack, grid-scan

A grid of rows and columns holds only 0s and 1s. Find the largest rectangle,
with sides along the grid lines, that covers nothing but 1s, and return its
area as a count of cells. A grid with no 1s at all has answer 0.

Examples:

    Input:  grid = [[1, 0, 1, 1, 0],
                    [1, 1, 1, 1, 0],
                    [0, 1, 1, 1, 1],
                    [1, 1, 1, 0, 1]]
    Output: 6
    Why:    rows 1-2 across columns 1-3 are all 1s, and nothing bigger is

    Input:  grid = [[1, 1, 0, 1, 1, 1]]
    Output: 3
    Why:    a single row: the longest run of 1s wins

    Input:  grid = [[0, 0], [0, 0]]
    Output: 0
    Why:    edge case, there is no 1 to start a rectangle from

Approach:
    Every all-ones rectangle rests on some bottom row, and seen from that
    row it is a rectangle under the bar chart of 1-runs ending there. The
    bars change by one step per row, so they are rebuilt in O(columns). The
    largest rectangle under a bar chart comes from a stack whose heights
    only rise: a bar is popped when a lower bar arrives, and at that moment
    its rectangle spans from the leftmost column it could reach to just
    before the lower bar. A final bar of height 0 empties the stack at the
    end of each row. Time is O(rows times columns), and space is O(columns).

The lesson behind it: Largest Rectangle
    https://bytepatterns.com/learn/stacks-queues/largest-rectangle
    python stacks-queues/09-largest-rectangle.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/matrix-grid/largest-all-ones-rectangle

Run it:  python problems/matrix-grid/09-largest-all-ones-rectangle.py
"""


def largest_ones(grid):
    if not grid: return 0
    heights, best = [0] * len(grid[0]), 0
    for row in grid:
        for c, cell in enumerate(row):
            heights[c] = heights[c] + 1 if cell else 0   # 1s ending in this row
        stack = []                                       # (leftmost column, height), rising
        for c, h in enumerate(heights + [0]):            # the 0 flushes the stack
            start = c
            while stack and stack[-1][1] >= h:
                start, top = stack.pop()
                best = max(best, top * (c - start))      # that bar spans start..c-1
            stack.append((start, h))
    return best


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    grid = [[1, 0, 1, 1, 0], [1, 1, 1, 1, 0], [0, 1, 1, 1, 1], [1, 1, 1, 0, 1]]
    check(largest_ones(grid), 6)
    check(largest_ones([[1, 1, 0, 1, 1, 1]]), 3)
    check(largest_ones([[0, 0], [0, 0]]), 0)
