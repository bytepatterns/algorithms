"""
Multiply Digit Strings (medium) · patterns: digit-arithmetic, carry-propagation

Two non-negative whole numbers are given as text, most significant digit
first, and may be far too long to fit in a machine integer. Return their
product, also as text. Converting the inputs to built-in numbers is not
allowed, and the result must carry no leading zeros.

Examples:

    Input:  a = "123", b = "456"
    Output: "56088"

    Input:  a = "9", b = "99"
    Output: "891"
    Why:    the carry out of the last column adds a digit

    Input:  a = "0", b = "52"
    Output: "0"
    Why:    edge case, a zero factor must not produce a padded result

Approach:
    Each pair of digits contributes to a fixed output column, so all the
    products can be accumulated into a slot array before any carrying
    happens; that separation is what keeps the code short. A product of an
    i-digit and a j-digit number never needs more than i+j slots, which
    sizes the array up front. A single right-to-left sweep then normalises
    every slot to one digit, and stripping leading zeros finishes the job,
    with the zero factor handled up front so nothing is stripped away
    entirely. Time is O(i times j), and space is O(i + j).

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/strings/multiply-digit-strings

Run it:  python problems/strings/04-multiply-digit-strings.py
"""


def multiply_digits(a, b):
    if a == "0" or b == "0":
        return "0"                   # otherwise the sweep would strip everything
    slots = [0] * (len(a) + len(b))  # a product never needs more columns than this
    for i in range(len(a) - 1, -1, -1):
        for j in range(len(b) - 1, -1, -1):
            slots[i + j + 1] += int(a[i]) * int(b[j])   # the column is fixed by i and j
    for k in range(len(slots) - 1, 0, -1):
        slots[k - 1] += slots[k] // 10                  # carry the tens leftwards
        slots[k] %= 10
    return "".join(str(d) for d in slots).lstrip("0")


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
    check_printed(multiply_digits("123", "456"), expect="56088")
    check_printed(multiply_digits("9", "99"), expect="891")
    check_printed(multiply_digits("0", "52"), expect="0")
