"""
Trie Basics: Store words by their letters so shared prefixes are stored once.

A trie spells words out instead of storing them whole. Each edge carries one
character, so the path down from the root is a prefix. Words that share a
prefix share those nodes.

One flag per node marks "a word ends here" — without it you cannot tell the
word car from the prefix inside cart.

Lesson 1 of Tries, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/tries/trie-basics

Short video on this lesson: https://www.youtube.com/@bytepatterns

Run it:  python tries/01-trie-basics.py
"""


root = {}
def insert(word):
    node = root
    for ch in word:                # one node per character
        node = node.setdefault(ch, {})
    node["$"] = True               # "a word ends here"

def search(word):
    node = root
    for ch in word:
        if ch not in node: return False
        node = node[ch]
    return "$" in node             # a bare prefix carries no flag


# The predict-output exercise from the lesson page. Guess first, then run.
def exercise():
    root = {}
    for word in ["do", "dorm"]:
        node = root
        for ch in word:
            node = node.setdefault(ch, {})
        node["$"] = True
    print(sorted(root["d"]["o"]))


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
    for w in ["car", "cart", "cat"]: insert(w)
    print(search("car"), search("ca"))

    # The exercise's answer, as the lesson page marks it.
    with expect_output("['$', 'r']"):
        exercise()
