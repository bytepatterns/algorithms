"""
Wildcard Word Search (medium) · patterns: trie, backtracking

Build a dictionary from a list of words, then answer search queries where a
. in the query matches any single character. A query matches only if some
stored word has exactly the same length and agrees on every non-dot
position.

Examples:

    Input:  words = ["bad", "dad", "mad"], query = ".ad"
    Output: True
    Why:    the dot can stand for b, d or m

    Input:  words = ["bad", "dad", "mad"], query = "pad"
    Output: False
    Why:    no stored word starts with p

    Input:  words = ["bad"], query = "ba"
    Output: False
    Why:    edge case, a prefix is not a stored word

Approach:
    A nested-dictionary trie stores each word once along a path, with a
    sentinel key marking where a word ends. A concrete character narrows the
    search to one child; a dot forks into all of them, which is the only
    place backtracking happens. A query with no dots costs O(m) for length
    m. Each dot multiplies the work by the branching factor, so the worst
    case is O(26^d · m) for d dots — still far cheaper than scanning every
    word when dots are few.

The lesson behind it: Trie Basics
    https://bytepatterns.com/learn/tries/trie-basics
    python tries/01-trie-basics.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/tries/wildcard-word-search

Run it:  python problems/tries/01-wildcard-word-search.py
"""


def build(words):
    root = {}
    for w in words:
        node = root
        for ch in w:
            node = node.setdefault(ch, {})   # shared prefixes share nodes
        node["$"] = True                     # sentinel: a word ends here
    return root

def search(node, pattern, i=0):
    if i == len(pattern):
        return "$" in node                   # a prefix is not a word
    ch = pattern[i]
    if ch != ".":
        return ch in node and search(node[ch], pattern, i + 1)
    return any(search(kid, pattern, i + 1) for k, kid in node.items() if k != "$")


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
    t = build(["bad", "dad", "mad"])
    check_printed(search(t, ".ad"), search(t, "pad"), expect="True False")
    check(search(build(["bad"]), "ba"), False)
