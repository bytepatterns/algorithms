"""
Retries in a Compare-and-Swap Loop (easy) · patterns: compare-and-swap, step-simulation

Several threads add their own amount to one shared value without a lock.
Each thread loops over two steps: read the shared value into a private
snapshot, then compare-and-swap. The swap succeeds only if the shared value
still equals the snapshot, in which case it writes snapshot + amount and the
thread is done; otherwise the swap fails, nothing is written, and the thread
starts over with a fresh read. You are given the starting value, each
thread's amount, and the schedule as a list of thread numbers, where each
entry lets that thread take its next step. Entries for a thread that has
already finished are ignored. Return the final value and how many swaps each
thread lost.

Examples:

    Input:  start = 0, amounts = [5, 7], schedule = [0, 1, 0, 1, 1, 1]
    Output: (12, [0, 1])
    Why:    thread 1's swap fails because thread 0 changed the value after thread 1 read it, so it rereads and tries again

    Input:  start = 0, amounts = [1, 1, 1], schedule = [0, 1, 2, 0, 1, 2, 1, 2, 1, 2, 2, 2]
    Output: (3, [0, 1, 2])
    Why:    all three read 0, only one swap per round can win, and thread 2 loses twice

    Input:  start = 10, amounts = [3], schedule = [0, 0]
    Output: (13, [0])
    Why:    edge case, with no other writer the first swap always succeeds

Approach:
    A compare-and-swap loop replaces a lock with an optimistic check: the
    write only happens if nobody changed the value since this thread read
    it. The simulation keeps what that check needs, one snapshot per thread
    plus whether it has finished, and a None snapshot means the thread's
    next step is a read. A failed swap writes nothing and sends the thread
    back to reread, so every amount lands exactly once and the final value
    is always the start plus the sum, which is the difference from the
    lost-update race. What contention costs instead is retries, and the
    second example shows them piling up on the thread that keeps losing.
    Time is O(s) for a schedule of s steps, and space is O(t) for t threads.

The lesson behind it: Compare-and-Swap
    https://bytepatterns.com/learn/concurrency/compare-and-swap
    python concurrency/15-compare-and-swap.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/concurrency/retries-in-a-compare-and-swap-loop

Run it:  python problems/concurrency/06-retries-in-a-compare-and-swap-loop.py
"""


def cas_add(start, amounts, schedule):
    value = start                          # the shared value
    snap = [None] * len(amounts)           # None means the next step is a read
    done = [False] * len(amounts)
    failed = [0] * len(amounts)
    for t in schedule:
        if done[t]:
            continue                       # finished threads take no more steps
        if snap[t] is None:
            snap[t] = value                # read into a private snapshot
        elif value == snap[t]:
            value = snap[t] + amounts[t]   # the swap wins: nobody wrote in between
            done[t] = True
        else:
            failed[t] += 1                 # someone got there first: retry from a read
            snap[t] = None
    return value, failed


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(cas_add(0, [5, 7], [0, 1, 0, 1, 1, 1]), (12, [0, 1]))
    check(cas_add(0, [1, 1, 1], [0, 1, 2, 0, 1, 2, 1, 2, 1, 2, 2, 2]), (3, [0, 1, 2]))
    check(cas_add(10, [3], [0, 0]), (13, [0]))
