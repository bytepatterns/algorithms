"""
DP on Grids: Each cell's answer comes from the cells above and to its left.

A grid makes DP two-dimensional. When movement is limited to right and down,
a cell can only be entered from above or from the left, so its answer
combines just those two. Counting routes means adding them together; finding
the cheapest route means taking the smaller one and adding the cell's own
cost.

Lesson 10 of Dynamic Programming, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/dynamic-programming/dp-on-grids

Run it:  python dynamic-programming/10-dp-on-grids.py
"""


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    grid = [[1, 3, 1],
            [1, 5, 1],
            [4, 2, 1]]

    cost = [row[:] for row in grid]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if i or j:                                        # skip the start cell
                above = cost[i - 1][j] if i else float("inf")
                left = cost[i][j - 1] if j else float("inf")
                cost[i][j] += min(above, left)                # cheapest way in

    check(cost[-1][-1], 7)
