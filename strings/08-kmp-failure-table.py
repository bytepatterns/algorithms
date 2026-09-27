"""
Build the KMP Table: Every prefix remembers its longest border.

The table holds one number per position: the length of the longest proper
prefix of the pattern that is also a suffix ending there. That is the
border. Build it by matching the pattern against itself with a carried
border length k. On a mismatch, fall back to the border of that border —
table[k - 1] — instead of restarting. Later, a search that breaks at
position i reads the table and resumes without re-reading the text.

Lesson 8 of Strings, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/strings/kmp-failure-table

Run it:  python strings/08-kmp-failure-table.py
"""


def failure_table(p):
    table = [0] * len(p)
    k = 0                            # length of the current border
    for i in range(1, len(p)):
        while k and p[i] != p[k]:
            k = table[k - 1]         # fall back to a shorter border
        if p[i] == p[k]:
            k += 1
        table[i] = k
    return table


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(failure_table("ababaca"), [0, 0, 1, 2, 3, 0, 1])
