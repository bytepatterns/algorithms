"""
Reorganize a String: Spend the commonest letter first, and hold it back one round.

No two neighbours may match. The greedy choice is to place whichever letter
has the most copies left, because that is the one at risk of piling up at
the end.

Keep the letter you just used out of the heap for exactly one round. If the
heap empties before the string is filled, no arrangement exists.

Lesson 6 of Heaps, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/heaps/reorganize-a-string

Run it:  python heaps/06-reorganize-a-string.py
"""


import heapq
from collections import Counter

def reorganize(s):
    heap = [(-n, ch) for ch, n in Counter(s).items()]
    heapq.heapify(heap)                      # commonest letter on top
    out, held = [], None
    while heap:
        n, ch = heapq.heappop(heap)          # never the letter placed last round
        out.append(ch)
        if held: heapq.heappush(heap, held)  # that one is legal again now
        held = (n + 1, ch) if n + 1 else None
    return "".join(out) if len(out) == len(s) else ""


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
    check_printed(reorganize("aabbcc"), expect="abcabc")
    check(reorganize("aaab"), "")  # one letter is too common to spread out
