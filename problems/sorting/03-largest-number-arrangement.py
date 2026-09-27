"""
Largest Number Arrangement (medium) · patterns: custom-comparator, sorting

Given non-negative whole numbers, glue them together in some order so the
resulting number is as large as possible, and return it as text. Each number
is used exactly once and its own digits are never rearranged. A result made
only of zeros must read as a single zero.

Examples:

    Input:  nums = [3, 30, 34, 5, 9]
    Output: "9534330"
    Why:    34 must come before 3, which must come before 30

    Input:  nums = [10, 2]
    Output: "210"
    Why:    the larger number is not the one that belongs first

    Input:  nums = [0, 0]
    Output: "0"
    Why:    edge case, gluing zeros must not produce a padded result

Approach:
    Ordering by value is wrong, but the pairwise question has an exact
    answer: a should precede b when a glued in front of b reads larger than
    the other way round. That rule is a valid ordering, so handing it to the
    sort places every number correctly in one go. The only wrinkle is an
    input of all zeros, where gluing produces a run of zeros that must
    collapse to a single one. Time is O(n log n) comparisons on short texts,
    and space is O(n).

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/sorting/largest-number-arrangement

Run it:  python problems/sorting/03-largest-number-arrangement.py
"""


from functools import cmp_to_key
def largest_arrangement(nums):
    words = [str(x) for x in nums]
    # a comes first when gluing it in front produces the larger text
    def order(a, b):
        return (b + a > a + b) - (b + a < a + b)
    words.sort(key=cmp_to_key(order))
    glued = "".join(words)
    return glued.lstrip("0") or "0"  # all zeros must not collapse to nothing


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
    check_printed(largest_arrangement([3, 30, 34, 5, 9]), expect="9534330")
    check_printed(largest_arrangement([10, 2]), expect="210")
    check_printed(largest_arrangement([0, 0]), expect="0")
