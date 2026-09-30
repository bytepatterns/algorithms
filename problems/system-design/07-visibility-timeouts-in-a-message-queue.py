"""
Visibility Timeouts in a Message Queue (medium) · patterns: message-queue, event-simulation

A queue hands each message to one consumer at a time. When a consumer polls
at time t, it receives the first message, in the order they were sent, that
is currently visible. A received message is hidden for timeout seconds. If
the consumer's processing time is shorter than the timeout, it acknowledges
in time and the message is deleted. Otherwise the message becomes visible
again at t + timeout, and once it has been received max_receives times
without an acknowledgement it moves to a dead-letter queue instead. Given
the messages, the polls as (time, consumer) sorted by time, and each
consumer's processing time, return the delivery log as (time, consumer,
message or None), the messages completed in order, and the dead-lettered
messages.

Examples:

    Input:  messages = ["m1", "m2"], polls = [(0, "slow"), (1, "fast"), (30, "fast"), (31, "fast")],
            work = {"slow": 60, "fast": 2}, timeout = 30, max_receives = 3
    Output: ([(0, 'slow', 'm1'), (1, 'fast', 'm2'), (30, 'fast', 'm1'), (31, 'fast', None)], ['m2', 'm1'], [])
    Why:    slow cannot finish m1 within 30 seconds, so m1 reappears at 30 and fast picks it up

    Input:  messages = ["poison"], polls at 0, 10, 20 and 30 by "a", work = {"a": 99}, timeout = 10, max_receives = 3
    Output: ([(0, 'a', 'poison'), (10, 'a', 'poison'), (20, 'a', 'poison'), (30, 'a', None)], [], ['poison'])
    Why:    a message that always fails is parked after 3 tries instead of blocking the queue forever

    Input:  messages = [], polls = [(5, "a")], work = {"a": 1}, timeout = 10, max_receives = 3
    Output: ([(5, 'a', None)], [], [])
    Why:    edge case, polling an empty queue returns nothing

Approach:
    A visibility timeout is how a queue gets at-least-once delivery without
    knowing whether a consumer crashed: it simply hides the message for a
    while and shows it again if no acknowledgement arrives. The simulation
    keeps, for every message still in the queue, when it becomes visible,
    plus a receive counter. A poll takes the earliest-sent visible message,
    and the consumer's processing time decides the outcome: an
    acknowledgement in time deletes it, while a late one lets it reappear
    for another consumer, which is why the same message can be processed
    twice. The receive counter implements the dead-letter rule, so a message
    that fails every time stops consuming capacity after max_receives
    attempts. Each poll scans the messages, so time is O(p × m) for p polls
    and m messages, and space is O(m).

The lesson behind it: Message Queues
    https://bytepatterns.com/learn/system-design/message-queues

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/system-design/visibility-timeouts-in-a-message-queue

Run it:  python problems/system-design/07-visibility-timeouts-in-a-message-queue.py
"""


from collections import defaultdict

def run_queue(messages, polls, work, timeout, max_receives):
    visible_at = {m: 0 for m in messages}  # only messages still in the queue
    receives = defaultdict(int)
    log, done, dead = [], [], []
    for t, consumer in polls:
        ready = [m for m in messages if m in visible_at and visible_at[m] <= t]
        if not ready:
            log.append((t, consumer, None))
            continue
        m = ready[0]                       # oldest visible message first
        receives[m] += 1
        log.append((t, consumer, m))
        if work[consumer] < timeout:
            del visible_at[m]              # acknowledged in time: delete
            done.append(m)
        elif receives[m] == max_receives:
            del visible_at[m]              # too many failures: dead-letter it
            dead.append(m)
        else:
            visible_at[m] = t + timeout    # no ack: visible again later
    return log, done, dead


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(run_queue(["m1", "m2"], [(0, "slow"), (1, "fast"), (30, "fast"), (31, "fast")], {"slow": 60, "fast": 2}, 30, 3), ([(0, 'slow', 'm1'), (1, 'fast', 'm2'), (30, 'fast', 'm1'), (31, 'fast', None)], ['m2', 'm1'], []))
    check(run_queue(["poison"], [(0, "a"), (10, "a"), (20, "a"), (30, "a")], {"a": 99}, 10, 3), ([(0, 'a', 'poison'), (10, 'a', 'poison'), (20, 'a', 'poison'), (30, 'a', None)], [], ['poison']))
    check(run_queue([], [(5, "a")], {"a": 1}, 10, 3), ([(5, 'a', None)], [], []))
