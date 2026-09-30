"""
Value at a Point in Time (medium) · patterns: binary-search, upper-bound, versioned-store

A config service keeps every version of every setting. set(key, value, t)
records that key took value at time t, and for any one key the times always
arrive in strictly increasing order. get(key, t) returns the value the key
had at time t, meaning the value from the latest set with time at most t, or
"" if the key had no value yet. There are up to 200,000 calls in total and
times go up to 10^7, so a get must not scan all of a key's versions.

Examples:

    Input:  set("theme", "light", 1), get("theme", 1), get("theme", 3),
            set("theme", "dark", 4), get("theme", 4), get("theme", 5)
    Output: ["light", "light", "dark", "dark"]
    Why:    at time 3 the latest version is still the one written at 1

    Input:  set("port", "80", 10), get("port", 9), get("port", 10)
    Output: ["", "80"]
    Why:    before time 10 the key has no value yet

    Input:  get("missing", 7)
    Output: [""]
    Why:    edge case, a key that was never set

Approach:
    Each key gets two parallel lists, one of times and one of values.
    Because set is called with increasing times for a key, appending keeps
    the time list sorted without any extra work, so set is O(1). A lookup
    wants the rightmost time that is at most t, and bisect_right answers
    exactly that: it returns the position where t would be inserted after
    any equal times, so everything before that position is at most t. A
    position of 0 means no version is old enough and the answer is the empty
    string; otherwise the value just before it is the one in effect. Each
    get costs O(log v) for v versions of the key, and space is O(total
    calls).

The lesson behind it: Binary Search
    https://bytepatterns.com/learn/searching/binary-search
    python searching/02-binary-search.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/searching/value-at-a-point-in-time

Run it:  python problems/searching/10-value-at-a-point-in-time.py
"""


from bisect import bisect_right

class VersionedStore:
    def __init__(self):
        self.times, self.values = {}, {}

    def set(self, key, value, t):
        self.times.setdefault(key, []).append(t)     # times stay sorted
        self.values.setdefault(key, []).append(value)

    def get(self, key, t):
        i = bisect_right(self.times.get(key, []), t) # versions with time <= t
        return self.values[key][i - 1] if i else ""


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    store = VersionedStore()
    store.set("theme", "light", 1)
    early = [store.get("theme", 1), store.get("theme", 3)]
    store.set("theme", "dark", 4)
    store.set("port", "80", 10)
    check(early + [store.get("theme", 4), store.get("theme", 5)], ['light', 'light', 'dark', 'dark'])
    check([store.get("port", 9), store.get("port", 10)], ['', '80'])
    check([store.get("missing", 7)], [''])
