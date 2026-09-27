"""
Semaphores: Count the permits, not the holders.

A semaphore holds a fixed number of permits. Acquire takes one, release puts
one back, and when none are left the next caller waits. It caps how many
threads use a limited resource at once — connections, licences, outbound
calls.

Lesson 9 of Concurrency, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/concurrency/semaphores

Run it:  python concurrency/09-semaphores.py
"""


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
    import threading

    barrows = threading.Semaphore(3)     # three permits on the rack

    for plot in ["A", "B", "C"]:
        barrows.acquire()
        print(plot, "took a barrow")

    check_printed("spare?", barrows.acquire(blocking=False), expect="False — rack is empty")
    barrows.release()                                  # plot A wheels one back
    check_printed("spare?", barrows.acquire(blocking=False), expect="True")
