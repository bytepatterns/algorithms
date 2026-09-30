"""
Alien Alphabet Order (hard) · patterns: topological-sort, graph-from-constraints

A recovered dictionary from an unknown language uses lowercase English
letters, but in a different alphabetical order. Given its words, already
sorted by that unknown order, return a string of every letter that appears,
arranged in an order consistent with the dictionary. When several letters
could come next, take the one that is earliest in the English alphabet, so
the answer is unique. If no order fits the words, return an empty string.
There are up to 100 words of up to 100 letters each.

Examples:

    Input:  words = ["wrt", "wrf", "er", "ett", "rftt"]
    Output: "wertf"
    Why:    the neighbouring pairs give t before f, w before e, r before t and e before r

    Input:  words = ["z", "x", "z"]
    Output: ""
    Why:    z must come before x and x before z, a contradiction

    Input:  words = ["abc", "ab"]
    Output: ""
    Why:    edge case, a word cannot come before its own prefix in any order

Approach:
    Comparing neighbouring words at their first differing position gives one
    ordering fact each, an edge from the earlier letter to the later one;
    comparing words further apart adds nothing new, since the order is
    transitive. Two cases break the input: a word followed by its own proper
    prefix, and a cycle among the edges. Kahn's algorithm then outputs
    letters with no remaining incoming edge, and using a min-heap as its
    queue picks the earliest English letter whenever there is a choice,
    which makes the answer unique. If the heap empties before every letter
    is placed, the leftover letters sit on a cycle. With L total letters in
    the words and at most 26 distinct letters, time is O(L), and space is
    O(1) beyond the input.

The lesson behind it: Topological Sort
    https://bytepatterns.com/learn/graphs/topological-sort
    python graphs/08-topological-sort.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/graphs/alien-alphabet-order

Run it:  python problems/graphs/20-alien-alphabet-order.py
"""


import heapq

def alien_order(words):
    letters = {ch for w in words for ch in w}
    after = {ch: set() for ch in letters}
    indegree = {ch: 0 for ch in letters}
    for a, b in zip(words, words[1:]):
        for x, y in zip(a, b):
            if x != y:
                if y not in after[x]:
                    after[x].add(y)            # x comes before y
                    indegree[y] += 1
                break
        else:
            if len(a) > len(b):
                return ""                      # a word before its own prefix
    ready = [ch for ch in letters if indegree[ch] == 0]
    heapq.heapify(ready)
    out = []
    while ready:
        ch = heapq.heappop(ready)              # smallest letter that is free to go
        out.append(ch)
        for nxt in after[ch]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                heapq.heappush(ready, nxt)
    return "".join(out) if len(out) == len(letters) else ""   # leftovers mean a cycle


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
    check_printed(alien_order(["wrt", "wrf", "er", "ett", "rftt"]), expect="wertf")
    check(alien_order(["z", "x", "z"]), "")
    check(alien_order(["abc", "ab"]), "")
    check_printed(alien_order(["ab", "adc"]), expect="abcd")
