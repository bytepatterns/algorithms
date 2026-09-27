"""
Count Provinces (medium) · patterns: union-find, connected-components

A square matrix records which cities are directly linked: matrix[i][j] is 1
when city i and city j are joined, and 0 otherwise. The matrix is symmetric
and every city is linked to itself. A province is a group of cities
reachable from one another, directly or through others. Return how many
provinces there are.

Examples:

    Input:  matrix = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    Output: 2
    Why:    cities 0 and 1 are joined; city 2 stands alone

    Input:  matrix = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    Output: 3
    Why:    nothing is linked, so every city is its own province

    Input:  matrix = [[1]]
    Output: 1
    Why:    edge case, a single city is one province

Approach:
    Start the count at n — every city alone — and let each link that joins
    two different groups reduce it by one. A disjoint-set structure answers
    "same group?" in near-constant time once path halving flattens the
    chains, and a link inside one group is simply ignored. Only the upper
    triangle has to be read, since the matrix is symmetric. Time is O(n² ·
    α(n)) dominated by reading the matrix, space O(n).

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/union-find/count-provinces

Run it:  python problems/union-find/01-count-provinces.py
"""


def provinces(matrix):
    n = len(matrix)
    parent = list(range(n))                  # every city starts alone
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]    # path halving
            x = parent[x]
        return x
    groups = n
    for i in range(n):
        for j in range(i + 1, n):            # symmetric: upper triangle only
            if matrix[i][j]:
                a, b = find(i), find(j)
                if a != b:                   # a real merge, not a re-link
                    parent[a] = b
                    groups -= 1
    return groups


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(provinces([[1, 1, 0], [1, 1, 0], [0, 0, 1]]), 2)
    check(provinces([[1, 0, 0], [0, 1, 0], [0, 0, 1]]), 3)
    check(provinces([[1]]), 1)
