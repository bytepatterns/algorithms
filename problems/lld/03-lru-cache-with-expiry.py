"""
LRU Cache With Expiry (medium) · patterns: ordered-dict, lazy-expiry, min-heap

Design a cache class that holds at most capacity entries, where every entry
also has a time to live. put(key, value, ttl, now) stores a value that
expires at now + ttl, replacing any older value for the key. get(key, now)
returns the value, or None once now has reached the expiry time, and a
successful get makes the entry the most recently used. When a put finds the
cache full, it must first throw away entries that have already expired, and
only if that frees nothing may it evict the least recently used live entry.
Time is passed in as a number so the behaviour is deterministic and
testable.

Examples:

    Input:  capacity 2; put("a", 1, ttl=10, now=0), put("b", 2, ttl=100, now=0)
            get("a", now=5), put("c", 3, ttl=100, now=6), get("b", now=7), get("a", now=7)
    Output: [1, None, 1]
    Why:    the get at 5 made "a" recent, so "b" was the one evicted for "c"

    Input:  then get("a", now=10)
    Output: None
    Why:    "a" expired at exactly 10

    Input:  then put("d", 4, ttl=5, now=20), put("e", 5, ttl=5, now=26), get("c", now=27), get("d", now=27)
    Output: [3, None]
    Why:    edge case, "d" had already expired, so it was dropped and "c" survived even though it was older

Approach:
    Two orders matter here, and each gets its own structure: an OrderedDict
    keeps keys in use order for the LRU rule, and a min-heap keeps expiry
    times so the earliest to expire is always on top. A get treats an
    expired entry as missing and removes it; a hit moves the key to the
    recent end. A full put pops expired heap entries first, and because a
    key may have been overwritten or evicted since it was pushed, an entry
    is deleted only when its expiry still matches what the cache holds,
    which is how stale heap entries are skipped without ever searching the
    heap. Only when nothing expired is freed does the least recently used
    entry go. get is O(1), and put is O(log n) amortised, since every heap
    entry is pushed once and popped at most once.

The lesson behind it: LRU Cache
    https://bytepatterns.com/learn/lld/lru-cache-design
    python lld/13-lru-cache-design.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/lld/lru-cache-with-expiry

Run it:  python problems/lld/03-lru-cache-with-expiry.py
"""


import heapq
from collections import OrderedDict

class TTLCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = OrderedDict()          # key -> (value, expires_at), least recent first
        self.expiry = []                   # min-heap of (expires_at, key), may hold stale entries

    def get(self, key, now):
        entry = self.data.get(key)
        if entry is None or entry[1] <= now:
            self.data.pop(key, None)       # an expired entry reads as missing
            return None
        self.data.move_to_end(key)         # a hit makes it the most recent
        return entry[0]

    def put(self, key, value, ttl, now):
        self.data.pop(key, None)
        while len(self.data) >= self.capacity and self.expiry and self.expiry[0][0] <= now:
            at, old = heapq.heappop(self.expiry)
            if old in self.data and self.data[old][1] == at:
                del self.data[old]         # drop something already dead first
        if len(self.data) >= self.capacity:
            self.data.popitem(last=False)  # otherwise evict the least recently used
        self.data[key] = (value, now + ttl)
        heapq.heappush(self.expiry, (now + ttl, key))


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    c = TTLCache(2)
    c.put("a", 1, ttl=10, now=0)
    c.put("b", 2, ttl=100, now=0)
    first = c.get("a", now=5)
    c.put("c", 3, ttl=100, now=6)
    check([first, c.get("b", now=7), c.get("a", now=7)], [1, None, 1])
    check(c.get("a", now=10), None)
    c.put("d", 4, ttl=5, now=20)
    c.put("e", 5, ttl=5, now=26)
    check([c.get("c", now=27), c.get("d", now=27)], [3, None])
