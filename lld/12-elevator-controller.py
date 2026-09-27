"""
Elevator Controller: The car has a direction, and the direction answers the buttons.

Model the car as a small state machine: idle, up, down, doors open. Pending
floors live in a set, not a queue.

The controller never asks who pressed first. It asks what is next in the
direction it is already travelling, and only reconsiders direction when
nothing is left ahead.

Lesson 12 of Low-Level Design, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/lld/elevator-controller

Run it:  python lld/12-elevator-controller.py
"""


class Car:
    def __init__(self, floor=0):
        self.floor, self.direction, self.stops = floor, "idle", set()
    def press(self, f):
        self.stops.add(f)                                # a set, not a queue
        if self.direction == "idle":                     # first request sets it
            self.direction = "up" if f > self.floor else "down"
    def next_stop(self):
        ahead = [f for f in self.stops
                 if (f > self.floor) == (self.direction == "up")]
        return (min if self.direction == "up" else max)(ahead) if ahead else None


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
    car = Car(6); car.press(9); car.press(4)
    check_printed(car.direction, car.next_stop(), expect="up 9")
