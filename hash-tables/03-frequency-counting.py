"""
Frequency Counting: One pass, one counter per distinct value.

A surprising number of questions collapse into counting: the most common
item, the first value that repeats, whether two collections hold the same
multiset. Build a map from value to count in one pass, then read the answer
off the map. Rescanning the list per item would cost O(n²).

Lesson 3 of Hash Tables, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/hash-tables/frequency-counting

Run it:  python hash-tables/03-frequency-counting.py
"""


def top_item(items):
    counts = {}
    for item in items:
        # first sighting starts at 0, every later one adds a tick
        counts[item] = counts.get(item, 0) + 1
    return max(counts, key=counts.get)     # highest tally wins


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
    birds = ["robin", "crow", "robin", "wren", "crow", "robin"]
    check_printed(top_item(birds), expect="robin")
    check(len(set(birds)), 3)  # distinct species
