"""
Rising Tide Crossing (hard) · patterns: union-find, minimum-spanning-tree, sorting

A flooded field is a grid of ground heights, and the water level rises
steadily from 0. A rescue boat can float over any cell whose ground height
is at most the current water level, and it moves up, down, left or right
between floatable cells. Return the lowest water level at which the boat can
travel from the top-left cell to the bottom-right cell. The grid has at
least one cell, and heights are whole numbers from 0 upward.

Examples:

    Input:  heights = [[1, 5, 2],
                       [2, 9, 1],
                       [3, 4, 1]]
    Output: 4
    Why:    down the left edge and along the bottom, the highest ground is 4

    Input:  heights = [[0, 2],
                       [1, 3]]
    Output: 3
    Why:    the destination itself sits at height 3

    Input:  heights = [[7]]
    Output: 7
    Why:    edge case, start and finish are the same cell

Approach:
    A route is usable at level t exactly when every cell on it is at most t,
    so the answer is the smallest possible maximum height along any route.
    Opening cells in increasing height, as Kruskal adds edges in increasing
    weight, and joining each one with its already-open neighbours keeps
    track of which open cells are connected. The moment the two corners
    share a set, the cell just opened is the highest one any route needs.
    Time is O(rc log rc) for sorting r times c cells, and space is O(rc).

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/graphs/rising-tide-crossing

Run it:  python problems/graphs/11-rising-tide-crossing.py
"""


def lowest_crossing_level(heights):
    rows, cols = len(heights), len(heights[0])
    parent = list(range(rows * cols))
    def find(x):                               # union-find root with path halving
        while parent[x] != x:
            parent[x] = parent[parent[x]]; x = parent[x]
        return x
    opened = set()
    for h, r, c in sorted((heights[r][c], r, c) for r in range(rows) for c in range(cols)):
        opened.add((r, c))                     # the tide reaches h and this cell floats
        for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
            if (nr, nc) in opened:
                parent[find(nr * cols + nc)] = find(r * cols + c)
        if find(0) == find(rows * cols - 1):   # the corners just joined up
            return h


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(lowest_crossing_level([[1, 5, 2], [2, 9, 1], [3, 4, 1]]), 4)
    check(lowest_crossing_level([[0, 2], [1, 3]]), 3)
    check(lowest_crossing_level([[7]]), 7)
