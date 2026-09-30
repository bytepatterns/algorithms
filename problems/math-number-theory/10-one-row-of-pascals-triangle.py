"""
One Row of Pascal's Triangle (easy) · patterns: binomial-coefficients, multiplicative-formula

A probability library needs every binomial coefficient from C(k, 0) through
C(k, k) for a given k, which is row k of Pascal's triangle counting from row
0. Given k between 0 and 1,000, return that row as a list of integers. Build
it in O(k) arithmetic steps without building the rows above it.

Examples:

    Input:  k = 3
    Output: [1, 3, 3, 1]

    Input:  k = 5
    Output: [1, 5, 10, 10, 5, 1]

    Input:  k = 0
    Output: [1]
    Why:    edge case, row 0 holds a single 1

Approach:
    Each entry of row k is a binomial coefficient, and neighbouring
    coefficients differ by a simple ratio: C(k, j + 1) = C(k, j) × (k - j) /
    (j + 1). Starting from C(k, 0) = 1, each next entry costs one
    multiplication and one division. Multiplying before dividing keeps the
    arithmetic exact, because C(k, j) × (k - j) equals C(k, j + 1) × (j + 1)
    and so is always a multiple of j + 1, and Python's big integers mean
    even the middle of row 1,000 never overflows. This avoids building the k
    rows above, which would take O(k²) additions. The row takes O(k)
    arithmetic steps and O(k) space for the output.

The lesson behind it: Permutations vs Combinations
    https://bytepatterns.com/learn/math-number-theory/counting-permutations-combinations
    python math-number-theory/05-counting-permutations-combinations.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/math-number-theory/one-row-of-pascals-triangle

Run it:  python problems/math-number-theory/10-one-row-of-pascals-triangle.py
"""


def pascal_row(k):
    row = [1]
    for j in range(k):
        row.append(row[-1] * (k - j) // (j + 1))   # exact: C(k, j+1) * (j+1)
    return row


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(pascal_row(3), [1, 3, 3, 1])
    check(pascal_row(5), [1, 5, 10, 10, 5, 1])
    check(pascal_row(0), [1])
