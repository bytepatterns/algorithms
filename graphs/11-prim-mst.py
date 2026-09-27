"""
Prim's Spanning Tree: One tree that grows, always by its cheapest way out.

Prim grows a single tree instead of merging scattered pieces. Every edge
leaving the tree sits in a min-heap; pop the cheapest, and if its far end is
new, absorb it and push that node's own exits. Stale edges — both ends
already inside — are skipped on the way out. Same total as Kruskal,
different order of arrival.

Lesson 11 of Graphs, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/graphs/prim-mst

Run it:  python graphs/11-prim-mst.py
"""


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
    import heapq
    g = {"a": [("b", 1), ("c", 3)], "b": [("a", 1), ("c", 4), ("d", 5)],
         "c": [("a", 3), ("b", 4), ("d", 2)], "d": [("b", 5), ("c", 2)]}

    seen = {"a"}
    pq = [(w, "a", m) for m, w in g["a"]]
    heapq.heapify(pq)
    total, tree = 0, []
    while pq:
        w, u, v = heapq.heappop(pq)      # cheapest edge leaving the tree
        if v in seen:
            continue                     # both ends inside: stale
        seen.add(v)
        tree.append((u, v))
        total += w
        for m, w2 in g[v]:
            if m not in seen:
                heapq.heappush(pq, (w2, v, m))

    check_printed(tree, total, expect="[('a', 'b'), ('a', 'c'), ('c', 'd')] 6")
