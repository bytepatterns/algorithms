"""
Product Of Others (medium) · patterns: prefix-products, two-pass

Given a list of integers, build a new list of the same length where each
position holds the product of every other value in the input. The value at
that position itself is left out of its own product. Solve it without using
division, since a single zero in the input would make division impossible.

Examples:

    Input:  nums = [2, 3, 4, 5]
    Output: [60, 40, 30, 24]
    Why:    345, 245, 235, 234

    Input:  nums = [1, 0, 3]
    Output: [0, 3, 0]
    Why:    only the slot facing the zero escapes it

    Input:  nums = [0, 0, 7]
    Output: [0, 0, 0]
    Why:    edge case, two zeros wipe out every position

Approach:
    Every answer is the product of a prefix and a suffix, so two sweeps are
    enough. The first pass writes the running product of all earlier values
    into each slot, and the second pass multiplies in the running product of
    all later values while walking backwards. The output list doubles as the
    scratch space, so no extra structure is needed. Time is O(n) for the two
    passes, and space is O(1) beyond the returned list.

The lesson behind it: Product Except Self
    https://bytepatterns.com/learn/arrays/product-except-self
    python arrays/12-product-except-self.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/arrays/product-of-others

Run it:  python problems/arrays/03-product-of-others.py
"""


def products_excluding_self(nums):
    n = len(nums)
    out = [1] * n
    prefix = 1                       # product of everything to the left
    for i in range(n):
        out[i] = prefix
        prefix *= nums[i]
    suffix = 1                       # product of everything to the right
    for i in range(n - 1, -1, -1):
        out[i] *= suffix
        suffix *= nums[i]
    return out


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(products_excluding_self([2, 3, 4, 5]), [60, 40, 30, 24])
    check(products_excluding_self([1, 0, 3]), [0, 3, 0])
    check(products_excluding_self([0, 0, 7]), [0, 0, 0])
