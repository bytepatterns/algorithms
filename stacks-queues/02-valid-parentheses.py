"""
Valid Parentheses: A closing bracket must answer the newest opening one.

Push every opening bracket. When a closing bracket shows up, it has to match
the one on top — the most recently opened. Anything else means the string is
broken. One pass, O(n), and valid input finishes with an empty stack.

Lesson 2 of Stacks & Queues, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/stacks-queues/valid-parentheses

Short video on this lesson: https://www.youtube.com/@bytepatterns

Run it:  python stacks-queues/02-valid-parentheses.py
"""


def is_valid(s):
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    for ch in s:
        if ch in "([{":
            stack.append(ch)              # remember this opening
        elif not stack or stack.pop() != pairs[ch]:
            return False                  # wrong or missing partner
    return not stack                      # leftovers mean unclosed


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(is_valid("{[()]}"), True)
    check(is_valid("(]"), False)
    check(is_valid("(("), False)
