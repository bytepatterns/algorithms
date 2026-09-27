"""
Search a 2D Matrix: Start in the corner where one step rules out a whole line.

Rows grow left to right and columns grow top to bottom, but the matrix is
not one sorted list. Stand at the top-right corner instead. That cell is the
largest in its row and the smallest in its column. Too big, and the whole
column is too big — step left. Too small, and the whole row is too small —
step down. Each move deletes an entire line, so the walk is m + n steps.

Lesson 6 of Searching, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/searching/search-2d-matrix

Run it:  python searching/06-search-2d-matrix.py
"""


def search(matrix, target):
    r, c = 0, len(matrix[0]) - 1     # top-right corner
    while r < len(matrix) and c >= 0:
        v = matrix[r][c]
        if v == target:
            return (r, c)
        if v > target:
            c -= 1                   # that whole column is too big
        else:
            r += 1                   # that whole row is too small
    return None


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(search([[1, 4, 7], [8, 9, 12], [13, 15, 20]], 9), (1, 1))
