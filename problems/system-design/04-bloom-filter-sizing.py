"""
Bloom Filter Sizing (medium) · patterns: bloom-filter, double-hashing

A cache sits in front of a database, and lookups for keys that do not exist
at all go straight through it and hit the database every time. A Bloom
filter of known keys can stop most of them: it answers "definitely absent"
or "maybe present". Given the expected number of keys n and the
false-positive rate p you can accept, return the number of bits m = ceil(-n
ln p / (ln 2)²) and the number of hash functions k = round(m / n × ln 2), at
least 1. Then build the filter, deriving its k bit positions from one
SHA-256 digest, and check that it never misses a key it holds while its
false-positive rate stays close to p.

Examples:

    Input:  n = 1000, p = 0.01
    Output: (9586, 7)
    Why:    about 9.6 bits and 7 hashes per key for a 1% false-positive rate

    Input:  n = 1000000, p = 0.001
    Output: (14377588, 10)
    Why:    each tenfold drop in p costs about 4.8 more bits per key

    Input:  n = 10, p = 0.5
    Output: (15, 1)
    Why:    edge case, a very loose target still needs at least one hash function

Approach:
    The sizing formulas come from minimising the false-positive rate for a
    fixed number of bits, and they say the cost grows with log(1/p), not
    with the size of the keys, which is why a filter is so much smaller than
    the key set it guards. Instead of k separate hash functions, double
    hashing cuts two 64-bit numbers from one SHA-256 digest and combines
    them as a + i × b, a standard trick that keeps the accuracy of k
    independent hashes. A key that was added always has all its bits set, so
    the filter never gives a false "absent", which is the property the cache
    relies on; a key that was never added is let through only when all k of
    its bits happen to be set by other keys. With 1,000 keys, 105 of 10,000
    unknown probes slip through, 1.05%, right at the 1% target. Each add or
    lookup is O(k), and the filter takes m bits.

The lesson behind it: Caching
    https://bytepatterns.com/learn/system-design/caching

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/system-design/bloom-filter-sizing

Run it:  python problems/system-design/04-bloom-filter-sizing.py
"""


import hashlib, math

def bloom_size(n, p):
    m = math.ceil(-n * math.log(p) / math.log(2) ** 2)   # bits
    k = max(1, round(m / n * math.log(2)))               # hash functions
    return m, k

class Bloom:
    def __init__(self, n, p):
        self.m, self.k = bloom_size(n, p)
        self.bits = bytearray(self.m)

    def _spots(self, item):
        d = hashlib.sha256(item.encode()).digest()
        a, b = int.from_bytes(d[:8], "big"), int.from_bytes(d[8:16], "big")
        return [(a + i * b) % self.m for i in range(self.k)]   # double hashing

    def add(self, item):
        for s in self._spots(item):
            self.bits[s] = 1

    def might_contain(self, item):
        return all(self.bits[s] for s in self._spots(item))


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(bloom_size(1000, 0.01), (9586, 7))
    check(bloom_size(1_000_000, 0.001), (14377588, 10))
    check(bloom_size(10, 0.5), (15, 1))
    bf = Bloom(1000, 0.01)
    for i in range(1000):
        bf.add(f"key:{i}")
    check(all(bf.might_contain(f"key:{i}") for i in range(1000)), True)
    check(sum(bf.might_contain(f"miss:{i}") for i in range(10000)), 105)
