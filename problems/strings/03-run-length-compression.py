"""
Run Length Compression (medium) · patterns: two-pointers, run-length-encoding

Shrink a piece of text by replacing each run of identical characters with
that character followed by the length of the run. A run of length one keeps
the bare character with no number after it. Return the compressed text only
when it is strictly shorter than the original; otherwise return the original
unchanged.

Examples:

    Input:  text = "aaabccdddd"
    Output: "a3bc2d4"
    Why:    the lone b stays bare while the longer runs pick up a count

    Input:  text = "abcd"
    Output: "abcd"
    Why:    compressing would not shrink anything, so the original wins

    Input:  text = ""
    Output: ""
    Why:    edge case, there is no run to encode

Approach:
    Two positions describe the current run: one marks its start and a scout
    walks to its end, which makes the run length a simple subtraction. Each
    run contributes its character, plus a count only when the run is longer
    than one, so short runs are never inflated. The final length comparison
    honours the rule that compression must actually pay for itself. Time is
    O(n) because the scout never revisits a character, and space is O(n) for
    the built output.

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/strings/run-length-compression

Run it:  python problems/strings/03-run-length-compression.py
"""


def compress_runs(text):
    out, i = [], 0
    while i < len(text):
        j = i
        while j < len(text) and text[j] == text[i]:
            j += 1                   # walk to the end of this run
        out.append(text[i])
        if j - i > 1:                # runs of length one stay bare
            out.append(str(j - i))
        i = j                        # continue from where the run ended
    packed = "".join(out)
    return packed if len(packed) < len(text) else text


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
    check_printed(compress_runs("aaabccdddd"), expect="a3bc2d4")
    check_printed(compress_runs("abcd"), expect="abcd")
    check_printed(compress_runs(""), expect="")
