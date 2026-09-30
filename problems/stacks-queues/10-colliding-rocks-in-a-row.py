"""
Colliding Rocks in a Row (medium) · patterns: stack, pop-while-weaker

Rocks move along a line at the same speed. Each is given as a nonzero
integer: the absolute value is its size, and the sign is its direction,
positive for right and negative for left. When two rocks meet, the smaller
one breaks; if they are the same size, both break. Rocks moving in the same
direction never meet. Return the rocks that remain after every collision, in
their original order. There are between 2 and 10,000 rocks, and each size is
at most 1,000.

Examples:

    Input:  rocks = [5, 10, -5]
    Output: [5, 10]
    Why:    -5 meets 10 and breaks; 5 and 10 move the same way and never meet

    Input:  rocks = [10, 2, -5]
    Output: [10]
    Why:    -5 breaks 2, then meets 10 and breaks itself

    Input:  rocks = [8, -8]
    Output: []
    Why:    edge case, equal sizes break each other

Approach:
    Scanning left to right, the stack holds the rocks that have survived so
    far. A right-mover never hits anything behind it, so it is pushed. A
    left-mover can only meet the right-movers at the top of the stack, and
    it meets the nearest one first, so it keeps popping smaller right-movers
    until it either breaks against a bigger one, cancels out an equal one,
    or reaches a left-mover or the bottom of the stack, in which case it
    survives and is pushed. What remains on the stack is already in the
    original order. Each rock is pushed and popped at most once, so time and
    space are O(n).

The lesson behind it: Monotonic Stack
    https://bytepatterns.com/learn/stacks-queues/monotonic-stack
    python stacks-queues/05-monotonic-stack.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/stacks-queues/colliding-rocks-in-a-row

Run it:  python problems/stacks-queues/10-colliding-rocks-in-a-row.py
"""


def after_collisions(rocks):
    stack = []
    for rock in rocks:
        alive = True
        while alive and rock < 0 and stack and stack[-1] > 0:
            if stack[-1] < -rock:        # the right-mover breaks, keep going
                stack.pop()
                continue
            if stack[-1] == -rock:       # both break
                stack.pop()
            alive = False                # the incoming rock is gone
        if alive:
            stack.append(rock)
    return stack


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(after_collisions([5, 10, -5]), [5, 10])
    check(after_collisions([10, 2, -5]), [10])
    check(after_collisions([8, -8]), [])
    check(after_collisions([-2, -1, 1, 2]), [-2, -1, 1, 2])
