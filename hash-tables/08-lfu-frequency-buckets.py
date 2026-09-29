"""
LFU: Frequency Buckets: Group keys by use count and eviction becomes O(1).

Least-frequently-used eviction has to find the lowest count fast, and
scanning every key is O(n). So keep one bucket per count, each an ordered
list, plus a note of the lowest non-empty count. A hit moves its key from
bucket c to bucket c+1; an eviction pops the front of the lowest bucket —
least used, and oldest among those. The lowest count only ever rises when a
promotion empties its bucket.

Lesson 8 of Hash Tables, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/hash-tables/lfu-frequency-buckets

Short video on this lesson: https://www.youtube.com/@bytepatterns

Run it:  python hash-tables/08-lfu-frequency-buckets.py
"""


def touch(count, buckets, least, key):
    c = count[key]
    buckets[c].remove(key)
    if not buckets[c]:
        del buckets[c]
        if least == c:
            least = c + 1          # the only way the floor ever rises
    count[key] = c + 1
    buckets.setdefault(c + 1, []).append(key)
    return least

def evict(count, buckets, least):
    key = buckets[least].pop(0)    # least used, and oldest among those
    del count[key]
    return key


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
    count, buckets = {"a": 1, "b": 1}, {1: ["a", "b"]}
    check_printed(touch(count, buckets, 1, "a"), buckets, expect="1 {1: ['b'], 2: ['a']}")
