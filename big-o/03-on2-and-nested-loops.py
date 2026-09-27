"""
O(n²) and Nested Loops: Every pair costs you. Nested loops explode fast.

When a loop runs inside another loop over the same data, you do n units of
work n times. That is O(n²). It feels perfectly fine on ten items and
freezes solid on ten thousand.

Lesson 3 of Big-O, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/big-o/on2-and-nested-loops

Run it:  python big-o/03-on2-and-nested-loops.py
"""


def has_duplicate(nums):
    n = len(nums)
    # outer loop picks each item...
    for i in range(n):
        # ...inner loop compares it against the rest
        for j in range(i + 1, n):
            if nums[i] == nums[j]:
                return True
    return False


if __name__ == "__main__":
    # roughly n*n/2 comparisons -> O(n^2)
    print("Defines has_duplicate. Import this file to use it.")
