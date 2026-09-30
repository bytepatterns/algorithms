"""
Islands After Each Land Drop (medium) · patterns: union-find, online-connectivity, grid

A grid with m rows and n columns starts as all water. You are given a list
of positions [row, col], and each one turns that cell into land, in order.
Land cells that touch up, down, left or right belong to the same island.
After each position, report how many islands there are. A position can
appear more than once, and turning land into land changes nothing.

Examples:

    Input:  m = 3, n = 3, positions = [[0, 0], [0, 1], [1, 2], [2, 1]]
    Output: [1, 1, 2, 3]
    Why:    [0, 1] joins [0, 0], while [1, 2] and [2, 1] touch nothing

    Input:  m = 2, n = 2, positions = [[0, 0], [1, 1], [0, 1]]
    Output: [1, 2, 1]
    Why:    [0, 1] touches both earlier cells and merges two islands into one

    Input:  m = 1, n = 1, positions = [[0, 0], [0, 0]]
    Output: [1, 1]
    Why:    edge case, the repeated position is already land

Approach:
    Each drop can only create one island or glue existing islands together,
    so the count is maintained instead of recomputed. The new cell starts as
    an island of its own, then each of its up to four land neighbours is
    unioned with it, and a union that joins two different roots means two
    islands became one. Two neighbours may already share a root, for example
    when they were connected around the far side, and the root check stops
    that case from being subtracted twice. Path compression makes repeated
    finds cheap, since every cell on a searched path is pointed straight at
    the root. With k positions, time is O(k · α(m · n)) after O(m · n)
    setup, and space is O(m · n).

The lesson behind it: Path Compression
    https://bytepatterns.com/learn/union-find/path-compression
    python union-find/02-path-compression.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/union-find/islands-after-each-land-drop

Run it:  python problems/union-find/12-islands-after-each-land-drop.py
"""


def islands_after_each(m, n, positions):
    parent = {}                              # only land cells are present

    def find(x):
        root = x
        while parent[root] != root:
            root = parent[root]
        while parent[x] != root:             # path compression
            parent[x], x = root, parent[x]
        return root

    count, result = 0, []
    for r, c in positions:
        cell = r * n + c
        if cell not in parent:
            parent[cell] = cell
            count += 1                       # a new island of one cell
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and nr * n + nc in parent:
                    a, b = find(cell), find(nr * n + nc)
                    if a != b:               # two islands become one
                        parent[a] = b
                        count -= 1
        result.append(count)
    return result


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(islands_after_each(3, 3, [[0, 0], [0, 1], [1, 2], [2, 1]]), [1, 1, 2, 3])
    check(islands_after_each(2, 2, [[0, 0], [1, 1], [0, 1]]), [1, 2, 1])
    check(islands_after_each(1, 1, [[0, 0], [0, 0]]), [1, 1])
