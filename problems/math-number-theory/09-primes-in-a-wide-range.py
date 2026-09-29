"""
Primes in a Wide Range (hard) · patterns: segmented-sieve, sieve

Count the primes p with lo ≤ p ≤ hi. The bounds can be as large as 10^12,
far too large to sieve from 1, but the window itself is narrow: hi minus lo
is at most 10^6. Values below 2 inside the window are not prime and simply
do not count.

Examples:

    Input:  lo = 10, hi = 30
    Output: 6
    Why:    11, 13, 17, 19, 23 and 29

    Input:  lo = 1000000000000, hi = 1000000001000
    Output: 37
    Why:    only the 1,001 values of the window are sieved, not the trillion below them

    Input:  lo = 14, hi = 16
    Output: 0
    Why:    edge case, a window with no primes in it

Approach:
    Every composite value up to hi has a prime factor no larger than the
    square root of hi, so an ordinary sieve up to that root supplies every
    prime that can ever cross something out. The window then gets its own
    array of flags, indexed by value minus lo, and each small prime marks
    its multiples inside the window, starting at p squared or at the first
    multiple of p not below lo, whichever is later, so no prime crosses
    itself out. Slice assignment on a bytearray does each run of crossings
    in one step. Time is O(sqrt(hi) log log hi plus (hi minus lo) log log
    hi) and space is O(sqrt(hi) plus hi minus lo).

The lesson behind it: Sieve of Eratosthenes
    https://bytepatterns.com/learn/math-number-theory/sieve-of-eratosthenes
    python math-number-theory/03-sieve-of-eratosthenes.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/math-number-theory/primes-in-a-wide-range

Run it:  python problems/math-number-theory/09-primes-in-a-wide-range.py
"""


from math import isqrt

def primes_between(lo, hi):
    lo = max(lo, 2)                          # 0 and 1 are not prime
    if lo > hi:
        return 0
    root = isqrt(hi)
    small, base = bytearray([1]) * (root + 1), []
    for p in range(2, root + 1):             # ordinary sieve up to sqrt(hi)
        if small[p]:
            base.append(p)
            small[p * p::p] = bytearray(len(small[p * p::p]))
    alive = bytearray([1]) * (hi - lo + 1)   # one flag per value in the window
    for p in base:
        start = max(p * p, (lo + p - 1) // p * p)
        alive[start - lo::p] = bytearray(len(alive[start - lo::p]))
    return sum(alive)


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(primes_between(10, 30), 6)
    check(primes_between(10**12, 10**12 + 1000), 37)
    check(primes_between(14, 16), 0)
    check(primes_between(1, 10), 4)
