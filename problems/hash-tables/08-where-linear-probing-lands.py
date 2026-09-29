"""
Where Linear Probing Lands (medium) · patterns: open-addressing, union-find

A hash table has m slots numbered 0 to m - 1 and uses linear probing. Keys,
all zero or more, are inserted in order: key k aims at slot k mod m, and if
that slot is taken it tries the next one, wrapping from m - 1 back to 0,
until it finds a free slot. There are never more keys than slots. Return the
slot each key ends up in, and avoid re-walking long runs of taken slots,
because a bad hash can pile every key onto one spot.

Examples:

    Input:  m = 7, keys = [10, 3, 17, 24, 5]
    Output: [3, 4, 5, 6, 0]
    Why:    10, 3, 17 and 24 all aim at slot 3 and spread out to 3-6;
            5 finds 5 and 6 taken and wraps around to 0

    Input:  m = 5, keys = [4, 9, 14]
    Output: [4, 0, 1]
    Why:    every key aims at slot 4, so the later ones wrap around

    Input:  m = 1, keys = [42]
    Output: [0]
    Why:    edge case, a one-slot table has only one place to go

Approach:
    Every taken slot is linked to the slot after it, so following links from
    a key's home slot always ends at the first free slot in probe order.
    That is a union-find structure where each free slot is the root of the
    run of taken slots before it. Path compression makes later walks over
    the same run jump straight to its end, so a pile-up is not re-walked
    once per key. With path compression alone, each placement costs O(log m)
    amortised, so time is O(m + n log m), and space is O(m).

The lesson behind it: When Hashing Fails
    https://bytepatterns.com/learn/hash-tables/when-hashing-fails
    python hash-tables/05-when-hashing-fails.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/hash-tables/where-linear-probing-lands

Run it:  python problems/hash-tables/08-where-linear-probing-lands.py
"""


def probe_slots(m, keys):
    nxt = list(range(m))               # a slot at or after s that may still be free
    def first_free(s):
        root = s
        while nxt[root] != root:
            root = nxt[root]
        while nxt[s] != root:          # path compression
            nxt[s], s = root, nxt[s]
        return root
    placed = []
    for k in keys:
        slot = first_free(k % m)
        placed.append(slot)
        nxt[slot] = (slot + 1) % m     # taken: send later probes onwards
    return placed


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(probe_slots(7, [10, 3, 17, 24, 5]), [3, 4, 5, 6, 0])
    check(probe_slots(5, [4, 9, 14]), [4, 0, 1])
    check(probe_slots(1, [42]), [0])
