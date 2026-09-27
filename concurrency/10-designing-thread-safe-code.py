"""
Designing Thread-Safe Code: Don't share, freeze it, or guard it.

Work down the list. Give each thread its own state; make whatever must be
shared immutable; guard the small remainder with one lock whose scope is
written down. Reach for clever lock-free tricks only after the first three
have genuinely failed.

Lesson 10 of Concurrency, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/concurrency/designing-thread-safe-code

Run it:  python concurrency/10-designing-thread-safe-code.py
"""


import threading
readings = [3, 8, 1, 9, 4, 7]     # shared, but never mutated
totals = {}
lock = threading.Lock()           # guards: totals, and nothing else

def sum_chunk(name, chunk):
    subtotal = sum(chunk)         # thread-local work, no lock needed
    with lock:
        totals[name] = subtotal


if __name__ == "__main__":
    parts = {"left": readings[:3], "right": readings[3:]}   # private slices
    ts = [threading.Thread(target=sum_chunk, args=kv) for kv in parts.items()]
    for t in ts: t.start()
    for t in ts: t.join()
    print(sorted(totals.items()), sum(totals.values()))
