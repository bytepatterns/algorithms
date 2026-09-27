"""
Spreading Rot Minutes (medium) · patterns: bfs, multi-source, grid-traversal

A crate is a grid of cells: 0 is empty, 1 is a fresh fruit and 2 is a rotten
one. Every minute, each rotten fruit spoils the fresh fruit directly above,
below, left and right of it. Return the number of minutes until no fresh
fruit is left, or -1 when some fruit can never be reached.

Examples:

    Input:  [[2, 1, 1],
             [1, 1, 0],
             [0, 1, 1]]
    Output: 4
    Why:    the rot spreads outward one ring per minute

    Input:  [[2, 1, 1],
             [0, 1, 1],
             [1, 0, 1]]
    Output: -1
    Why:    the fruit in the bottom left corner is walled off by empty cells

    Input:  [[0, 2]]
    Output: 0
    Why:    edge case, nothing is fresh so no time passes

Approach:
    Because the rot advances one ring per minute from every rotten cell
    simultaneously, a breadth-first expansion seeded with all rotten cells
    at once assigns each fruit exactly the minute it spoils. Marking a cell
    as rotten at the moment it is queued, rather than when it is dequeued,
    keeps every cell in the queue once. A running count of fresh cells
    distinguishes finished from walled off, and it also gives 0 for a crate
    with nothing fresh. Time is O(rows times cols) and space is the same for
    the queue.

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/graphs/spreading-rot-minutes

Run it:  python problems/graphs/06-spreading-rot-minutes.py
"""


from collections import deque
def minutes_until_all_rot(grid):
    rows, cols = len(grid), len(grid[0])
    queue, fresh = deque(), 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2: queue.append((r, c, 0))
            elif grid[r][c] == 1: fresh += 1
    minutes = 0
    while queue:
        r, c, t = queue.popleft()
        minutes = t                  # the last cell reached sets the answer
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                grid[nr][nc] = 2     # spoil on the way in, so it queues once
                fresh -= 1
                queue.append((nr, nc, t + 1))
    return -1 if fresh else minutes


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(minutes_until_all_rot([[2, 1, 1], [1, 1, 0], [0, 1, 1]]), 4)
    check(minutes_until_all_rot([[2, 1, 1], [0, 1, 1], [1, 0, 1]]), -1)
    check(minutes_until_all_rot([[0, 2]]), 0)
