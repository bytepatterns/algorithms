"""
Graph Basics: Things, plus the connections between them.

A graph is nodes joined by edges. That is the whole definition — arrays and
linked lists just add rules on top of it. Edges can be undirected (a two-way
bond) or directed (one-way). A node's degree is simply how many edges touch
it.

Lesson 1 of Graphs, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/graphs/graph-basics

Run it:  python graphs/01-graph-basics.py
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
    molecule = {                     # methanol, CH3OH
        "C": ["H1", "H2", "H3", "O"],
        "H1": ["C"], "H2": ["C"], "H3": ["C"],
        "O": ["C", "H4"],
        "H4": ["O"],
    }
    bonds = sum(len(v) for v in molecule.values()) // 2   # each bond seen twice
    check_printed("atoms:", len(molecule), expect="atoms: 6")
    check_printed("bonds:", bonds, expect="bonds: 5")
    check_printed("degree of C:", len(molecule["C"]), expect="degree of C: 4")
