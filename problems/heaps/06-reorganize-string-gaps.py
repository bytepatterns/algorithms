"""
Reorganize String Gaps (medium) · patterns: heap, greedy

Rearrange the letters of a string so that no two neighbours are the same
letter. Return any arrangement that works, or the empty string when no
arrangement exists.

Examples:

    Input:  s = "aab"
    Output: "aba"
    Why:    the two a's are separated by the b

    Input:  s = "aaab"
    Output: ""
    Why:    three a's cannot be kept apart by a single b

    Input:  s = "vvvlo"
    Output: "vlvov"
    Why:    the three v's are spaced out by the other two letters

Approach:
    A max-heap on remaining counts always hands you the letter most at risk
    of bunching up, and holding the letter you just placed out of the heap
    for exactly one step is what stops it repeating. The construction is
    optimal, so failure is detectable without a separate count check: if it
    ever runs dry before the output is full, no arrangement exists. Time is
    O(n log d) for d distinct letters, space O(d).

The lesson behind it: Reorganize a String
    https://bytepatterns.com/learn/heaps/reorganize-a-string
    python heaps/06-reorganize-a-string.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/heaps/reorganize-string-gaps

Run it:  python problems/heaps/06-reorganize-string-gaps.py
"""


import heapq
from collections import Counter

def reorganize(s):
    heap = [(-n, ch) for ch, n in Counter(s).items()]
    heapq.heapify(heap)                     # max-heap on remaining count
    out, held = [], None
    while heap:
        n, ch = heapq.heappop(heap)         # most frequent letter still allowed
        out.append(ch)
        if held:
            heapq.heappush(heap, held)      # the previous letter is free again
        held = (n + 1, ch) if n + 1 else None
    return "".join(out) if len(out) == len(s) else ""


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
    check_printed(reorganize("aab"), expect="aba")
    check_printed(reorganize("aaab"), expect="(empty string)")
    check_printed(reorganize("vvvlo"), expect="vlvov")
