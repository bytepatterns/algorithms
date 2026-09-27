"""
Factorial and Fibonacci: One call per step, or two calls that redo everything.

Factorial recurses once per step, so its calls form a straight line n frames
deep and cost O(n). Naive Fibonacci recurses twice, so the calls fan out
into a tree and the same subproblems get solved over and over — roughly
O(2^n).

Lesson 3 of Recursion, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/recursion/factorial-and-fibonacci

Run it:  python recursion/03-factorial-and-fibonacci.py
"""


def factorial(n):
    if n <= 1:                       # base case
        return 1
    return n * factorial(n - 1)      # one branch: a straight line

def fib(n):
    if n < 2:
        return n                     # fib(0) = 0, fib(1) = 1
    return fib(n - 1) + fib(n - 2)   # two branches: a tree


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(factorial(5), 120)
    check(fib(10), 55)
