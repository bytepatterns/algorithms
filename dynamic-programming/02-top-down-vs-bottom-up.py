"""
Top-Down vs Bottom-Up: One recurrence, two directions: recurse and cache, or fill a table.

Two directions, one recurrence. Top-down starts at the full problem,
recurses, and caches whatever it meets — so it touches only the subproblems
it actually needs. Bottom-up starts at the base cases and fills a table
forward, so every dependency is ready before it is read. Top-down is easier
to derive from the recursion; bottom-up avoids deep call stacks.

Lesson 2 of Dynamic Programming, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/dynamic-programming/top-down-vs-bottom-up

Run it:  python dynamic-programming/02-top-down-vs-bottom-up.py
"""


def top_down(n, memo):
    if n < 2:
        return n
    if n not in memo:                                        # solve on demand
        memo[n] = top_down(n - 1, memo) + top_down(n - 2, memo)
    return memo[n]

def bottom_up(n):
    table = [0, 1] + [0] * (n - 1)                           # base cases first
    for i in range(2, n + 1):                                # dependency order
        table[i] = table[i - 1] + table[i - 2]
    return table[n]


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
    check_printed(top_down(30, {}), bottom_up(30), expect="832040 832040")
