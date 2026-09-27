"""
Which Sort When?: The right sort is the one that fits your data's shape.

Ask three questions: how big is the input, what do you already know about
it, and does stability matter. Small or nearly sorted favours insertion
sort, and small integer ranges favour counting sort. Everything else goes to
quick or merge sort.

Lesson 8 of Sorting, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/sorting/which-sort-when

Run it:  python sorting/08-which-sort-when.py
"""


def choose_sort(n, nearly_sorted, small_int_range, needs_stable):
    if n <= 32 or nearly_sorted:
        return "insertion sort"       # tiny overhead wins
    if small_int_range:
        return "counting sort"        # O(n + k), no comparisons
    if needs_stable:
        return "merge sort"           # stable, guaranteed n log n
    return "quick sort"               # fast in place, average n log n


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
    check_printed(choose_sort(1000, False, False, True), expect="merge sort")
