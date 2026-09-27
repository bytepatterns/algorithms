"""
Kruskal's Spanning Tree: Buy the cheapest cable that joins two pieces you have not joined yet.

A minimum spanning tree connects every node as cheaply as possible. Kruskal
sorts all edges by weight and walks the list, keeping an edge only when its
two ends still belong to different pieces. Union-find answers that question
in near-constant time. Stop after V-1 accepted edges — the rest would only
close cycles.

Lesson 10 of Graphs, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/graphs/kruskal-mst

Run it:  python graphs/10-kruskal-mst.py
"""


edges = [(1, "a", "b"), (4, "b", "c"), (3, "a", "c"), (2, "c", "d"), (5, "b", "d")]
parent = {n: n for n in "abcd"}

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]    # path compression
        x = parent[x]
    return x


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

import re


def _same(printed, expected):
    """Printed text vs the lesson's comment, which may add a note after it."""
    printed, expected = printed.strip(), expected.strip()
    wants = [expected] + [expected.rsplit(s, 1)[1].strip() for s in (" -> ", " = ") if s in expected]
    for want in wants + [w[1:] for w in wants if w.startswith("~")]:
        rest = want[len(printed):] if want.startswith(printed) else None
        if rest == "" or (rest and re.match(r"[\s,;:]+([A-Za-z]|\u2014|\u2013|-(?!\d)|\u2192|<-|\([A-Za-z]|#)", rest)):
            return True
    return False


def check_printed(*values, expect, sep=" ", end="\n"):
    """print(*values), then assert the line reads the way the lesson's comment says."""
    print(*values, sep=sep, end=end)
    forms = [sep.join(map(str, values))]
    if len(values) == 1 and isinstance(values[0], str):
        forms += [repr(values[0]), '"%s"' % values[0]] + (["(empty string)"] if not values[0] else [])
    if len(values) > 1 and isinstance(values[0], str):  # a leading label
        forms.append(sep.join(map(str, values[1:])))
    assert any(_same(f, expect) for f in forms), f"expected {expect!r}, got {forms[0]!r}"


if __name__ == "__main__":
    total, tree = 0, []
    for w, u, v in sorted(edges):            # cheapest edge first
        ru, rv = find(u), find(v)
        if ru != rv:                         # different pieces, so no cycle
            parent[ru] = rv
            tree.append((u, v))
            total += w

    check_printed(tree, total, expect="[('a', 'b'), ('c', 'd'), ('a', 'c')] 6")
