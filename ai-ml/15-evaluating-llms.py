"""
Evaluating LLMs: If you cannot score it, you cannot improve it.

An evaluation is a fixed set of inputs, an expected outcome for each, and a
scorer. Deterministic checks come first: normalised exact match, a pattern,
does the code run. Softer qualities need a rubric, graded by people or by a
model.

Lesson 15 of AI & ML, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/ai-ml/evaluating-llms

Run it:  python ai-ml/15-evaluating-llms.py
"""


def norm(s):
    return " ".join(s.lower().strip().split()).rstrip(".")


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
    cases = [("Paris", " paris "), ("42", "42."), ("blue", "green")]

    hits = sum(1 for want, got in cases if norm(want) == norm(got))
    check_printed(hits, "/", len(cases), expect="2 / 3")

    raw = sum(1 for want, got in cases if want == got)
    check_printed(raw, "/", len(cases), expect="0 / 3 -> unnormalised scoring lies")
