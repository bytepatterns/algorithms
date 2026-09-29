"""
Word Endings in a Letter Stream (hard) · patterns: trie, reversed-trie, stream

A filter watches a chat message as it is typed, one letter at a time. It is
given a list of banned words up front, and after each new letter it must
report whether the text typed so far ends with any banned word. The stream
can be very long, so each letter should cost time bounded by the length of
the longest banned word, not by the length of the stream.

Examples:

    Input:  words = ["cd", "f", "kl"], stream = "abcdefghijkl"
    Output: [F, F, F, T, F, T, F, F, F, F, F, T]
    Why:    the text ends with "cd" after d, with "f" after f and with "kl" after l

    Input:  words = ["ab", "bab"], stream = "bab"
    Output: [F, F, T]
    Why:    after the last letter the text ends with both "ab" and "bab"

    Input:  words = ["xyz"], stream = "xy"
    Output: [F, F]
    Why:    edge case, the word is never completed

Approach:
    A banned word ends at the newest letter exactly when that word, read
    backwards, is a prefix of the stream read backwards from the newest
    letter. So the banned words go into a prefix tree in reverse, and each
    query is a walk down that tree over the recent letters from newest to
    oldest, which succeeds at the first node that marks the end of a word
    and fails at the first missing child. Letters older than the longest
    word can never take part in a match, so a bounded buffer holds just
    those. Building the tree costs O(total characters), each letter then
    costs O(L) for the longest word length L, and the space is O(total
    characters plus L).

The lesson behind it: Word Search With a Trie
    https://bytepatterns.com/learn/tries/word-search-with-a-trie
    python tries/03-word-search-with-a-trie.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/tries/word-endings-in-a-letter-stream

Run it:  python problems/tries/09-word-endings-in-a-letter-stream.py
"""


from collections import deque

class StreamFilter:
    def __init__(self, words):
        self.root, longest = {}, max(map(len, words))
        for w in words:
            node = self.root
            for ch in reversed(w):             # store every word backwards
                node = node.setdefault(ch, {})
            node["$"] = True
        self.recent = deque(maxlen=longest)    # older letters never matter
    def feed(self, ch):
        self.recent.append(ch)
        node = self.root
        for c in reversed(self.recent):        # newest letter first
            if c not in node:
                return False
            node = node[c]
            if "$" in node:
                return True
        return False


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
    f = StreamFilter(["cd", "f", "kl"])
    check_printed("".join("T" if f.feed(c) else "F" for c in "abcdefghijkl"), expect="FFFTFTFFFFFT")
    g = StreamFilter(["ab", "bab"])
    check_printed("".join("T" if g.feed(c) else "F" for c in "bab"), expect="FFT")
    h = StreamFilter(["xyz"])
    check_printed("".join("T" if h.feed(c) else "F" for c in "xy"), expect="FF")
