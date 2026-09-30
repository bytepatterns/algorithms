"""
Next Letter After the Target (easy) · patterns: binary-search, upper-bound

You are given a list of lowercase letters sorted in non-decreasing order,
containing at least two different letters, and a target letter. Return the
smallest letter in the list that is strictly greater than the target. If no
letter is greater, wrap around and return the first letter of the list.

Examples:

    Input:  letters = ["c", "f", "j"], target = "a"
    Output: "c"

    Input:  letters = ["c", "f", "f", "j"], target = "f"
    Output: "j"
    Why:    strictly greater means both copies of f are skipped

    Input:  letters = ["c", "f", "j"], target = "j"
    Output: "c"
    Why:    edge case, nothing is greater than j, so the answer wraps to the front

Approach:
    The first letter strictly greater than the target is an upper bound, one
    of the boundary searches where the loop keeps a half-open range and
    never returns early. Letters less than or equal to the target push lo
    past the middle, larger letters pull hi down to it, so when the two
    meet, lo is the first index holding a greater letter. If every letter is
    less than or equal to the target, lo ends at the length of the list, and
    taking it modulo the length turns that into the wrap to the front. Time
    is O(log n) and space is O(1).

The lesson behind it: Binary Search Variants
    https://bytepatterns.com/learn/searching/binary-search-variants
    python searching/03-binary-search-variants.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/searching/next-letter-after-the-target

Run it:  python problems/searching/11-next-letter-after-the-target.py
"""


def next_letter(letters, target):
    lo, hi = 0, len(letters)
    while lo < hi:                        # find the first letter greater than target
        mid = (lo + hi) // 2
        if letters[mid] <= target:
            lo = mid + 1
        else:
            hi = mid
    return letters[lo % len(letters)]     # past the end wraps to the front


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
    check_printed(next_letter(["c", "f", "j"], "a"), expect="c")
    check_printed(next_letter(["c", "f", "f", "j"], "f"), expect="j")
    check_printed(next_letter(["c", "f", "j"], "j"), expect="c")
