"""
Choose K Modulo A Prime (medium) · patterns: combinatorics, modular-inverse

Count the ways to pick k items out of n distinct items when the order of
picking does not matter, and report the count modulo 1,000,000,007, which is
prime. The value of n can reach a million, so the exact count has hundreds
of thousands of digits and must never be built. Picking more items than
exist gives zero ways.

Examples:

    Input:  n = 5, k = 2
    Output: 10

    Input:  n = 1000, k = 500
    Output: 159835829
    Why:    the exact count has about 300 digits; only its remainder is returned

    Input:  n = 3, k = 5
    Output: 0
    Why:    edge case, there is no way to pick five items out of three

Approach:
    The count equals the falling product n times (n minus 1) down to (n
    minus k plus 1), divided by k factorial. Both products are easy to keep
    reduced modulo the prime, and the division becomes a multiplication by
    the modular inverse of k factorial, which Fermat's little theorem gives
    as that value to the power p minus 2. Because n stays below the prime, k
    factorial is never a multiple of it, so the inverse always exists.
    Swapping k for n minus k when that is smaller halves the work. Time is
    O(min(k, n minus k) plus log p) and space is O(1).

The lesson behind it: Permutations vs Combinations
    https://bytepatterns.com/learn/math-number-theory/counting-permutations-combinations
    python math-number-theory/05-counting-permutations-combinations.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/math-number-theory/choose-k-modulo-prime

Run it:  python problems/math-number-theory/06-choose-k-modulo-prime.py
"""


MOD = 1_000_000_007

def choose(n, k):
    if k < 0 or k > n:
        return 0                               # cannot pick more than exist
    k = min(k, n - k)                          # same count, shorter loop
    top = bottom = 1
    for i in range(k):
        top = top * (n - i) % MOD              # n (n-1) ... (n-k+1)
        bottom = bottom * (i + 1) % MOD        # k!
    return top * pow(bottom, MOD - 2, MOD) % MOD   # divide via Fermat's inverse


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(choose(5, 2), 10)
    check(choose(1000, 500), 159835829)
    check(choose(3, 5), 0)
    check(choose(7, 0), 1)
