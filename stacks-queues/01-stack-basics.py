"""
Stack Basics: Last one in is the first one out.

A stack only lets you touch one end: the top. Push puts an item there, pop
takes the newest one back off. Both are O(1) because nothing else in the
pile moves. The price is that older items are buried until you clear what
sits above them.

Lesson 1 of Stacks & Queues, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/stacks-queues/stack-basics

Run it:  python stacks-queues/01-stack-basics.py
"""


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    stack = []

    stack.append("a")        # push -> O(1)
    stack.append("b")
    stack.append("c")        # stack is ["a", "b", "c"]

    check(stack[-1], "c")  # peek: look, do not remove
    check(stack.pop(), "c")  # the newest leaves first
    check(stack.pop(), "b")
    check(stack, ["a"])
    check(len(stack) == 0, False)  # still one item left
