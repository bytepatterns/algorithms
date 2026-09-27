"""
Interfaces and Polymorphism: Call one method name and let each type answer in its own way.

An interface is a promise about method names, not about data. Anything
honouring the promise is interchangeable, so the caller writes one line and
each type supplies its own behaviour. Abstract base classes turn that
promise into an error you get at construction time rather than in
production.

Lesson 4 of Low-Level Design, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/lld/interfaces-and-polymorphism

Run it:  python lld/04-interfaces-and-polymorphism.py
"""


from abc import ABC, abstractmethod
class Notifier(ABC):                    # the contract: one method, no data
    @abstractmethod
    def send(self, msg): ...
class Sms(Notifier):
    def send(self, msg): return "sms:" + msg
class Webhook(Notifier):
    def send(self, msg): return "post:" + msg

def fan_out(channels, msg):             # depends on the contract, not the classes
    return [c.send(msg) for c in channels]


# The predict-output exercise from the lesson page. Guess first, then run.
def exercise():
    class Plain:
        def tag(self): return "A"

    class Loud(Plain):
        def tag(self): return "B"

    def show(items): return "".join(x.tag() for x in items)

    print(show([Plain(), Loud(), Plain()]))


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

import io
import re
import sys


def _same(printed, expected):
    """Printed text vs the lesson's comment, which may add a note after it."""
    printed, expected = printed.strip(), expected.strip()
    wants = [expected] + [expected.rsplit(s, 1)[1].strip() for s in (" -> ", " = ") if s in expected]
    for want in wants + [w[1:] for w in wants if w.startswith("~")]:
        rest = want[len(printed):] if want.startswith(printed) else None
        if rest == "" or (rest and re.match(r"[\s,;:]+([A-Za-z]|\u2014|\u2013|-(?!\d)|\u2192|<-|\([A-Za-z]|#)", rest)):
            return True
    return False


class expect_output:
    """Capture everything the block prints and compare it line by line."""

    def __init__(self, *lines):
        self.lines = list(lines)

    def __enter__(self):
        self.buffer, self.stdout = io.StringIO(), sys.stdout
        sys.stdout = self.buffer

    def __exit__(self, *exc):
        sys.stdout = self.stdout
        printed = self.buffer.getvalue()
        print(printed, end="")
        got = [line.rstrip() for line in printed.splitlines()]
        want = self.lines
        if len(want) == 1 and " / " in want[0] and len(got) > 1:
            want = want[0].split(" / ")
        assert exc[0] or _lines_match(got, want), f"expected {want!r}, got {got!r}"


def _lines_match(got, want):
    if not want:
        return not got
    if want[0].strip() in ("...", "\u2026"):  # the lesson elides some lines
        return any(_lines_match(got[i:], want[1:]) for i in range(len(got) + 1))
    return bool(got) and _same(got[0], want[0]) and _lines_match(got[1:], want[1:])


if __name__ == "__main__":
    print(fan_out([Sms(), Webhook()], "disk full"))
    try: Notifier()                         # abstract: refuses to be built
    except TypeError: print("contract only")

    # The exercise's answer, as the lesson page marks it.
    with expect_output("ABA"):
        exercise()
