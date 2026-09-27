"""
Spiral Order: Four walls that close in after every pass.

Do not chase a direction. Hold four walls — top, bottom, left, right —
around the part still unread.

Walk the top wall left to right and push it down. Walk the right wall down
and pull it in. Bottom back, left up, and repeat. The same four moves handle
any rectangle; when the walls cross, you are done.

Lesson 2 of Matrix & Grid, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/matrix-grid/spiral-order

Run it:  python matrix-grid/02-spiral-order.py
"""


def spiral(g):
    top, bottom, left, right = 0, len(g) - 1, 0, len(g[0]) - 1
    out = []
    while top <= bottom and left <= right:
        out += [g[top][c] for c in range(left, right + 1)]; top += 1
        out += [g[r][right] for r in range(top, bottom + 1)]; right -= 1
        if top <= bottom:                    # that row may already be spent
            out += [g[bottom][c] for c in range(right, left - 1, -1)]; bottom -= 1
        if left <= right:
            out += [g[r][left] for r in range(bottom, top - 1, -1)]; left += 1
    return out


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(spiral([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [1, 2, 3, 6, 9, 8, 7, 4, 5])
