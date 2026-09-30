"""
Lost Updates in a Shared Counter (easy) · patterns: race-condition, step-simulation

Several threads share one counter, and each thread runs count += 1 a few
times. Every increment is really three steps: read the counter into the
thread's own register, add one to the register, and write the register back.
You are given the number of threads and the schedule the operating system
chose, as a list of thread numbers: each entry lets that thread take its
next step. Every thread finishes all of its steps. Return the counter's
final value, starting from 0.

Examples:

    Input:  threads = 2, schedule = [0, 0, 0, 1, 1, 1]
    Output: 2
    Why:    thread 0 finishes its increment before thread 1 reads, so nothing is lost

    Input:  threads = 2, schedule = [0, 1, 0, 1, 0, 1]
    Output: 1
    Why:    both threads read 0, both write back 1, and one increment disappears

    Input:  threads = 1, schedule = [0, 0, 0, 0, 0, 0]
    Output: 2
    Why:    edge case, a single thread can never race with itself

Approach:
    The bug in a data race lives in the gap between a read and the matching
    write, so the simulation keeps exactly the state that gap needs: one
    register per thread and which step each thread takes next. A read copies
    the shared value, an add changes only the private copy, and a write
    stores the private copy over whatever the counter holds now, which
    silently discards any increment that landed in between. Replaying the
    schedule step by step therefore reproduces the lost update exactly as
    the hardware would. Time is O(s) for a schedule of s steps, and space is
    O(t) for t threads.

The lesson behind it: Race Conditions
    https://bytepatterns.com/learn/concurrency/race-conditions
    python concurrency/02-race-conditions.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/concurrency/lost-updates-in-a-shared-counter

Run it:  python problems/concurrency/01-lost-updates-in-a-shared-counter.py
"""


def final_count(threads, schedule):
    count = 0                              # the shared counter
    reg = [0] * threads                    # each thread's private register
    step = [0] * threads                   # 0 = read, 1 = add, 2 = write
    for t in schedule:
        if step[t] == 0:
            reg[t] = count                 # read the shared value
        elif step[t] == 1:
            reg[t] += 1                    # add one to the private copy
        else:
            count = reg[t]                 # write back, possibly over a newer value
        step[t] = (step[t] + 1) % 3
    return count


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(final_count(2, [0, 0, 0, 1, 1, 1]), 2)
    check(final_count(2, [0, 1, 0, 1, 0, 1]), 1)
    check(final_count(1, [0, 0, 0, 0, 0, 0]), 2)
    check(final_count(2, [0, 1, 1, 1, 0, 0, 0, 0, 0]), 2)
