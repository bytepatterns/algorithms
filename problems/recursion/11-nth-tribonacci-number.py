"""
Nth Tribonacci Number (easy) · patterns: recurrence, rolling-state

The Tribonacci sequence starts with T(0) = 0, T(1) = 1 and T(2) = 1, and
every later term is the sum of the three before it: T(n) = T(n - 1) + T(n -
2) + T(n - 3). Given n with 0 ≤ n ≤ 37, return T(n).

Examples:

    Input:  n = 4
    Output: 4
    Why:    the sequence runs 0, 1, 1, 2, 4

    Input:  n = 25
    Output: 1389537

    Input:  n = 0
    Output: 0
    Why:    edge case, the first seed value

Approach:
    The recursive definition is correct but recomputes the same terms again
    and again, exactly like the naive Fibonacci in the lesson, only worse,
    since each call spawns three more instead of two. Memoization would fix
    that, but the dependency is so short that there is nothing to cache
    beyond three numbers. The loop keeps T(i), T(i + 1) and T(i + 2) and
    shifts the window one step per iteration, so after n steps the first
    slot holds T(n). Time is O(n) and space is O(1), and n up to 37 keeps
    the answer within a 32-bit integer.

The lesson behind it: Factorial and Fibonacci
    https://bytepatterns.com/learn/recursion/factorial-and-fibonacci
    python recursion/03-factorial-and-fibonacci.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/recursion/nth-tribonacci-number

Run it:  python problems/recursion/11-nth-tribonacci-number.py
"""


def tribonacci(n):
    a, b, c = 0, 1, 1                   # T(0), T(1), T(2)
    for _ in range(n):
        a, b, c = b, c, a + b + c       # slide the window one term forward
    return a


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(tribonacci(4), 4)
    check(tribonacci(25), 1389537)
    check(tribonacci(0), 0)
