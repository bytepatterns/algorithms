"""
Evaluate Sums With Brackets (hard) · patterns: stack, expression-parsing, sign-tracking

A spreadsheet cell holds a formula made of non-negative integers, +, -,
round brackets and spaces. A - may also be unary, as in "-(2 + 3)" or "1 -
(-2)". Return the value of the formula without calling any built-in
evaluator. The formula is valid, is at most 300,000 characters long, and
every intermediate value fits in a 32-bit signed integer, so the parser must
run in linear time.

Examples:

    Input:  s = "1 + 1"
    Output: 2

    Input:  s = "(1+(4+5+2)-3)+(6+8)"
    Output: 23

    Input:  s = "-(2 + 3) - (1 - 10)"
    Output: 4
    Why:    a unary minus in front of a bracket flips the sign of its whole value

Approach:
    Without brackets the formula is a running total: digits build the
    current number, and each + or - adds that number with the pending sign
    and sets the sign for the next one. A bracket is a sub-formula with its
    own running total, and the only context it needs from outside is the
    total so far and the sign written in front of it. So an opening bracket
    pushes that pair and resets, and a closing bracket finishes the inner
    total, pops the pair and folds the inner value back in with its sign. A
    unary minus needs no special case, because it simply sets the pending
    sign before a number or a bracket while the total is still unchanged.
    Each character is handled once, so time is O(n), and the stack holds at
    most one entry per open bracket, so space is O(depth).

The lesson behind it: Valid Parentheses
    https://bytepatterns.com/learn/stacks-queues/valid-parentheses
    python stacks-queues/02-valid-parentheses.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/stacks-queues/evaluate-sums-with-brackets

Run it:  python problems/stacks-queues/11-evaluate-sums-with-brackets.py
"""


def evaluate(s):
    total, num, sign, stack = 0, 0, 1, []
    for ch in s:
        if ch.isdigit():
            num = num * 10 + int(ch)
        elif ch in "+-":
            total += sign * num
            num, sign = 0, (1 if ch == "+" else -1)
        elif ch == "(":
            stack.append((total, sign))        # context outside the bracket
            total, sign = 0, 1
        elif ch == ")":
            total += sign * num
            num = 0
            outer_total, outer_sign = stack.pop()
            total = outer_total + outer_sign * total
    return total + sign * num


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(evaluate("1 + 1"), 2)
    check(evaluate("(1+(4+5+2)-3)+(6+8)"), 23)
    check(evaluate("-(2 + 3) - (1 - 10)"), 4)
    check(evaluate(" 2-1 + 2 "), 3)
