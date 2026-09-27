"""
Unique BST Shapes (medium) · patterns: bottom-up-dp, counting

Count the structurally different binary search trees that can hold the
values 1 through n, each value used exactly once. Two trees differ when
their shapes differ, so the same values arranged differently count
separately. For n equal to 0 the answer counts the single empty tree.

Examples:

    Input:  n = 3
    Output: 5
    Why:    each of the three values can be the root, and the root 2 allows only one shape

    Input:  n = 1
    Output: 1
    Why:    a single value has exactly one tree

    Input:  n = 0
    Output: 1
    Why:    edge case, the empty tree is one valid shape

Approach:
    Choosing the root splits the values deterministically: everything
    smaller goes left and everything larger goes right, so the count for a
    size is a sum over roots of left count times right count. Only the sizes
    of the two sides matter, never the actual values, which is why one table
    indexed by size suffices. Seeding size zero with one shape makes the
    empty subtree behave correctly inside every product. Time is O(n
    squared) for the double loop, and space is O(n).

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/dynamic-programming/unique-bst-shapes

Run it:  python problems/dynamic-programming/07-unique-bst-shapes.py
"""


def count_bst_shapes(n):
    ways = [0] * (n + 1)
    ways[0] = 1                      # the empty tree counts as one shape
    for size in range(1, n + 1):
        for left in range(size):     # the root leaves `left` values on its left
            ways[size] += ways[left] * ways[size - 1 - left]
    return ways[n]


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(count_bst_shapes(3), 5)
    check(count_bst_shapes(1), 1)
    check(count_bst_shapes(0), 1)
