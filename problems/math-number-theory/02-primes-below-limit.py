"""
Primes Below A Limit (medium) · patterns: sieve, precomputation

Count how many prime numbers are strictly smaller than a given limit. The
limit can reach a few million, so testing each candidate against its
divisors is far too slow.

Examples:

    Input:  limit = 10
    Output: 4
    Why:    2, 3, 5 and 7

    Input:  limit = 100
    Output: 25

    Input:  limit = 2
    Output: 0
    Why:    edge case, nothing below 2 is prime

Approach:
    Flag every value as a candidate, then walk upwards clearing the
    multiples of each survivor. A survivor has no smaller factor, which is
    exactly what makes it prime, so nothing is ever tested for divisibility.
    The inner clearing can start at the square of the value, because
    anything smaller carries a smaller factor that already cleared it, and
    the outer walk can stop at the square root of the limit for the same
    reason. Time is O(n log log n) and space is O(n) flags.

The lesson behind it: Sieve of Eratosthenes
    https://bytepatterns.com/learn/math-number-theory/sieve-of-eratosthenes
    python math-number-theory/03-sieve-of-eratosthenes.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/math-number-theory/primes-below-limit

Run it:  python problems/math-number-theory/02-primes-below-limit.py
"""


def count_primes(limit):
    if limit < 3:
        return 0                       # nothing below 2 is prime
    ok = [True] * limit
    ok[0] = ok[1] = False
    for p in range(2, int(limit ** 0.5) + 1):
        if ok[p]:                      # p survived, so p is prime
            step = len(range(p * p, limit, p))
            ok[p * p:limit:p] = [False] * step
    return sum(ok)


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(count_primes(10), 4)
    check(count_primes(100), 25)
    check(count_primes(2), 0)
    check(count_primes(3), 1)
