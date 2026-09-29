"""
Deadlock: Everyone holding what the next one needs.

Deadlock is a standoff. Thread one holds lock A and wants B; thread two
holds B and wants A. Neither will let go of what it has, so both wait
forever. No exception is raised — the work simply stops.

Lesson 4 of Concurrency, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/concurrency/deadlock

Short video on this lesson: https://www.youtube.com/@bytepatterns

Run it:  python concurrency/04-deadlock.py
"""


import threading

locks = {"alice": threading.Lock(), "bob": threading.Lock()}

def transfer(src, dst):
    first, second = sorted([src, dst])     # always the same order
    with locks[first], locks[second]:
        print("moved", src, "->", dst)


if __name__ == "__main__":
    transfer("bob", "alice")
    transfer("alice", "bob")                   # no cycle: alice's lock goes first
