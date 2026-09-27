"""
Memoization: Write each answer down once, never solve it twice.

Memoization stores each subproblem's answer the first time you compute it.
Every later call with the same input reads the stored value instead of
recursing again. The shape of the code barely changes, but the cost
collapses from exponential to linear.

Lesson 4 of Recursion, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/recursion/memoization-intro

Run it:  python recursion/04-memoization-intro.py
"""


def fib(n, memo=None):
    if memo is None:
        memo = {}
    if n < 2:
        return n
    if n in memo:                              # solved before: reuse it
        return memo[n]
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(fib(35), 9227465)  # in 35 steps instead of millions
