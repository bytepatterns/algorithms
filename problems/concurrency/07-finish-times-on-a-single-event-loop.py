"""
Finish Times on a Single Event Loop (medium) · patterns: event-loop, min-heap, event-simulation

A single-threaded event loop runs async tasks. Each task is (name, arrive,
steps), where steps alternates CPU time and I/O wait, starting and ending
with CPU: [2, 10, 1] means run 2 ms, await I/O for 10 ms, then run 1 ms
more. The loop runs one piece of CPU work at a time and never interrupts it.
A task is ready when it arrives and again when its I/O completes, and the
loop always picks the task that has been ready the longest, breaking ties by
the order tasks are listed. When nothing is ready the loop sits idle until
something is. Return a dict from task name to the time it finishes, in the
order tasks finish.

Examples:

    Input:  [("api", 0, [2, 10, 1]), ("report", 1, [30]), ("ping", 3, [1])]
    Output: {'report': 32, 'ping': 33, 'api': 34}
    Why:    one 30 ms block of CPU holds up a 1 ms ping and the api's last step

    Input:  [("api", 0, [2, 10, 1]), ("report", 1, [10, 0, 10, 0, 10]), ("ping", 3, [1])]
    Output: {'ping': 13, 'api': 14, 'report': 34}
    Why:    the same report split into three chunks with zero-length awaits lets the others in between

    Input:  [("job", 5, [4, 3, 2])]
    Output: {'job': 14}
    Why:    edge case, with one task the loop only waits for its arrival and its own I/O

Approach:
    On an event loop, concurrency comes only from tasks giving control back
    at an await, so the whole schedule is decided by when each task is ready
    again. A min-heap keyed by (ready time, list position) always has the
    task that has waited longest on top. Running a CPU step moves the clock
    forward by its full length, because nothing can interrupt it, and an I/O
    wait just puts the task back in the heap for later. The first example is
    the classic mistake: one long synchronous step makes a 1 ms request wait
    30 ms. The second shows the fix, breaking the work into chunks with
    zero-length awaits so the loop can serve others in between. Each step is
    pushed and popped once, so time is O(s log n) for s steps across n
    tasks, and space is O(n).

The lesson behind it: Blocking the Event Loop
    https://bytepatterns.com/learn/concurrency/blocking-the-event-loop
    python concurrency/14-blocking-the-event-loop.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/concurrency/finish-times-on-a-single-event-loop

Run it:  python problems/concurrency/07-finish-times-on-a-single-event-loop.py
"""


import heapq

def finish_times(tasks):
    ready = [(arrive, i, 0) for i, (_, arrive, _) in enumerate(tasks)]
    heapq.heapify(ready)                   # (ready time, task index, step index)
    clock, done = 0, {}
    while ready:
        at, i, s = heapq.heappop(ready)
        name, _, steps = tasks[i]
        clock = max(clock, at) + steps[s]  # CPU work runs to the end, uninterrupted
        if s + 1 < len(steps):
            heapq.heappush(ready, (clock + steps[s + 1], i, s + 2))   # await I/O
        else:
            done[name] = clock
    return done


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(finish_times([("api", 0, [2, 10, 1]), ("report", 1, [30]), ("ping", 3, [1])]), {'report': 32, 'ping': 33, 'api': 34})
    check(finish_times([("api", 0, [2, 10, 1]), ("report", 1, [10, 0, 10, 0, 10]), ("ping", 3, [1])]), {'ping': 13, 'api': 14, 'report': 34})
    check(finish_times([("job", 5, [4, 3, 2])]), {'job': 14})
