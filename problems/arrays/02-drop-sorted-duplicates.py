"""
Drop Sorted Duplicates (easy) · patterns: two-pointers, in-place

A list of integers arrives sorted in non-decreasing order, so equal values
sit next to each other in runs. Compact the list in place so every distinct
value appears exactly once, in the original order. Return the count k of
distinct values; the first k slots must hold them, and whatever remains
after those slots is ignored.

Examples:

    Input:  nums = [1, 1, 2, 3, 3, 3]
    Output: 3, and nums begins with [1, 2, 3]

    Input:  nums = [4, 4, 4]
    Output: 1, and nums begins with [4]
    Why:    one long run collapses to a single value

    Input:  nums = []
    Output: 0
    Why:    edge case, an empty list keeps nothing

Approach:
    Two indexes walk the same list: a reader visits every element, and a
    writer marks the slot for the next distinct value. Because equal values
    are adjacent in sorted input, the reader only needs to compare against
    the last kept value to detect a new run. Copying happens only at run
    boundaries, so no extra list is allocated. Time is O(n) and space is
    O(1).

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/arrays/drop-sorted-duplicates

Run it:  python problems/arrays/02-drop-sorted-duplicates.py
"""


def compact_sorted(nums):
    if not nums:                     # nothing to keep in an empty list
        return 0
    write = 1                        # slot for the next distinct value
    for read in range(1, len(nums)):
        # sorted input means a new value shows up only at a run boundary
        if nums[read] != nums[write - 1]:
            nums[write] = nums[read]
            write += 1
    return write


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
    a = [1, 1, 2, 3, 3, 3]
    check_printed(compact_sorted(a), a[:3], expect="3 [1, 2, 3]")
    b = [4, 4, 4]
    check_printed(compact_sorted(b), b[:1], expect="1 [4]")
    check(compact_sorted([]), 0)
