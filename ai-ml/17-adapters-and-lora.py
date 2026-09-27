"""
Adapters and LoRA: Train a thin correction instead of the whole weight matrix.

Full fine-tuning rewrites every weight, which means a full copy of the model
per task. A low-rank adapter instead learns two thin matrices whose product
has the same shape as the layer, and adds it. The base weights never move,
so one base can serve many tasks.

Lesson 17 of AI & ML, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/ai-ml/adapters-and-lora

Run it:  python ai-ml/17-adapters-and-lora.py
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
    d, r = 4096, 8                  # layer width, adapter rank
    full = d * d                    # a full fine-tune rewrites all of these
    adapter = 2 * d * r             # A is d×r, B is r×d
    check_printed(full, adapter, expect="16777216 65536")
    check_printed(round(100 * adapter / full, 2), "%", expect="0.39 %")
    # merged weight = W + B @ A -> same shape, so serving cost is unchanged
