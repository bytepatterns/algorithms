"""
Stones Sharing A Line (medium) · patterns: union-find, connected-components

Stones sit on distinct points of an integer grid. You may take a stone off
the board if at least one other stone still on the board shares its row or
its column. Return the largest number of stones you can take off by choosing
the order well.

Examples:

    Input:  stones = [[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]
    Output: 5
    Why:    all six stones are linked through shared rows and columns, so one remains

    Input:  stones = [[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]]
    Output: 3
    Why:    the centre stone shares nothing, and the four corners reduce to one

    Input:  stones = [[0, 0]]
    Output: 0
    Why:    edge case, a lone stone has no partner

Approach:
    Within a connected group of stones, removing them in reverse order of a
    traversal from any chosen stone always leaves the removed stone a
    partner, so each group shrinks to one stone and no further; the answer
    is the number of stones minus the number of groups. Rather than
    comparing stones pairwise, each stone merges its row with its column, so
    two stones end up in the same set exactly when a chain of shared lines
    links them. Union by size keeps the trees shallow and path halving
    flattens them further. Time is O(n times the inverse Ackermann function)
    and space is O(n).

The lesson behind it: Union by Rank or Size
    https://bytepatterns.com/learn/union-find/union-by-size
    python union-find/03-union-by-size.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/union-find/stones-sharing-a-line

Run it:  python problems/union-find/06-stones-sharing-a-line.py
"""


def removable(stones):
    parent, size = {}, {}
    def find(x):
        parent.setdefault(x, x); size.setdefault(x, 1)
        while parent[x] != x:
            parent[x] = parent[parent[x]]        # path halving
            x = parent[x]
        return x
    def union(a, b):
        a, b = find(a), find(b)
        if a == b: return
        if size[a] < size[b]: a, b = b, a        # hang the smaller tree under the larger
        parent[b] = a; size[a] += size[b]
    for r, c in stones:
        union(("row", r), ("col", c))            # a stone links its row and its column
    groups = len({find(x) for x in parent})
    return len(stones) - groups


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(removable([[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]), 5)
    check(removable([[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]]), 3)
    check(removable([[0, 0]]), 0)
