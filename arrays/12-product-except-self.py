"""
Product Except Self: Two sweeps beat one division.

The answer at index i is everything to its left multiplied by everything to
its right. So make two sweeps. Going left to right, write the running
product of the left side into the output, before folding the current value
in. Then sweep back, multiplying in the running product of the right side.
Each cell meets both halves of the array without ever meeting itself.

Lesson 12 of Arrays, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/arrays/product-except-self

Short video on this lesson: https://www.youtube.com/@bytepatterns

Run it:  python arrays/12-product-except-self.py
"""


def product_except_self(nums):
    out = [1] * len(nums)
    prefix = 1
    for i in range(len(nums)):              # everything left of i
        out[i] = prefix
        prefix *= nums[i]
    suffix = 1
    for i in range(len(nums) - 1, -1, -1):  # fold in everything right of i
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
    check(product_except_self([2, 3, 4, 5]), [60, 40, 30, 24])
