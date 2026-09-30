"""
Largest Group by Shared Factor (hard) · patterns: union-find, prime-factors

You are given a list of distinct positive integers. Two numbers are linked
when they share a common factor greater than 1, and links chain, so numbers
that are linked through others belong to the same group. Return the size of
the largest group.

Examples:

    Input:  nums = [4, 6, 15, 35]
    Output: 4
    Why:    4 and 6 share 2, 6 and 15 share 3, 15 and 35 share 5, so all four form one group

    Input:  nums = [20, 50, 9, 63]
    Output: 2
    Why:    20 and 50 share 2 and 5, 9 and 63 share 3, and nothing links the two pairs

    Input:  nums = [1, 7]
    Output: 1
    Why:    edge case, 1 has no factor greater than 1, so every group has a single number

Approach:
    Linking numbers directly needs a check for every pair, but a shared
    factor greater than 1 always means a shared prime, so each number only
    has to be unioned with its own prime factors and the primes do the rest.
    The disjoint set holds two kinds of nodes, numbers and primes, and union
    by size attaches the smaller tree under the larger one so the trees stay
    shallow while path halving flattens them further on every find. Because
    the tree sizes include the prime nodes, the answer counts only numbers
    per root at the end. Factoring by trial division takes O(√v) per number,
    so time is O(n · √V) for largest value V, plus near-constant work per
    union, and space is O(n) for the numbers and their primes.

The lesson behind it: Union by Rank or Size
    https://bytepatterns.com/learn/union-find/union-by-size
    python union-find/03-union-by-size.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/union-find/largest-group-by-shared-factor

Run it:  python problems/union-find/10-largest-group-by-shared-factor.py
"""


from collections import Counter

def largest_group(nums):
    parent, size = {}, {}

    def find(x):
        parent.setdefault(x, x)
        size.setdefault(x, 1)
        while parent[x] != x:
            parent[x] = parent[parent[x]]        # path halving
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return
        if size[ra] < size[rb]:                  # union by size: small tree under big
            ra, rb = rb, ra
        parent[rb] = ra
        size[ra] += size[rb]

    for v in nums:
        find(("num", v))
        x, p = v, 2
        while p * p <= x:                        # trial division
            if x % p == 0:
                union(("num", v), ("prime", p))
                while x % p == 0:
                    x //= p
            p += 1
        if x > 1:                                # a prime factor above the square root
            union(("num", v), ("prime", x))
    groups = Counter(find(("num", v)) for v in nums)   # count numbers only
    return max(groups.values(), default=0)


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(largest_group([4, 6, 15, 35]), 4)
    check(largest_group([20, 50, 9, 63]), 2)
    check(largest_group([1, 7]), 1)
