"""
Consistent Hashing Ring (medium) · patterns: consistent-hashing, virtual-nodes, bisect

A sharded store places keys on database nodes with a consistent hashing
ring. Every node is hashed onto the ring 100 times, as "node#0" to
"node#99", to spread its share evenly. A key belongs to the first node point
at or after the key's own hash, going clockwise and wrapping around past the
top. Use the first 8 hex digits of MD5 as the hash so the placement is
identical on every machine. Build the ring and its owner(key) lookup, then
show the property that makes it worth using: when a fourth node joins, only
the keys it takes over move, and they all move to it.

Examples:

    Input:  nodes = db-a, db-b, db-c; owner("user:42") before and after db-d joins
    Output: db-c db-c

    Input:  keys user:0 to user:999, then db-d joins
    Output: 251 {'db-d'}
    Why:    about a quarter of the keys move, and every one of them moves to the new node

    Input:  a ring with the single node "solo"; owners of user:0, user:1, user:2
    Output: ['solo', 'solo', 'solo']
    Why:    edge case, every lookup wraps around to the only node

Approach:
    A ring compares hashes instead of dividing by the node count, so a new
    node only claims the arcs just before each of its own points, and every
    key that moves goes to the new node while all others stay put. The ring
    is a sorted list of virtual points, and bisect finds the first point at
    or after a key's hash in O(log p); taking the index modulo the number of
    points handles the wrap past the top. Virtual nodes matter because three
    points would split the ring into very uneven arcs, while a hundred per
    node averages the shares out. MD5 is used only as a stable, well-spread
    hash, not for security, and Python's built-in hash would not do because
    it is randomised for strings on every run. Building the ring is O(p log
    p) for p points, and each lookup is O(log p).

The lesson behind it: Database Sharding
    https://bytepatterns.com/learn/system-design/database-sharding

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/system-design/consistent-hashing-ring

Run it:  python problems/system-design/03-consistent-hashing-ring.py
"""


import bisect, hashlib

def h(text):
    return int(hashlib.md5(text.encode()).hexdigest()[:8], 16)   # stable across runs

class Ring:
    def __init__(self, nodes, vnodes=100):
        self.points = sorted((h(f"{n}#{i}"), n) for n in nodes for i in range(vnodes))
        self.hashes = [p for p, _ in self.points]

    def owner(self, key):
        i = bisect.bisect_left(self.hashes, h(key)) % len(self.points)   # next point clockwise
        return self.points[i][1]


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
    keys = [f"user:{i}" for i in range(1000)]
    before = Ring(["db-a", "db-b", "db-c"])
    after = Ring(["db-a", "db-b", "db-c", "db-d"])
    moved = [k for k in keys if before.owner(k) != after.owner(k)]
    check_printed(before.owner("user:42"), after.owner("user:42"), expect="db-c db-c")
    check_printed(len(moved), {after.owner(k) for k in moved}, expect="251 {'db-d'}")
    check([Ring(["solo"]).owner(k) for k in keys[:3]], ['solo', 'solo', 'solo'])
