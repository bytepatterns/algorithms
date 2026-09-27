"""
Backtracking: Choose, explore, then undo the choice and try the next.

Backtracking builds an answer one choice at a time. Make a choice, recurse
to extend it, and when the path dead-ends, undo that choice and try the next
option. The undo step is what lets a single shared list serve the entire
search.

Lesson 5 of Recursion, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/recursion/backtracking-intro

Run it:  python recursion/05-backtracking-intro.py
"""


def permute(left, path, out):
    if not left:                 # complete: record this answer
        out.append(path[:])
        return
    for i, x in enumerate(left):
        path.append(x)                            # choose
        permute(left[:i] + left[i + 1:], path, out)
        path.pop()                                # un-choose


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
    out = []
    permute(["a", "b", "c"], [], out)
    check_printed(len(out), out[0], expect="6 ['a', 'b', 'c']")
