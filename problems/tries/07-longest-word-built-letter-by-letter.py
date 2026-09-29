"""
Longest Word Built Letter by Letter (medium) · patterns: trie, dfs

A word game lets a player grow a word one letter at a time, adding each
letter to the end, and every intermediate step must itself be a word from
the dictionary. Given the dictionary, return the longest word that can be
built this way starting from a one-letter word. If several words tie on
length, return the alphabetically smallest; if none can be built, return an
empty string.

Examples:

    Input:  words = ["w", "wo", "wor", "worl", "world"]
    Output: "world"

    Input:  words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
    Output: "apple"
    Why:    "apply" is also buildable and just as long, but "apple" sorts first

    Input:  words = ["cat", "ca"]
    Output: ""
    Why:    edge case, "c" is missing, so no chain can start

Approach:
    A word can be built letter by letter exactly when each of its prefixes
    is also a word, which in a prefix tree means every node along its path
    carries an end-of-word marker. So the search walks the tree from the
    root and only descends into children that end a word; branches whose
    next step is not a word are never entered. Every node reached is a
    buildable word, and the answer is the longest one, with ties broken
    alphabetically. Building the tree takes O(total characters), and the
    walk visits each node at most once, so time and space are both O(total
    characters).

The lesson behind it: Trie Basics
    https://bytepatterns.com/learn/tries/trie-basics
    python tries/01-trie-basics.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/tries/longest-word-built-letter-by-letter

Run it:  python problems/tries/07-longest-word-built-letter-by-letter.py
"""


def longest_buildable(words):
    root = {}
    for w in words:
        node = root
        for ch in w:
            node = node.setdefault(ch, {})
        node["$"] = w                          # the word that ends here
    best, stack = "", [root]
    while stack:
        node = stack.pop()
        for ch, child in node.items():
            if ch != "$" and "$" in child:     # only step onto real words
                w = child["$"]
                if len(w) > len(best) or (len(w) == len(best) and w < best):
                    best = w
                stack.append(child)
    return best


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
    check_printed(longest_buildable(["w", "wo", "wor", "worl", "world"]), expect="world")
    check_printed(longest_buildable(["a", "banana", "app", "appl", "ap", "apply", "apple"]), expect="apple")
    check(longest_buildable(["cat", "ca"]) == "", True)
