"""
Encode and Decode Strings: Send the length first and no character is special.

Joining parts with a separator breaks the moment a payload contains that
separator. Prefix each part with its length instead: 5#hello. The decoder
reads digits up to the marker, then copies exactly that many characters
without looking at them. Empty strings survive, every byte is legal inside a
payload, and decoding stays linear because nothing is ever scanned twice.

Lesson 11 of Strings, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/strings/encode-decode-strings

Run it:  python strings/11-encode-decode-strings.py
"""


def encode(parts):
    return "".join(f"{len(p)}#{p}" for p in parts)

def decode(s):
    out, i = [], 0
    while i < len(s):
        j = s.index("#", i)              # the length ends at the first #
        n = int(s[i:j])
        out.append(s[j + 1 : j + 1 + n])
        i = j + 1 + n                    # jump the whole payload
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
    check_printed(encode(["hi", "a#b", ""]), expect="2#hi3#a#b0#")
    check(decode("2#hi3#a#b0#"), ['hi', 'a#b', ''])
