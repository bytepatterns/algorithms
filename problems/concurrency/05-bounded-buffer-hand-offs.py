"""
Bounded Buffer Hand-Offs (hard) · patterns: bounded-queue, event-simulation, fifo-fairness

Producers and consumers share a blocking queue that holds at most capacity
items. You get the calls in the order they happened: ("put", producer, item)
or ("take", consumer). A put on a full queue blocks its producer, and a take
on an empty queue blocks its consumer. Blocked callers wake in the order
they blocked: a take that frees a slot lets the oldest blocked producer add
its item, and a put while consumers are blocked hands its item straight to
the oldest of them. With capacity 0 the queue stores nothing, so every item
must pass directly from a producer to a consumer. Return the deliveries as
(consumer, item) pairs in order, and the producers still blocked at the end.

Examples:

    Input:  capacity = 1, calls = put P1 a, put P2 b, take C1, take C2, take C1, put P1 c
    Output: ([('C1', 'a'), ('C2', 'b'), ('C1', 'c')], [])
    Why:    P2 blocks until C1's take makes room; C1's second take blocks until c arrives

    Input:  capacity = 2, calls = take C1, put P1 x, put P1 y, put P2 z, put P2 w
    Output: ([('C1', 'x')], ['P2'])
    Why:    x goes straight to the waiting C1, y and z fill the queue, and w has nowhere to go

    Input:  capacity = 0, calls = put P1 q, take C1, take C2
    Output: ([('C1', 'q')], [])
    Why:    edge case, a zero-capacity queue is a rendezvous, so C2 is left waiting

Approach:
    The queue behaves like a condition-variable monitor, so the simulation
    keeps the monitor's state: the stored items plus two FIFO waiting lines,
    one for blocked producers holding their item and one for blocked
    consumers. A put first checks for a waiting consumer, because a consumer
    can only be waiting when the queue is empty, so handing over directly is
    what the real queue does; otherwise it stores the item or blocks. A take
    that removes an item frees exactly one slot, which the oldest blocked
    producer fills at once, so items leave in the order they were offered.
    The capacity 0 case never stores anything, which is why a take also
    checks the producer line when the queue is empty. Every call is O(1)
    with deques, so time is O(n) for n calls and space is O(n).

The lesson behind it: Producer and Consumer
    https://bytepatterns.com/learn/concurrency/producer-consumer
    python concurrency/06-producer-consumer.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/concurrency/bounded-buffer-hand-offs

Run it:  python problems/concurrency/05-bounded-buffer-hand-offs.py
"""


from collections import deque

def run_buffer(capacity, calls):
    buf, parked_puts, parked_takes, got = deque(), deque(), deque(), []
    for kind, who, *item in calls:
        if kind == "put":
            if parked_takes:               # a consumer is waiting: hand over directly
                got.append((parked_takes.popleft(), item[0]))
            elif len(buf) < capacity:
                buf.append(item[0])
            else:
                parked_puts.append((who, item[0]))     # full: the producer blocks
        elif buf:
            got.append((who, buf.popleft()))
            if parked_puts:                # the freed slot wakes the oldest producer
                buf.append(parked_puts.popleft()[1])
        elif parked_puts:                  # capacity 0: take straight from a producer
            got.append((who, parked_puts.popleft()[1]))
        else:
            parked_takes.append(who)       # empty: the consumer blocks
    return got, [who for who, _ in parked_puts]


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    one = [("put", "P1", "a"), ("put", "P2", "b"), ("take", "C1"), ("take", "C2"), ("take", "C1"), ("put", "P1", "c")]
    two = [("take", "C1"), ("put", "P1", "x"), ("put", "P1", "y"), ("put", "P2", "z"), ("put", "P2", "w")]
    zero = [("put", "P1", "q"), ("take", "C1"), ("take", "C2")]
    check(run_buffer(1, one), ([('C1', 'a'), ('C2', 'b'), ('C1', 'c')], []))
    check(run_buffer(2, two), ([('C1', 'x')], ['P2']))
    check(run_buffer(0, zero), ([('C1', 'q')], []))
