"""
Reverse Words: Flip the word order without disturbing the letters.

Reversing words is not reversing characters. Split the sentence into words,
reverse that list, then join it back with single spaces.

The letters inside each word never move — only the boxes holding them swap
places, which two pointers do in one pass.

Lesson 3 of Strings, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/strings/reverse-words

Run it:  python strings/03-reverse-words.py
"""


def reverse_words(s):
    words = s.split()          # split() also eats runs of spaces
    left, right = 0, len(words) - 1
    while left < right:        # swap the ends, then walk inward
        words[left], words[right] = words[right], words[left]
        left, right = left + 1, right - 1
    return " ".join(words)     # one clean separator


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
    check_printed(reverse_words("the sky is blue"), expect="blue is sky the")
    check_printed(reverse_words("  hello   world  "), expect="world hello")
