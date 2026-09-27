"""
Connected Components: Count the islands by starting a fresh sweep on each one.

A graph need not be one piece. Run a traversal from a node and you reach
exactly its component — nothing more. So loop over every node, and each time
you meet one nobody has visited, start a fresh sweep and add one to the
count.

Lesson 5 of Graphs, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/graphs/connected-components

Run it:  python graphs/05-connected-components.py
"""


pixels = {1: [2], 2: [1], 3: [4, 5], 4: [3], 5: [3], 6: []}

def flood(p, seen, blob):
    seen.add(p)
    blob.append(p)
    for q in pixels[p]:              # spread to touching pixels
        if q not in seen:
            flood(q, seen, blob)
    return blob


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
    seen, blobs = set(), []
    for p in pixels:
        if p not in seen:                # a region nobody has reached
            blobs.append(flood(p, seen, []))
    check_printed(len(blobs), blobs, expect="3 [[1, 2], [3, 4, 5], [6]]")
