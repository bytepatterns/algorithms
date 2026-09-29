"""
Least Frequently Used Cache (hard) · patterns: design, hash-map, frequency-buckets

Build a cache that holds at most capacity keys. A get returns the key's
value, or -1 if it is missing, and counts as a use; a put inserts a key with
one use, or updates an existing key's value and counts as a use. When a new
key arrives while the cache is full, first evict the key with the fewest
uses, and among those the one whose last use is oldest. Given the capacity
and a list of operations, return the results of the get calls, with every
operation in O(1) average time.

Examples:

    Input:  capacity = 2
            ops = put(5, 50), put(6, 60), get(6), get(6), put(7, 70),
                  get(5), put(5, 55), get(7), get(5)
    Output: [60, 60, -1, -1, 55]
    Why:    7 evicts 5 (one use against three); later 5 evicts 7 for the same reason

    Input:  capacity = 2
            ops = put(1, 100), put(2, 200), put(1, 111), get(2), put(3, 300),
                  get(1), get(3)
    Output: [200, -1, 300]
    Why:    1 and 2 both have two uses, and 1 was used longer ago, so 1 goes

    Input:  capacity = 0
            ops = put(1, 1), get(1)
    Output: [-1]
    Why:    edge case, a cache with no room keeps nothing

Approach:
    Keys are grouped by use count, and each group is an ordered dictionary
    with the least recently used key first. The victim is therefore always
    the first key of the lowest group, and the lowest count only changes in
    two ways: a use can empty the lowest group, which raises it by exactly
    one, and a new key sets it back to 1. Every operation touches a constant
    number of dictionary entries. Time is O(1) average per operation, and
    space is O(capacity).

The lesson behind it: LFU: Frequency Buckets
    https://bytepatterns.com/learn/hash-tables/lfu-frequency-buckets
    python hash-tables/08-lfu-frequency-buckets.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/hash-tables/least-frequently-used-cache

Run it:  python problems/hash-tables/10-least-frequently-used-cache.py
"""


from collections import OrderedDict, defaultdict
def run_cache(capacity, ops):
    value, uses, groups = {}, {}, defaultdict(OrderedDict)   # groups: count -> keys, oldest first
    lowest, out = 0, []
    def touch(k):
        nonlocal lowest
        c = uses[k]
        del groups[c][k]
        if not groups[c]:
            del groups[c]
            if lowest == c: lowest = c + 1
        uses[k] = c + 1
        groups[c + 1][k] = None                               # newest in its new group
    for op in ops:
        if op[0] == "get":
            if op[1] in value: touch(op[1])
            out.append(value.get(op[1], -1))
        elif capacity:
            k, v = op[1], op[2]
            if k in value:
                value[k] = v; touch(k); continue
            if len(value) == capacity:
                victim, _ = groups[lowest].popitem(last=False)   # fewest uses, oldest
                if not groups[lowest]: del groups[lowest]
                del value[victim], uses[victim]
            value[k], uses[k], lowest = v, 1, 1
            groups[1][k] = None
    return out


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    first = [("put", 5, 50), ("put", 6, 60), ("get", 6), ("get", 6), ("put", 7, 70),
             ("get", 5), ("put", 5, 55), ("get", 7), ("get", 5)]
    second = [("put", 1, 100), ("put", 2, 200), ("put", 1, 111), ("get", 2),
              ("put", 3, 300), ("get", 1), ("get", 3)]
    check(run_cache(2, first), [60, 60, -1, -1, 55])
    check(run_cache(2, second), [200, -1, 300])
    check(run_cache(0, [("put", 1, 1), ("get", 1)]), [-1])
