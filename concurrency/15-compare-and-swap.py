"""
Compare-and-Swap: Publish the new value only if nobody changed the old one.

Compare-and-swap takes an address, the value you expect there, and the value
you want. The hardware writes only if the expectation still holds, and tells
you which happened. A failed swap is not an error — it is news, and the
answer is to re-read and try again.

Lesson 15 of Concurrency, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/concurrency/compare-and-swap

Run it:  python concurrency/15-compare-and-swap.py
"""


class Cell:
    def __init__(self, v): self.v = v
    def cas(self, expect, new):
        if self.v != expect: return False      # somebody moved it
        self.v = new; return True


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
    cell, tries, meddle = Cell(10), 0, [True, False]
    while True:
        tries += 1
        seen = cell.v                              # read
        if meddle.pop(0): cell.v += 5              # another thread wins the race
        if cell.cas(seen, seen + 1): break         # compute, then publish or retry
    check_printed(tries, cell.v, expect="2 16")
