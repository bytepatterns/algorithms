"""
Pack a Word List Into One String (easy) · patterns: length-prefix, string-parsing

Write pack(words), which turns a list of strings into one string, and
unpack(text), which turns that string back into the original list. Each word
is written as its length in decimal, then a #, then the word itself. Words
can be empty and can contain any character, including digits and #, so
unpack must never search for a separator inside a word.

Examples:

    Input:  words = ["hi", "#1"]
    Output: pack   -> "2#hi2##1"
            unpack -> ["hi", "#1"]
    Why:    after reading "2#", the next two characters are taken whole, "#" or not

    Input:  words = ["", "a"]
    Output: pack   -> "0#1#a"
    Why:    an empty word still gets its length, so it survives the round trip

    Input:  words = []
    Output: pack   -> ""
            unpack -> []
    Why:    edge case, nothing to write and nothing to read

Approach:
    The length prefix tells the reader exactly how many characters to take,
    so the contents of a word never matter. Reading a length is safe because
    a length is only digits, which makes the first # after it the true end
    of the number. Each character is visited a constant number of times
    while packing and while unpacking. Time is O(L) for L total characters,
    and space is O(L) for the output.

The lesson behind it: Encode and Decode Strings
    https://bytepatterns.com/learn/strings/encode-decode-strings
    python strings/11-encode-decode-strings.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/strings/pack-a-word-list

Run it:  python problems/strings/14-pack-a-word-list.py
"""


def pack(words):
    return "".join(f"{len(w)}#{w}" for w in words)

def unpack(text):
    words, i = [], 0
    while i < len(text):
        hash_at = text.index("#", i)        # end of the length digits
        n = int(text[i:hash_at])
        words.append(text[hash_at + 1:hash_at + 1 + n])
        i = hash_at + 1 + n                 # jump over the word, never into it
    return words


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
    check_printed(pack(["hi", "#1"]), expect="2#hi2##1")
    check(unpack("2#hi2##1"), ['hi', '#1'])
    check(unpack(pack(["", "a"])), ['', 'a'])
    check(unpack(pack([])), [])
