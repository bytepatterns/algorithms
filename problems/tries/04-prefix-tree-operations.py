"""
Prefix Tree Operations (easy) · patterns: trie, design

Build a prefix tree for lowercase words with three operations. insert(word)
stores a word. has_word(word) reports whether exactly that word was stored.
has_prefix(prefix) reports whether any stored word starts with the given
non-empty prefix. Each operation should cost time proportional to the length
of its argument, however many words are stored.

Examples:

    Input:  insert("apple"), has_word("apple"), has_word("app"), has_prefix("app")
    Output: True, False, True
    Why:    "app" begins a stored word but was never stored itself

    Input:  insert("apple"), insert("app"), has_word("app")
    Output: True

    Input:  (nothing inserted), has_word("app"), has_prefix("a")
    Output: False, False
    Why:    edge case, an empty tree contains no words and no prefixes

Approach:
    Each node is a dictionary from a character to the child node, so a word
    is a path from the root and shared prefixes share nodes. A sentinel key
    marks the nodes where a stored word actually ends, which is what
    separates a stored "app" from a mere prefix of "apple". Both queries use
    the same walk and differ only in whether they demand the sentinel at the
    end. Every operation touches one node per character, so each costs O(L)
    for an argument of length L, and the tree uses O(total characters
    stored) space.

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/tries/prefix-tree-operations

Run it:  python problems/tries/04-prefix-tree-operations.py
"""


class PrefixTree:
    def __init__(self):
        self.root = {}
    def insert(self, word):
        node = self.root
        for ch in word:
            node = node.setdefault(ch, {})    # shared prefixes share nodes
        node["$"] = True                      # a whole word ends here
    def _walk(self, s):                       # the node s leads to, or None
        node = self.root
        for ch in s:
            if ch not in node:
                return None
            node = node[ch]
        return node
    def has_word(self, word):
        node = self._walk(word)
        return node is not None and "$" in node
    def has_prefix(self, prefix):
        return self._walk(prefix) is not None


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
    t = PrefixTree(); t.insert("apple")
    check_printed(t.has_word("apple"), t.has_word("app"), t.has_prefix("app"), expect="True False True")
    t.insert("app"); e = PrefixTree()
    check_printed(t.has_word("app"), e.has_word("app"), e.has_prefix("a"), expect="True False False")
