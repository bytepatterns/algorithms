"""
Backpressure: An unbounded queue is not a buffer, it is a delayed crash.

Backpressure is the signal that travels backwards when the consumer cannot
keep up. A bounded queue creates it for free: once full, the producer
blocks, fails, or drops. Unbounded queues delete that signal, so latency and
memory grow until something dies.

Lesson 11 of Concurrency, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/concurrency/backpressure

Run it:  python concurrency/11-backpressure.py
"""


import queue, threading, time
belt = queue.Queue(maxsize=2)          # the bound IS the backpressure
placed = shed = 0

def wrap():                            # slow consumer
    for _ in range(3):
        time.sleep(0.08); belt.get()


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
    t = threading.Thread(target=wrap); t.start()
    for loaf in range(6):                  # fast producer
        try:
            belt.put(loaf, timeout=0.05); placed += 1
        except queue.Full:
            shed += 1                      # refuse work instead of hoarding it
    t.join()
    check_printed(placed + shed == 6, shed > 0, expect="True True")
