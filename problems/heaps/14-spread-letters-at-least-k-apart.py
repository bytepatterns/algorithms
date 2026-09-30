"""
Spread Letters at Least K Apart (medium) · patterns: max-heap, greedy, cooldown-queue

Rearrange the letters of a string so that any two equal letters are at least
k positions apart, meaning their indices differ by k or more. Among the
letters allowed at each position, always place the one with the most copies
left, taking the alphabetically smallest on a tie, so the answer is unique.
If no arrangement exists, return an empty string. The string has up to
100,000 lowercase letters.

Examples:

    Input:  s = "aabbcc", k = 3
    Output: "abcabc"
    Why:    each letter waits for the other two before it can repeat

    Input:  s = "aaadbbcc", k = 2
    Output: "abacabcd"
    Why:    a has the most copies, so it goes first whenever its cooldown allows

    Input:  s = "aaabc", k = 3
    Output: ""
    Why:    edge case, three a's need a span of 7 positions and only 5 exist

Approach:
    The greedy rule is to spend the most plentiful letter as early as it is
    allowed, because the letter with the most copies is the one that needs
    the most room; spending a rare letter first can only leave the common
    one stuck at the end. A heap of (-count, letter) gives that letter, with
    the alphabetical tie-break built into the tuple order. The cooldown is a
    plain FIFO queue: letters leave the heap when placed and come back once
    k positions have passed, and since they enter the queue in position
    order, only its front ever needs checking. If at some position the heap
    is empty but letters are still waiting, every remaining letter is on
    cooldown and no arrangement exists. With n letters and an alphabet of
    size a, time is O(n log a) and space is O(a).

The lesson behind it: Reorganize a String
    https://bytepatterns.com/learn/heaps/reorganize-a-string
    python heaps/06-reorganize-a-string.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/heaps/spread-letters-at-least-k-apart

Run it:  python problems/heaps/14-spread-letters-at-least-k-apart.py
"""


import heapq
from collections import Counter, deque

def spread_letters(s, k):
    heap = [(-n, ch) for ch, n in Counter(s).items()]
    heapq.heapify(heap)                    # most copies left first, then alphabetical
    waiting = deque()                      # (index it is free again, -count, letter)
    out = []
    while heap or waiting:
        if waiting and waiting[0][0] <= len(out):
            _, n, ch = waiting.popleft()
            heapq.heappush(heap, (n, ch))  # its cooldown is over
        if not heap:
            return ""                      # everything left is still cooling down
        n, ch = heapq.heappop(heap)
        out.append(ch)
        if n + 1:
            waiting.append((len(out) - 1 + k, n + 1, ch))
    return "".join(out)


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
    check_printed(spread_letters("aabbcc", 3), expect="abcabc")
    check_printed(spread_letters("aaadbbcc", 2), expect="abacabcd")
    check_printed(spread_letters("aaabc", 3), expect="(empty string)")
