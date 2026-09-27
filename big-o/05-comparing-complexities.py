"""
Comparing Complexities: O(n log n) beats O(n²) long before you notice.

The usual ranking runs O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ).
Small inputs hide the gaps between them. Real data exposes those gaps
immediately.

Lesson 5 of Big-O, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/big-o/comparing-complexities

Short video on this lesson: https://www.youtube.com/@bytepatterns

Run it:  python big-o/05-comparing-complexities.py
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
    import math

    n = 1_000_000
    check_printed(1, expect="O(1)       -> 1")
    check_printed(int(math.log2(n)), expect="O(log n)   -> 19")
    check_printed(n, expect="O(n)       -> 1000000")
    check_printed(int(n * math.log2(n)), expect="O(n log n) -> ~19931568")
    check_printed(n * n, expect="O(n^2)     -> 1000000000000")
    # Same input. Wildly different bills.
