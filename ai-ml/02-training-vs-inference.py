"""
Training vs Inference: Learn once, slowly. Answer many times, fast.

Training is the loop that adjusts parameters until predictions match labels.
It is expensive and runs rarely. Inference is a single pass over frozen
parameters to answer one input. Same model, two completely different cost
profiles.

Lesson 2 of AI & ML, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/ai-ml/training-vs-inference

Run it:  python ai-ml/02-training-vs-inference.py
"""


data = [(1.0, "cold"), (2.0, "cold"), (8.0, "hot"), (9.0, "hot")]

# TRAINING: fit one parameter from the labelled examples
cold = [x for x, y in data if y == "cold"]
hot = [x for x, y in data if y == "hot"]
threshold = (sum(cold) / len(cold) + sum(hot) / len(hot)) / 2

# INFERENCE: apply the frozen parameter to a new input
def predict(x):
    return "hot" if x > threshold else "cold"


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
    check_printed(threshold, predict(6.5), expect="5.0 hot")
