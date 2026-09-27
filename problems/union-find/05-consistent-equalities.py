"""
Consistent Equalities (medium) · patterns: union-find, two-phase

Each constraint is a four-character string over single lowercase letters,
either "x==y" or "x!=y". Decide whether you can give every letter an integer
value so that all the constraints hold at once.

Examples:

    Input:  rules = ["a==b", "b!=a"]
    Output: False

    Input:  rules = ["a==b", "b==c", "c!=d", "a!=d"]
    Output: True
    Why:    give a, b and c one value and d another

    Input:  rules = ["a!=a"]
    Output: False
    Why:    edge case, a letter can never differ from itself

Approach:
    Only the equalities force letters together, and they do so transitively,
    so merging them in a disjoint-set structure produces exactly the groups
    of letters that must share a value. Giving each group its own distinct
    value then satisfies every equality, and it satisfies every inequality
    whose letters sit in different groups. So an inequality fails precisely
    when both of its letters landed in the same group, including the case of
    a letter compared with itself. Processing all the equalities before any
    inequality is essential. With 26 letters, time is O(n) over the rules
    and space is O(1).

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/union-find/consistent-equalities

Run it:  python problems/union-find/05-consistent-equalities.py
"""


def consistent(rules):
    parent = {c: c for c in "abcdefghijklmnopqrstuvwxyz"}
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]        # path halving
            x = parent[x]
        return x
    for r in rules:
        if r[1] == "=":                          # phase 1: merge the equalities
            parent[find(r[0])] = find(r[3])
    for r in rules:
        if r[1] == "!" and find(r[0]) == find(r[3]):   # phase 2: test the rest
            return False
    return True


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(consistent(["a==b", "b!=a"]), False)
    check(consistent(["a==b", "b==c", "c!=d", "a!=d"]), True)
    check(consistent(["a!=a"]), False)
