"""
Trie vs Hash Set: A set answers 'is this word here'. A trie answers 'what starts with this'.

A hash set turns a word into a bucket. That is unbeatable for "is this exact
word stored?" and it costs less memory than a node per character.

The moment the question involves a prefix, hashing has thrown away what you
need. A trie keeps it. Pick by the question you will actually ask.

Lesson 4 of Tries, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/tries/trie-vs-hash-set

Run it:  python tries/04-trie-vs-hash-set.py
"""


# The predict-output exercise from the lesson page. Guess first, then run.
def exercise():
    words = {"ate", "atom", "be"}
    trie = {"a": {"t": {"e": {"$": 1}, "o": {"m": {"$": 1}}}}, "b": {"e": {"$": 1}}}
    print(len(words), len(trie))


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
    words = {"car", "cart", "cat", "dog"}
    print("cart" in words)                                   # exact hit, O(1)
    print(sorted(w for w in words if w.startswith("ca")))    # O(n): scans everything

    trie = {"c": {"a": {"r": {"$": 1, "t": {"$": 1}}, "t": {"$": 1}}}}
    node = trie
    for ch in "ca":                       # O(len(prefix)), then read the subtree
        node = node[ch]
    print(sorted(node))                   # only the 'ca' branch was touched

    # The exercise's answer, as the lesson page marks it.
    with expect_output("3 2"):
        exercise()
