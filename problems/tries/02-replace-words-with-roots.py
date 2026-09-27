"""
Replace Words With Roots (medium) · patterns: trie, prefix-match

You are given a list of root words and a sentence of space-separated words.
Replace every word in the sentence that begins with one of the roots by that
root. When several roots match the same word, use the shortest one. Words
matching no root are left alone.

Examples:

    Input:  roots = ["cat", "bat", "rat"], sentence = "the cattle was rattled by the battery"
    Output: "the cat was rat by the bat"
    Why:    each replaced word starts with a stored root

    Input:  roots = ["a", "aa"], sentence = "aaa aab"
    Output: "a a"
    Why:    the shortest matching root wins, so "aa" never applies

    Input:  roots = ["xy"], sentence = "x"
    Output: "x"
    Why:    edge case, the word is shorter than any root

Approach:
    Insert every root into a trie with a sentinel marking its final node.
    Then walk each sentence word down the trie: the first sentinel
    encountered is by construction the shortest matching root, so the scan
    stops immediately. Falling off the trie means no root matches. Building
    costs O(total root length); each word costs at most its own length.
    Total time is O(R + S) over root and sentence characters, with O(R)
    space.

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/tries/replace-words-with-roots

Run it:  python problems/tries/02-replace-words-with-roots.py
"""


def replace_words(roots, sentence):
    trie = {}
    for r in roots:
        node = trie
        for ch in r:
            node = node.setdefault(ch, {})
        node["$"] = True                        # a root ends here
    out = []
    for word in sentence.split():
        node, cut = trie, None
        for i, ch in enumerate(word):
            if ch not in node:
                break                           # fell off: no root matches
            node = node[ch]
            if "$" in node:
                cut = i + 1                     # first hit is the shortest root
                break
        out.append(word[:cut] if cut else word)
    return " ".join(out)


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
    check_printed(replace_words(["cat", "bat", "rat"], "the cattle was rattled by the battery"), expect="the cat was rat by the bat")
    check_printed(replace_words(["a", "aa"], "aaa aab"), "|", replace_words(["xy"], "x"), expect="a a | x")
