"""
Binary Strings With No Adjacent Ones (easy) · patterns: backtracking, pruning

Given a length n, return every binary string of that length in which no two
1s are next to each other. Return the strings in increasing order.

Examples:

    Input:  n = 3
    Output: ["000", "001", "010", "100", "101"]
    Why:    011, 110 and 111 each put two 1s side by side

    Input:  n = 1
    Output: ["0", "1"]

    Input:  n = 0
    Output: [""]
    Why:    edge case, the empty string is the one string of length zero

Approach:
    Each position is a level of the decision tree with two branches, 0 and
    1, and the rule prunes the 1 branch whenever the previous character is
    already 1. A pruned branch is never explored, so every leaf the search
    reaches is a valid string and nothing is filtered afterwards. Trying 0
    before 1 at every level visits the leaves in increasing order. The
    number of valid strings grows like the Fibonacci numbers, and each one
    costs O(n) to join, so time is O(n · F(n + 2)) and the recursion uses
    O(n) extra space beyond the output.

The lesson behind it: The Decision Tree
    https://bytepatterns.com/learn/backtracking/the-decision-tree
    python backtracking/01-the-decision-tree.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/backtracking/binary-strings-with-no-adjacent-ones

Run it:  python problems/backtracking/11-binary-strings-with-no-adjacent-ones.py
"""


def no_adjacent_ones(n):
    result, path = [], []

    def build():
        if len(path) == n:
            result.append("".join(path))
            return
        path.append("0")
        build()
        path.pop()
        if not path or path[-1] == "0":      # prune: a 1 may not follow a 1
            path.append("1")
            build()
            path.pop()

    build()
    return result


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(no_adjacent_ones(3), ['000', '001', '010', '100', '101'])
    check(no_adjacent_ones(1), ['0', '1'])
    check(no_adjacent_ones(0), [''])
