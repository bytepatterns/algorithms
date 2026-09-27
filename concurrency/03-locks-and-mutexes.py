"""
Locks and Mutexes: One thread inside, everybody else waits.

A mutex is a single token. A thread takes it before touching shared state
and returns it after; anyone else asking must wait. The rule that makes it
work is boring: every access to that state, without exception, goes through
the same lock.

Lesson 3 of Concurrency, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/concurrency/locks-and-mutexes

Run it:  python concurrency/03-locks-and-mutexes.py
"""


import threading

counter = 0
lock = threading.Lock()

def bump(times):
    global counter
    for _ in range(times):
        with lock:              # released automatically, even on error
            counter += 1


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    workers = [threading.Thread(target=bump, args=(50000,)) for _ in range(4)]
    for w in workers: w.start()
    for w in workers: w.join()
    check(counter, 200000)  # every single run
