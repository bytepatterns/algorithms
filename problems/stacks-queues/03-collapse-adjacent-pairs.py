"""
Collapse Adjacent Pairs (easy) · patterns: stack, string-scan

Given a piece of text, repeatedly delete any two neighbouring characters
that are identical. Deleting a pair pulls the surrounding characters
together, which may create a new neighbouring pair to delete. Keep going
until no such pair is left and return what remains.

Examples:

    Input:  text = "abbaca"
    Output: "ca"
    Why:    removing bb leaves aaca, and removing aa leaves ca

    Input:  text = "azxxzy"
    Output: "ay"
    Why:    deleting xx creates zz, which then deletes too

    Input:  text = "aa"
    Output: ""
    Why:    edge case, everything cancels and nothing is left

Approach:
    A stack holds the part of the answer built so far, and its top is always
    the character a newcomer would sit next to. A match therefore cancels by
    popping instead of pushing, which also exposes the character underneath
    as the new neighbour, so chains of cancellations happen automatically
    without rescanning. Each character is pushed and popped at most once.
    Time is O(n) and space is O(n) for the stack.

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/stacks-queues/collapse-adjacent-pairs

Run it:  python problems/stacks-queues/03-collapse-adjacent-pairs.py
"""


def collapse_pairs(text):
    stack = []
    for ch in text:
        if stack and stack[-1] == ch:
            stack.pop()              # the pair annihilates, exposing the one below
        else:
            stack.append(ch)
    return "".join(stack)


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
    check_printed(collapse_pairs("abbaca"), expect="ca")
    check_printed(collapse_pairs("azxxzy"), expect="ay")
    check_printed(collapse_pairs("aa"), expect="")
