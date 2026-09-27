"""
Atomic Operations: Indivisible: nobody sees it half-done.

An atomic operation cannot be split. Other threads see the world before it
or after it, never in between, so no lock is needed. The catch is scope:
atomicity covers one step, and most real invariants span several.

Lesson 8 of Concurrency, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/concurrency/atomic-operations

Run it:  python concurrency/08-atomic-operations.py
"""


import itertools, threading

dispenser = itertools.count(1)          # next() is one indivisible step
tickets = []

def take(n):
    for _ in range(n):
        tickets.append(next(dispenser))  # append is atomic too


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
    crowd = [threading.Thread(target=take, args=(50,)) for _ in range(4)]
    for person in crowd: person.start()
    for person in crowd: person.join()
    check_printed(len(tickets), len(set(tickets)), expect="200 200 — no number issued twice")
