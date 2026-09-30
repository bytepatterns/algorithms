"""
Sieve of Eratosthenes: Cross out what the primes can reach; the rest are prime.

Do not test numbers for primality. Cross out what you already know is
composite.

Take the smallest number nothing has struck: it is prime, because no smaller
value divides it. Strike its multiples, starting at its square, and move on.
Whatever survives is prime by construction, at a cost near n log log n
instead of n divisions each.

Lesson 3 of Math & Number Theory, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/math-number-theory/sieve-of-eratosthenes

Short video on this lesson: https://www.youtube.com/@bytepatterns

Run it:  python math-number-theory/03-sieve-of-eratosthenes.py
"""


def primes_up_to(n):
    ok = [True] * (n + 1)
    ok[0] = ok[1] = False
    for p in range(2, int(n ** 0.5) + 1):
        if ok[p]:                            # p survived, so p is prime
            for k in range(p * p, n + 1, p): # below p*p, someone else struck it
                ok[k] = False
    return [i for i, good in enumerate(ok) if good]


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(primes_up_to(31), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31])
    check(len(primes_up_to(100)), 25)
