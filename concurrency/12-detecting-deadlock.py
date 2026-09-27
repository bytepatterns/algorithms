"""
Detecting Deadlock: Draw who waits for whom; a closed ring is the proof.

A wait-for graph has one node per thread and an edge from a waiter to the
holder it is blocked on. Following the edges from any thread either runs out
— the chain ends at somebody who is running — or comes back around. That
ring is the deadlock, and breaking it means aborting one member.

Lesson 12 of Concurrency, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/concurrency/detecting-deadlock

Run it:  python concurrency/12-detecting-deadlock.py
"""


waits = {"t1": "t2", "t2": "t3", "t3": "t1", "t4": "t2"}

def stuck(graph, start):
    seen, at = [], start
    while at in graph:                 # who is this one waiting on?
        if at in seen:
            return seen[seen.index(at):]   # a closed ring: nobody can move
        seen.append(at)
        at = graph[at]
    return []                          # chain ends at a thread still running


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(stuck(waits, "t1"), ['t1', 't2', 't3'])
    check(stuck(waits, "t4"), ['t2', 't3', 't1'])  # queued behind it
    freed = {k: v for k, v in waits.items() if k != "t3"}
    check(stuck(freed, "t1"), [])  # abort one victim, ring broken
