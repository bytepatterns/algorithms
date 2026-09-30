"""
Deadlocked Threads in a Wait Graph (medium) · patterns: wait-for-graph, cycle-detection

A lock monitor takes a snapshot of a running process. holds maps each held
lock to the thread holding it, and waits maps each blocked thread to the one
lock it is waiting for; a thread waits for at most one lock at a time. A
thread is deadlocked when following "waits for a lock held by" from it leads
back to itself. Return the deadlocked threads, sorted. Threads that are
merely stuck behind a deadlock, without being on the cycle themselves, are
not part of the answer.

Examples:

    Input:  holds = {"a": "T1", "b": "T2"}, waits = {"T1": "b", "T2": "a"}
    Output: ['T1', 'T2']
    Why:    T1 waits for T2 and T2 waits for T1

    Input:  holds = {"a": "T1", "b": "T2", "c": "T3"}, waits = {"T1": "b", "T2": "c", "T3": "a", "T4": "a"}
    Output: ['T1', 'T2', 'T3']
    Why:    T4 is blocked behind the cycle but not on it

    Input:  holds = {"a": "T1"}, waits = {"T2": "a", "T3": "a"}
    Output: []
    Why:    edge case, T1 is running, so the waiters will get their turn

Approach:
    Replacing each "waits for lock" with "waits for the thread that holds
    it" turns the snapshot into a wait-for graph, and a deadlock is exactly
    a cycle in that graph. Because a thread waits for one lock at most, each
    node has one outgoing edge at most, so a walk from any thread has no
    choices: it stops at a running thread, reaches a thread finished
    earlier, or steps back onto its own path. Only the last case is a new
    cycle, and the cycle is the part of the path from the repeated thread
    onwards, which leaves waiters like T4 outside it. Marking every walked
    thread finished means each thread is visited once, so time is O(t + l)
    for t threads and l locks, and space is O(t).

The lesson behind it: Detecting Deadlock
    https://bytepatterns.com/learn/concurrency/detecting-deadlock
    python concurrency/12-detecting-deadlock.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/concurrency/deadlocked-threads-in-a-wait-graph

Run it:  python problems/concurrency/03-deadlocked-threads-in-a-wait-graph.py
"""


def deadlocked(holds, waits):
    # wait-for edge: a waiting thread points at the thread holding its lock
    nxt = {t: holds[lock] for t, lock in waits.items() if lock in holds}
    state, stuck = {}, set()               # 1 = on the current path, 2 = done
    for start in nxt:
        path, t = [], start
        while t in nxt and t not in state:
            state[t] = 1
            path.append(t)
            t = nxt[t]
        if state.get(t) == 1:              # walked back onto this path: a cycle
            stuck.update(path[path.index(t):])
        for p in path:
            state[p] = 2
    return sorted(stuck)


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(deadlocked({"a": "T1", "b": "T2"}, {"T1": "b", "T2": "a"}), ['T1', 'T2'])
    check(deadlocked({"a": "T1", "b": "T2", "c": "T3"}, {"T1": "b", "T2": "c", "T3": "a", "T4": "a"}), ['T1', 'T2', 'T3'])
    check(deadlocked({"a": "T1"}, {"T2": "a", "T3": "a"}), [])
