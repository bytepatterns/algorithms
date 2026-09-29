"""
Distinct Arrangements (medium) · patterns: backtracking, pruning, sorting

Given a list of values that may contain repeats, return every distinct
ordering of all of them. Two orderings are the same when they read the same
value by value, so repeats must not produce duplicate answers. Return the
orderings in ascending lexicographic order so the output is predictable.

Examples:

    Input:  vals = [1, 2, 1]
    Output: [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
    Why:    3 slots with two equal values give 3!/2! = 3 orderings

    Input:  vals = [2, 2, 2]
    Output: [[2, 2, 2]]
    Why:    every ordering reads the same

    Input:  vals = []
    Output: [[]]
    Why:    edge case, there is exactly one way to arrange nothing

Approach:
    This is the used-set permutation search with one extra pruning rule.
    After sorting, equal values are adjacent, and allowing a copy only when
    its left twin is already on the path means equal copies always appear in
    their original order. Every distinct ordering therefore has exactly one
    way to be built, so no duplicate is ever produced and no set is needed
    to remove them. Trying values in sorted order at every level also makes
    the results come out in lexicographic order. Time is O(n × n!) in the
    worst case, and space is O(n) besides the output.

The lesson behind it: Permutations
    https://bytepatterns.com/learn/backtracking/permutations
    python backtracking/03-permutations.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/backtracking/distinct-arrangements

Run it:  python problems/backtracking/07-distinct-arrangements.py
"""


def arrangements(vals):
    vals = sorted(vals)              # equal values become neighbours
    used, path, out = [False] * len(vals), [], []
    def place():
        if len(path) == len(vals):
            out.append(path[:])
            return
        for i, v in enumerate(vals):
            if used[i]:
                continue
            if i and v == vals[i - 1] and not used[i - 1]:
                continue             # a twin goes only after its left twin
            used[i] = True
            path.append(v)
            place()
            path.pop()
            used[i] = False
    place()
    return out


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(arrangements([1, 2, 1]), [[1, 1, 2], [1, 2, 1], [2, 1, 1]])
    check(arrangements([2, 2, 2]), [[2, 2, 2]])
    check(arrangements([]), [[]])
