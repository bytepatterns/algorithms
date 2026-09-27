"""
LRU Cache: A map that can find, a list that can reorder, one object.

Two structures, one job each. A map finds a key in one step but stores no
order; a doubly linked list reorders in one step but cannot find.

Keep the node in the map. Every touch unlinks it and relinks it at the
front, so the tail is always the least recently used — and evicting it is
O(1).

Lesson 13 of Low-Level Design, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/lld/lru-cache-design

Run it:  python lld/13-lru-cache-design.py
"""


from collections import OrderedDict     # a hash map *plus* a linked list

class LRU:
    def __init__(self, cap): self.cap, self.box = cap, OrderedDict()
    def get(self, k):
        if k not in self.box: return -1
        self.box.move_to_end(k)                     # unlink, relink at front
        return self.box[k]
    def put(self, k, v):
        self.box[k] = v; self.box.move_to_end(k)
        if len(self.box) > self.cap: self.box.popitem(last=False)   # drop tail


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
    c = LRU(2); c.put("a", 1); c.put("b", 2); c.get("a"); c.put("c", 3)
    check_printed(list(c.box), c.get("b"), expect="['a', 'c'] -1")
