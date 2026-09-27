"""
Composition vs Inheritance: Assemble behaviour from parts instead of freezing it in a family tree.

Inheritance says a child is its parent, forever, decided at import time.
Composition says an object has parts it can call, chosen when you build it —
or later. Prefer composition: parts recombine, and a change to one part does
not ripple through a family of subclasses.

Lesson 3 of Low-Level Design, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/lld/composition-vs-inheritance

Run it:  python lld/03-composition-vs-inheritance.py
"""


class Belt:
    def apply(self, item): return item + " +moved"
class Stamper:
    def apply(self, item): return item + " +stamped"

class Line:                              # HAS-A list of stages; it IS-A nothing
    def __init__(self, *stages): self.stages = list(stages)
    def run(self, item):
        for s in self.stages: item = s.apply(item)
        return item


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
    line = Line(Belt())
    check_printed(line.run("blank"), expect="blank +moved")
    line.stages.append(Stamper())            # new behaviour at runtime, no subclass
    check_printed(line.run("blank"), expect="blank +moved +stamped")
