"""
Tail Calls and Loops: When nothing happens after the call, the frame is dead weight.

If a recursive call is the very last thing a function does, the caller's
frame has no work left. Its locals are never read again.

Some languages spot that and reuse the frame. Python does not, so the stack
grows until it hits the limit. The fix is mechanical: the accumulator
parameter becomes a variable, the call becomes a loop.

Lesson 7 of Recursion, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/recursion/tail-recursion

Run it:  python recursion/07-tail-recursion.py
"""


import sys

def total(n, acc=0):                 # tail call: nothing happens after the call returns
    if n == 0: return acc
    return total(n - 1, acc + n)     # ...so this frame has no work left to come back to

def total_loop(n):                   # the same function with the frames taken out
    acc = 0
    while n:
        acc, n = acc + n, n - 1      # the accumulator is just a variable now
    return acc


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
    check_printed(total(500), total_loop(500), expect="125250 125250")
    check(sys.getrecursionlimit(), 1000)  # Python keeps every frame
    try: total(100_000)
    except RecursionError: print("RecursionError")   # the loop version would shrug
