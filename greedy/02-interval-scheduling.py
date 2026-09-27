"""
Interval Scheduling: Sort by finishing time and the room books itself.

You want as many non-overlapping jobs as possible from one room. Sort by
finishing time, then walk the list and take any job that starts at or after
the last one you took.

Finishing early is the only thing that matters, because the job that ends
soonest leaves the largest slice of the day for everything else. Duration
and start time are both red herrings.

Lesson 2 of Greedy, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/greedy/interval-scheduling

Run it:  python greedy/02-interval-scheduling.py
"""


if __name__ == "__main__":
    jobs = [(1, 4), (3, 5), (0, 6), (5, 7), (8, 10)]
    jobs.sort(key=lambda j: j[1])        # earliest finishing time first
    taken, last_end = [], float("-inf")
    for s, e in jobs:
        if s >= last_end:                # no clash with what is already booked
            taken.append((s, e))
            last_end = e                 # the room is free again at e
    print(taken)
    print(len(taken))
