"""
Least Common Multiple of a List (easy) · patterns: gcd, lcm

Several buses leave the same depot at time zero, and bus i returns every
nums[i] minutes. Return the first positive minute at which all of them are
back at the depot together, which is the least common multiple of the
values. Every value is a positive integer, and the list holds at least one
value.

Examples:

    Input:  nums = [4, 6, 10]
    Output: 60
    Why:    60 is the smallest number divisible by 4, 6 and 10

    Input:  nums = [12, 18, 24]
    Output: 72
    Why:    the values share factors, so the answer is far below their product

    Input:  nums = [9]
    Output: 9
    Why:    edge case, a single bus meets itself on its first return

Approach:
    The least common multiple of two numbers is their product divided by
    their greatest common divisor, because the divisor is exactly the part
    both numbers contribute and the product counts it twice. The operation
    is associative, so the answer for the whole list is built by folding the
    values into a running result one at a time. Dividing the running result
    by the divisor before multiplying keeps every intermediate value no
    larger than the final answer. Each step costs one Euclid call, so time
    is O(n log M) for largest value M, and space is O(1).

The lesson behind it: GCD and Euclid
    https://bytepatterns.com/learn/math-number-theory/gcd-and-euclid
    python math-number-theory/02-gcd-and-euclid.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/math-number-theory/lcm-of-a-list

Run it:  python problems/math-number-theory/07-lcm-of-a-list.py
"""


from math import gcd

def lcm_all(nums):
    result = 1
    for x in nums:
        result = result // gcd(result, x) * x   # divide first: stays small
    return result


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(lcm_all([4, 6, 10]), 60)
    check(lcm_all([12, 18, 24]), 72)
    check(lcm_all([9]), 9)
    check(lcm_all([2, 3, 5, 7, 11, 13]), 30030)
