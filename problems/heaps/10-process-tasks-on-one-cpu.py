"""
Process Tasks on One CPU (medium) · patterns: min-heap, event-simulation

A single-core worker receives tasks, where tasks[i] = [enqueueTime,
processingTime]. Task i becomes available at enqueueTime. Whenever the
worker is idle and tasks are available, it starts the available task with
the shortest processing time, breaking ties by the smaller index, and runs
it to completion without interruption. If nothing is available, it waits for
the next task to arrive. Return the order in which the task indices are
processed. There are up to 100,000 tasks, and times are up to 10^9.

Examples:

    Input:  tasks = [[1, 2], [2, 4], [3, 2], [4, 1]]
    Output: [0, 2, 3, 1]
    Why:    task 0 runs from 1 to 3; then 2 and 1 are waiting and 2 is shorter; at 5 task 3 is shortest

    Input:  tasks = [[7, 10], [7, 12], [7, 5], [7, 4], [7, 2]]
    Output: [4, 3, 2, 0, 1]
    Why:    everything arrives together, so the order is simply shortest first

    Input:  tasks = [[5, 3]]
    Output: [0]
    Why:    edge case, the worker waits until time 5 and runs the only task

Approach:
    The simulation only has to decide which task starts each time the worker
    becomes free. Sorting indices by enqueue time lets arrivals be fed in
    with a single pointer, and a min-heap keyed by (processingTime, index)
    always offers the task the rule picks, including the tie-break by index.
    Before each pick, every task that has arrived by the current time is
    pushed; if nothing has arrived, the clock jumps straight to the next
    arrival, so idle gaps of a billion units cost nothing. Popping a task
    and adding its processing time to the clock moves to the next decision
    point. Every task is pushed and popped once, so time is O(n log n) and
    space is O(n).

The lesson behind it: Priority Queue
    https://bytepatterns.com/learn/heaps/priority-queue
    python heaps/03-priority-queue.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/heaps/process-tasks-on-one-cpu

Run it:  python problems/heaps/10-process-tasks-on-one-cpu.py
"""


import heapq

def cpu_order(tasks):
    arrivals = sorted(range(len(tasks)), key=lambda i: tasks[i][0])
    ready, order, clock, k = [], [], 0, 0
    while len(order) < len(tasks):
        if not ready:
            clock = max(clock, tasks[arrivals[k]][0])        # skip idle time
        while k < len(arrivals) and tasks[arrivals[k]][0] <= clock:
            i = arrivals[k]
            heapq.heappush(ready, (tasks[i][1], i))          # shortest, then lowest index
            k += 1
        duration, i = heapq.heappop(ready)
        clock += duration
        order.append(i)
    return order


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(cpu_order([[1, 2], [2, 4], [3, 2], [4, 1]]), [0, 2, 3, 1])
    check(cpu_order([[7, 10], [7, 12], [7, 5], [7, 4], [7, 2]]), [4, 3, 2, 0, 1])
    check(cpu_order([[5, 3]]), [0])
