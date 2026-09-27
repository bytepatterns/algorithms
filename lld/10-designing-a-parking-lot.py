"""
Designing a Parking Lot: The classic interview warm-up, answered in objects rather than adjectives.

Name the objects first: Lot, Spot, Vehicle, Ticket, and a pricing rule. Give
each one job — the spot knows its size, the ticket knows when entry
happened, the lot only matches and counts. Then make allocation and pricing
pluggable, because those are the parts that change.

Lesson 10 of Low-Level Design, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/lld/designing-a-parking-lot

Run it:  python lld/10-designing-a-parking-lot.py
"""


class Lot:
    def __init__(self, counts): self.free = dict(counts); self.tickets = {}
    def park(self, plate, size):
        if self.free.get(size, 0) == 0: return None   # that class is full
        self.free[size] -= 1
        self.tickets[plate] = size
        return plate + "-" + size                     # the ticket
    def leave(self, plate):
        size = self.tickets.pop(plate)
        self.free[size] += 1
        return "freed " + size


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

import re

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


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
    lot = Lot({"small": 1, "large": 0})
    check_printed(lot.park("AB12", "small"), expect="AB12-small")
    check(lot.park("CD34", "small"), None)
    check_printed(lot.leave("AB12"), lot.free, expect="freed small {'small': 1, 'large': 0}")
