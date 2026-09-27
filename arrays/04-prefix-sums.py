"""
Prefix Sums: Pay once up front, answer range queries instantly.

Precompute running totals so that prefix[i] holds the sum of everything
before index i. Any range sum then becomes a single subtraction. You build
in O(n) and answer each query in O(1).

Lesson 4 of Arrays, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/arrays/prefix-sums

Run it:  python arrays/04-prefix-sums.py
"""


def build_prefix(nums):
    prefix = [0]
    for x in nums:
        prefix.append(prefix[-1] + x)   # running total
    return prefix

def range_sum(prefix, i, j):
    # sum of nums[i..j] inclusive, in O(1)
    return prefix[j + 1] - prefix[i]


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
    p = build_prefix([3, 1, 4, 1, 5])   # [0, 3, 4, 8, 9, 14]
    check_printed(range_sum(p, 1, 3), expect="1 + 4 + 1 = 6")
