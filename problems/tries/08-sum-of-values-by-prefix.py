"""
Sum of Values by Prefix (easy) · patterns: trie, design

Design a store of string keys with integer values and two operations.
put(key, value) sets the value of a key, replacing the old value if the key
is already stored. total(prefix) returns the sum of the values of all keys
that start with the prefix, or 0 if there are none. Both operations should
cost time proportional to the length of their argument.

Examples:

    Input:  put("apple", 3), total("ap"), put("app", 2), total("ap"), total("apple")
    Output: 3, 5, 3
    Why:    after both puts, "ap" begins both keys and "apple" begins only one

    Input:  put("apple", 3), put("app", 2), put("apple", 5), total("ap")
    Output: 7
    Why:    the second put of "apple" replaces 3 with 5 rather than adding to it

    Input:  put("apple", 3), total("b")
    Output: 0
    Why:    edge case, no key starts with the prefix

Approach:
    Each node of the prefix tree keeps the sum of the values of every key
    whose path passes through it, so the answer for a prefix is simply the
    number stored at the prefix's node. A put changes that sum on exactly
    the nodes along the key's path, and only by the difference between the
    new value and the old one, which a separate dictionary remembers; this
    is what makes overwriting a key correct instead of double counting it.
    Both operations touch one node per character, so each costs O(L) for an
    argument of length L, and the tree uses O(total characters stored)
    space.

The lesson behind it: Prefix Search
    https://bytepatterns.com/learn/tries/prefix-search-and-autocomplete
    python tries/02-prefix-search-and-autocomplete.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/tries/sum-of-values-by-prefix

Run it:  python problems/tries/08-sum-of-values-by-prefix.py
"""


class PrefixSums:
    def __init__(self):
        self.root, self.value = {"#": 0}, {}
    def put(self, key, val):
        delta = val - self.value.get(key, 0)   # overwrite, do not double count
        self.value[key] = val
        node = self.root
        node["#"] += delta                     # the empty prefix covers all
        for ch in key:
            node = node.setdefault(ch, {"#": 0})
            node["#"] += delta                 # every prefix of key gains delta
    def total(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node:
                return 0
            node = node[ch]
        return node["#"]


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
    s = PrefixSums(); s.put("apple", 3)
    check(s.total("ap"), 3)
    s.put("app", 2)
    check_printed(s.total("ap"), s.total("apple"), expect="5 3")
    s.put("apple", 5)
    check_printed(s.total("ap"), s.total("b"), expect="7 0")
