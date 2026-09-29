"""
Halve or Subtract One Steps (easy) · patterns: tail-recursion, bit-counting

Start from a whole number n that is zero or more. In one step, halve it if
it is even, or subtract one if it is odd. Return how many steps it takes to
reach zero. The number can be as large as 2 to the power 1000, so a solution
that makes one recursive call per step will run past Python's default
recursion limit.

Examples:

    Input:  n = 14
    Output: 6
    Why:    14 -> 7 -> 6 -> 3 -> 2 -> 1 -> 0

    Input:  n = 2 ** 1000
    Output: 1001
    Why:    1000 halvings reach 1, and one subtraction reaches 0

    Input:  n = 0
    Output: 0
    Why:    edge case, already at zero, so no steps are taken

Approach:
    With an accumulator, the recursion becomes a tail call: the answer for n
    is the answer for the next number with the counter raised by one, and
    nothing is left to do after the call returns. Python does not remove
    tail calls by itself, so the call is turned into a loop that reassigns n
    and the counter, and the stack never grows. The count also has a closed
    form for n above zero: one step per binary digit after the first, plus
    one per set bit. Time is O(log n) steps, and space is O(1) beyond the
    number itself.

The lesson behind it: Tail Calls and Loops
    https://bytepatterns.com/learn/recursion/tail-recursion
    python recursion/07-tail-recursion.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/recursion/halve-or-subtract-steps

Run it:  python problems/recursion/08-halve-or-subtract-steps.py
"""


def steps_to_zero(n):
    # tail-recursive shape: steps(n, done) = done if n == 0 else steps(next n, done + 1)
    done = 0
    while n:                             # the tail call, as a loop
        n = n // 2 if n % 2 == 0 else n - 1
        done += 1
    return done


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(steps_to_zero(14), 6)
    check(steps_to_zero(2 ** 1000), 1001)
    check(steps_to_zero(0), 0)
