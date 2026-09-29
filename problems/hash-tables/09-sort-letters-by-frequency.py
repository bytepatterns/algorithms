"""
Sort Letters by Frequency (medium) · patterns: bucket-sort, counting

Rearrange the characters of a string so that equal characters sit together
and the groups appear from most frequent to least frequent. When two
characters appear equally often, the one whose first appearance in the input
is earlier goes first. Return the rearranged string, and do it without a
comparison sort over the characters.

Examples:

    Input:  text = "banana"
    Output: "aaannb"
    Why:    a appears 3 times, n twice and b once

    Input:  text = "mississippi"
    Output: "iiiissssppm"
    Why:    i and s both appear 4 times, and i shows up first in the input

    Input:  text = ""
    Output: ""
    Why:    edge case, nothing to rearrange

Approach:
    A count is a whole number between 1 and the length of the string, so a
    list of buckets indexed by count sorts the characters in linear time.
    Python dictionaries keep insertion order, so the counter lists
    characters by first appearance, and filling the buckets in that order
    settles every tie. Walking the buckets from the top writes the most
    frequent group first. Time is O(n), and space is O(n) for the buckets
    and the output.

The lesson behind it: Top K Without a Heap
    https://bytepatterns.com/learn/hash-tables/top-k-buckets
    python hash-tables/07-top-k-buckets.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/hash-tables/sort-letters-by-frequency

Run it:  python problems/hash-tables/09-sort-letters-by-frequency.py
"""


from collections import Counter
def by_frequency(text):
    counts = Counter(text)                     # keys in first-appearance order
    buckets = [[] for _ in range(len(text) + 1)]
    for ch, c in counts.items():
        buckets[c].append(ch)                  # ties stay in first-appearance order
    parts = []
    for c in range(len(text), 0, -1):          # most frequent bucket first
        for ch in buckets[c]:
            parts.append(ch * c)
    return "".join(parts)


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
    check_printed(by_frequency("banana"), expect="aaannb")
    check_printed(by_frequency("mississippi"), expect="iiiissssppm")
    check_printed(by_frequency(""), expect="(empty string)")
