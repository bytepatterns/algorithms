"""
Maximum XOR Pair (hard) · patterns: bit-trie, greedy

Given a list of non-negative integers, return the largest value obtainable
by taking the bitwise XOR of two of them. The two may be the same element
only if that element appears twice.

Examples:

    Input:  nums = [3, 10, 5, 25, 2, 8]
    Output: 28
    Why:    5 XOR 25 is 28, and no other pair beats it

    Input:  nums = [8, 10, 2]
    Output: 10
    Why:    8 XOR 2 is 10, which beats 8 XOR 10 and 10 XOR 2

    Input:  nums = [1, 1]
    Output: 0
    Why:    edge case, identical values cancel to zero

Approach:
    A binary trie stores each number as a path of bits from the top down.
    Because the highest differing bit dominates the result, the best partner
    for a number is found by always steering toward the opposite bit and
    only falling back when that branch is empty — a greedy choice that is
    safe precisely because one high bit outweighs every lower bit together.
    Each of the n numbers is inserted once and queried once over b bits,
    giving O(n·b) time and O(n·b) space instead of O(n²).

The lesson behind it: Trie vs Hash Set
    https://bytepatterns.com/learn/tries/trie-vs-hash-set
    python tries/04-trie-vs-hash-set.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/tries/maximum-xor-pair

Run it:  python problems/tries/03-maximum-xor-pair.py
"""


def max_xor(nums):
    bits = max(max(nums).bit_length(), 1)
    root = {}
    for n in nums:                              # insert, most significant first
        node = root
        for b in range(bits - 1, -1, -1):
            node = node.setdefault((n >> b) & 1, {})
    best = 0
    for n in nums:
        node, value = root, 0
        for b in range(bits - 1, -1, -1):
            want = 1 - ((n >> b) & 1)           # a differing bit sets a 1
            if want in node:
                value |= 1 << b
                node = node[want]
            else:
                node = node[1 - want]
        best = max(best, value)
    return best


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
    check_printed(max_xor([3, 10, 5, 25, 2, 8]), max_xor([8, 10, 2]), max_xor([1, 1]), expect="28 10 0")
