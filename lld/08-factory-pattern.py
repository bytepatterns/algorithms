"""
Factory Pattern: Ask for what you want; one place decides which class to build.

Scattered SomeClass() calls hard-wire every caller to a concrete type. A
factory takes a key and returns an object honouring a shared interface.
Choosing moves to one function, and unknown keys fail there with a clear
message instead of anywhere.

Lesson 8 of Low-Level Design, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/lld/factory-pattern

Run it:  python lld/08-factory-pattern.py
"""


class Estate:  seats, boot = 5, 550      # three products, one shared shape
class Van:     seats, boot = 3, 3000
class Compact: seats, boot = 4, 300

FLEET = {"estate": Estate, "van": Van, "compact": Compact}

def hire(car_class):                     # callers name a class, never a constructor
    if car_class not in FLEET:
        raise ValueError("no such class: " + car_class)
    return FLEET[car_class]()


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
    car = hire("van")
    check_printed(type(car).__name__, car.seats, car.boot, expect="Van 3 3000")
    check_printed(type(hire("estate")).__name__, expect="Estate")
