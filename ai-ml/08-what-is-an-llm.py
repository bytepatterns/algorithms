"""
What Is an LLM: A next-token predictor trained on a lot of text.

A large language model has one job: given the tokens so far, score every
possible next token. Answering, translating and writing code all fall out of
running that prediction in a loop, feeding each choice back in.

Lesson 8 of AI & ML, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/ai-ml/what-is-an-llm

Run it:  python ai-ml/08-what-is-an-llm.py
"""


text = "the cat sat on the mat the cat ran"
words = text.split()

nxt = {}
for a, b in zip(words, words[1:]):      # count what follows what
    nxt.setdefault(a, []).append(b)

def most_likely(word):                  # a real model conditions on
    options = nxt[word]                 # thousands of tokens, not one
    return max(set(options), key=options.count)


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
    check(nxt["the"], ['cat', 'mat', 'cat'])
    check_printed(most_likely("the"), expect="cat")
