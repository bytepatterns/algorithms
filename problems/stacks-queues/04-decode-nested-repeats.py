"""
Decode Nested Repeats (medium) · patterns: stack, string-parsing

An encoded text uses the form k[segment], meaning the segment is repeated k
times. The repeat count k is a positive whole number that may have several
digits, and a segment may itself contain further encoded segments. Expand
the encoding and return the plain text.

Examples:

    Input:  text = "3[a]2[bc]"
    Output: "aaabcbc"

    Input:  text = "2[ab3[c]]"
    Output: "abcccabccc"
    Why:    the inner segment expands first, then the outer one repeats the result

    Input:  text = "xyz"
    Output: "xyz"
    Why:    edge case, text with no encoding passes through unchanged

Approach:
    Brackets nest, so the contexts they open must be closed in reverse
    order, which is exactly what a stack provides. Each opening bracket
    parks the text built so far together with the count that applies to the
    segment about to start, and each closing bracket retrieves them and
    folds the finished segment in. Digits are accumulated as a running
    number so multi-digit counts work, and text with no brackets simply
    never touches the stack. Time is O(length of the output) and space is
    O(depth of nesting plus the output).

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/stacks-queues/decode-nested-repeats

Run it:  python problems/stacks-queues/04-decode-nested-repeats.py
"""


def decode_repeats(text):
    stack, current, count = [], [], 0
    for ch in text:
        if ch.isdigit():
            count = count * 10 + int(ch)     # a count may span several digits
        elif ch == "[":
            stack.append((current, count))   # park the outer context
            current, count = [], 0
        elif ch == "]":
            outer, times = stack.pop()       # resume the context we parked
            outer.append("".join(current) * times)
            current = outer
        else:
            current.append(ch)
    return "".join(current)


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
    check_printed(decode_repeats("3[a]2[bc]"), expect="aaabcbc")
    check_printed(decode_repeats("2[ab3[c]]"), expect="abcccabccc")
    check_printed(decode_repeats("xyz"), expect="xyz")
