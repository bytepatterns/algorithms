"""
Queue Basics: First one in is the first one out.

A queue is open at both ends. Items join at the back and leave from the
front, so the oldest one is always served first. Reach for
collections.deque: removing the front is O(1) there, while list.pop(0) costs
O(n) because everything behind it shifts down a slot.

Lesson 3 of Stacks & Queues, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/stacks-queues/queue-basics

Run it:  python stacks-queues/03-queue-basics.py
"""


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    from collections import deque

    q = deque()
    q.append("job1")         # enqueue at the back -> O(1)
    q.append("job2")
    q.append("job3")

    check(q[0], "job1")  # peek at the front
    check(q.popleft(), "job1")  # the oldest leaves first
    check(q.popleft(), "job2")
    check(list(q), ["job3"])
    # a plain list would need pop(0) here, which is O(n)
