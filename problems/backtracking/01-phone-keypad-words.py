"""
Phone Keypad Words (medium) · patterns: backtracking, decision-tree

An old phone keypad maps each digit to a small group of letters: 2 to abc, 3
to def, 4 to ghi, 5 to jkl. Given a string of those digits, return every
letter string it could have been typed as. Order the results by taking each
digit's letters left to right. An empty digit string produces no words at
all.

Examples:

    Input:  digits = "23"
    Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    Why:    three letters on 2 times three letters on 3

    Input:  digits = "4"
    Output: ["g", "h", "i"]
    Why:    a single digit contributes one letter per word

    Input:  digits = ""
    Output: []
    Why:    edge case, no digits means no word, not one empty word

Approach:
    This is the plain choose-explore-un-choose loop with the digit index as
    the depth. One shared path list holds the letters picked so far;
    appending is the choice, the recursive call explores it, and popping
    restores the path for the next branch. The base case fires when the
    index reaches the end of the digit string, which is the only point a
    candidate is complete. With k letters per digit and n digits the tree
    has k to the n leaves, so time is O(n times k to the n) and the
    recursion depth is O(n).

The lesson behind it: The Decision Tree
    https://bytepatterns.com/learn/backtracking/the-decision-tree
    python backtracking/01-the-decision-tree.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/backtracking/phone-keypad-words

Run it:  python problems/backtracking/01-phone-keypad-words.py
"""


PADS = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl"}

def keypad_words(digits):
    out = []
    def build(i, path):
        if i == len(digits):        # every digit has contributed a letter
            out.append("".join(path))
            return
        for ch in PADS[digits[i]]:
            path.append(ch)         # choose
            build(i + 1, path)      # explore
            path.pop()              # un-choose
    if digits:
        build(0, [])
    return out


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
    words = keypad_words("23")
    check_printed(len(words), words[0], words[-1], expect="9 ad cf")
    check(keypad_words(""), [])
