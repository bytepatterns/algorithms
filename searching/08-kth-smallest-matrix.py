"""
Kth Smallest in a Matrix: Search the values, not the positions.

Rows and columns are sorted, but the matrix is not one sorted list, so there
is no index to binary search. Binary search the values instead. Guess a
number between the two corners and count how many entries are at most that
guess — the staircase walk does it in O(n). Too few, and the answer is
higher; enough, and the answer is this value or lower. The range shrinks to
one number, and that number is in the matrix.

Lesson 8 of Searching, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/searching/kth-smallest-matrix

Run it:  python searching/08-kth-smallest-matrix.py
"""


def kth_smallest(matrix, k):
    n = len(matrix)
    lo, hi = matrix[0][0], matrix[n - 1][n - 1]
    while lo < hi:
        mid = (lo + hi) // 2
        count, c = 0, n - 1
        for r in range(n):                    # staircase count of values <= mid
            while c >= 0 and matrix[r][c] > mid:
                c -= 1
            count += c + 1
        if count < k:
            lo = mid + 1
        else:
            hi = mid
    return lo


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(kth_smallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8), 13)
