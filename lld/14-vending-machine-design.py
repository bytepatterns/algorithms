"""
Vending Machine: Four small objects, each one only answering for its own moment.

Give every state its own small object: idle, paid, dispensing, sold out.
Each answers the same actions differently, and a transition is a state
replacing itself on the machine.

The machine holds no rules at all — no flags, no chain of checks that has to
be repeated in every method.

Lesson 14 of Low-Level Design, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/lld/vending-machine-design

Run it:  python lld/14-vending-machine-design.py
"""


class Idle:
    def coin(self, m): m.state = Paid(); return "paid"
    def select(self, m): return "pay first"

class Paid:
    def coin(self, m): return "already paid"
    def select(self, m): m.state = Idle(); return "dispensing"

class Machine:
    def __init__(self): self.state = Idle()
    def do(self, action): return getattr(self.state, action)(self)  # no flags


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
    m = Machine()
    check_printed(m.do("select"), m.do("coin"), m.do("select"), m.do("select"), expect="pay first paid dispensing pay first")
