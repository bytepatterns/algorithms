"""
Flood Fill: Spread while the colour matches, stop the moment it does not.

Click a cell, remember the colour under it, and repaint. Then ask the four
neighbours the same question: are you that colour too?

Each match repaints and passes the question on, so the patch grows outwards
until every edge is a different colour or the grid's own border. Cells
already repainted no longer match, which is what stops the spread from
looping.

Lesson 5 of Matrix & Grid, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/matrix-grid/flood-fill

Run it:  python matrix-grid/05-flood-fill.py
"""


def flood(canvas, r, c, new):
    start = canvas[r][c]
    if start == new:                   # already that colour: nothing to do
        return canvas
    stack = [(r, c)]
    while stack:
        y, x = stack.pop()
        if not (0 <= y < len(canvas) and 0 <= x < len(canvas[0])):
            continue                   # off the grid
        if canvas[y][x] != start:
            continue                   # a wall, or already repainted
        canvas[y][x] = new
        stack += [(y-1, x), (y+1, x), (y, x-1), (y, x+1)]
    return canvas


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(flood([["A", "A", "B"],
                 ["A", "A", "B"],
                 ["B", "A", "B"]], 1, 0, "C"), [['C', 'C', 'B'], ['C', 'C', 'B'], ['B', 'C', 'B']])
