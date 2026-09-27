"""
Bipartite Check: Two colours, no neighbour sharing one — or the split is impossible.

Colour the start node, colour every neighbour the opposite, and keep going.
If you ever reach a neighbour that already carries your own colour, the
split is impossible — an odd cycle is hiding in there. It is ordinary BFS
with one extra field per node, so the cost stays O(V + E).

Lesson 12 of Graphs, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/graphs/bipartite-check

Run it:  python graphs/12-bipartite-check.py
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
    from collections import deque
    g = {"ann": ["bob", "cy"], "bob": ["ann", "dee"],
         "cy": ["ann", "dee"], "dee": ["bob", "cy"]}

    colour = {"ann": 0}
    q = deque(["ann"])
    ok = True
    while q:
        n = q.popleft()
        for m in g[n]:
            if m not in colour:
                colour[m] = 1 - colour[n]    # opposite side of the split
                q.append(m)
            elif colour[m] == colour[n]:     # neighbours share a side
                ok = False

    check_printed(ok, colour, expect="True {'ann': 0, 'bob': 1, 'cy': 1, 'dee': 0}")
