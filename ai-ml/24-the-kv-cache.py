"""
The KV Cache: Keep the past keys and values so each new token is cheap.

Attention at each step looks back over every earlier token's key and value.
Those depend only on the prefix, so they never change. Keeping them turns
each step from "redo the whole prefix" into "project one new token and read
the cache".

Lesson 24 of AI & ML, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/ai-ml/the-kv-cache

Run it:  python ai-ml/24-the-kv-cache.py
"""


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
    n = 100
    redo = sum(range(1, n + 1))   # every step re-projects the whole prefix
    cached = n                    # every step projects exactly one token
    check_printed(redo, cached, round(redo / cached, 1), expect="5050 100 50.5")

    layers, heads, dim, width = 32, 32, 128, 2     # width = bytes per number
    per_token = 2 * layers * heads * dim * width   # keys and values
    check_printed(per_token, round(per_token * 8192 / 1e9, 2), expect="524288 4.29")
