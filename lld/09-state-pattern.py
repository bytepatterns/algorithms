"""
State Pattern: Same method call, different answer, because the object moved on.

Some objects answer the same call differently depending on where they are in
their life. Model that explicitly: name the states, list which actions each
one allows, and let the state decide what comes next. Illegal actions
bounce, leaving the object untouched.

Lesson 9 of Low-Level Design, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/lld/state-pattern

Run it:  python lld/09-state-pattern.py
"""


class Application:
    ALLOWED = {"draft": ["submit"], "submitted": ["check"],
               "checked": ["print"], "printed": []}
    NEXT = {"submit": "submitted", "check": "checked", "print": "printed"}
    def __init__(self): self.state = "draft"
    def do(self, action):
        if action not in self.ALLOWED[self.state]:      # the state owns the menu
            return action + " refused while " + self.state
        self.state = self.NEXT[action]
        return "now " + self.state


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
    a = Application()
    check_printed(a.do("submit"), expect="now submitted")
    check_printed(a.do("print"), expect="print refused while submitted")
    check_printed(a.do("check"), expect="now checked")
