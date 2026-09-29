"""
Two-Stack Queue Operations (easy) · patterns: two-stacks, amortized

Build a first-in, first-out queue from two stacks, using only push to the
top, pop from the top and a read of the top. Process a list of operations:
["push", x] adds x, ["pop"] removes and reports the oldest value, and
["peek"] reports it without removing it. Return the reported values in
order, reporting None when pop or peek finds the queue empty. Each operation
should cost O(1) amortized time.

Examples:

    Input:  ops = [["push", 1], ["push", 2], ["peek"], ["pop"],
                   ["push", 3], ["pop"], ["pop"]]
    Output: [1, 1, 2, 3]
    Why:    values leave in the order they arrived

    Input:  ops = [["push", 7], ["pop"], ["push", 8], ["push", 9], ["peek"]]
    Output: [7, 8]
    Why:    after 7 leaves, 8 is the oldest value left

    Input:  ops = [["pop"], ["push", 4], ["peek"]]
    Output: [None, 4]
    Why:    edge case, popping an empty queue reports None

Approach:
    New values go onto an inbox stack. Pops and peeks read from an outbox
    stack, and only when the outbox is empty is the whole inbox poured into
    it, which reverses the arrivals so the oldest ends up on top. Pouring
    into an outbox that still holds values would bury older values under
    newer ones, so the empty check is what keeps the order right. Each value
    is pushed twice and popped twice at most, so m operations cost O(m) in
    total, which is O(1) amortized per operation. Space is O(n) for the
    stored values.

The lesson behind it: Queue From Two Stacks
    https://bytepatterns.com/learn/stacks-queues/queue-with-two-stacks
    python stacks-queues/04-queue-with-two-stacks.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/stacks-queues/two-stack-queue-operations

Run it:  python problems/stacks-queues/07-two-stack-queue-operations.py
"""


def run_queue(ops):
    inbox, outbox, out = [], [], []
    for op in ops:
        if op[0] == "push":
            inbox.append(op[1])
            continue
        if not outbox:
            while inbox:                  # reverse once: the oldest ends on top
                outbox.append(inbox.pop())
        if not outbox:
            out.append(None)              # the queue is empty
        elif op[0] == "pop":
            out.append(outbox.pop())
        else:
            out.append(outbox[-1])
    return out


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(run_queue([["push", 1], ["push", 2], ["peek"], ["pop"], ["push", 3], ["pop"], ["pop"]]), [1, 1, 2, 3])
    check(run_queue([["push", 7], ["pop"], ["push", 8], ["push", 9], ["peek"]]), [7, 8])
    check(run_queue([["pop"], ["push", 4], ["peek"]]), [None, 4])
