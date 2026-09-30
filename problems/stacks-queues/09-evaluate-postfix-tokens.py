"""
Evaluate Postfix Tokens (easy) · patterns: stack, expression-evaluation

A pocket calculator stores formulas in postfix order, where each operator
comes after its two operands, so "3 4 +" means 3 + 4 and no brackets are
ever needed. Given the formula as a list of tokens, each an integer or one
of +, -, * and /, return its value. Division truncates toward zero, so 7 /
-2 is -3. The formula is always valid, has between 1 and 10,000 tokens,
never divides by zero, and every intermediate value fits in a 32-bit signed
integer.

Examples:

    Input:  tokens = ["2", "1", "+", "3", "*"]
    Output: 9
    Why:    (2 + 1) * 3

    Input:  tokens = ["4", "13", "5", "/", "+"]
    Output: 6
    Why:    4 + (13 / 5), and 13 / 5 truncates to 2

    Input:  tokens = ["10", "6", "9", "3", "+", "-11", "", "/", "", "17", "+", "5", "+"]
    Output: 22
    Why:    negative numbers such as -11 are operands, not operators

Approach:
    In postfix order an operator always applies to the two most recent
    unused values, which is exactly what the top of a stack holds. Numbers
    are pushed; an operator pops the right operand, then the left one, and
    pushes the combined value, so at the end the only value left is the
    answer. The one trap is division: Python's floor division rounds -7 // 2
    down to -4, so the quotient is taken on absolute values and its sign
    restored, which truncates toward zero. A token is an operator only if it
    is exactly one of the four symbols, so "-11" is read as a number. Time
    and space are both O(n).

The lesson behind it: Stack Basics
    https://bytepatterns.com/learn/stacks-queues/stack-basics
    python stacks-queues/01-stack-basics.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/stacks-queues/evaluate-postfix-tokens

Run it:  python problems/stacks-queues/09-evaluate-postfix-tokens.py
"""


def eval_postfix(tokens):
    stack = []
    for tok in tokens:
        if tok not in ("+", "-", "*", "/"):
            stack.append(int(tok))
            continue
        right, left = stack.pop(), stack.pop()     # right operand is on top
        if tok == "+":
            stack.append(left + right)
        elif tok == "-":
            stack.append(left - right)
        elif tok == "*":
            stack.append(left * right)
        else:
            q = abs(left) // abs(right)            # truncate toward zero
            stack.append(q if (left < 0) == (right < 0) else -q)
    return stack[0]


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(eval_postfix(["2", "1", "+", "3", "*"]), 9)
    check(eval_postfix(["4", "13", "5", "/", "+"]), 6)
    check(eval_postfix(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]), 22)
