"""
Blocking the Event Loop: One thread runs everything, so one rude call stops the world.

An event loop is cooperative: one thread, one task running at a time, and
control only changes hands at an await. Concurrency comes from tasks that
yield while they wait. A call that does not yield — a blocking read, a tight
computation — holds the only thread, and everything else stops.

Lesson 14 of Concurrency, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/concurrency/blocking-the-event-loop

Run it:  python concurrency/14-blocking-the-event-loop.py
"""


import asyncio, time

async def gauge(depth):
    await asyncio.sleep(0.1)              # yields the thread to the loop
    return depth

async def rude(depth):
    time.sleep(0.1)                       # holds the only thread
    return depth

async def race(worker):
    start = time.perf_counter()
    await asyncio.gather(worker(3), worker(7))
    return round(time.perf_counter() - start, 1)


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(asyncio.run(race(gauge)), 0.1)  # the two waits overlapped
    check(asyncio.run(race(rude)), 0.2)  # they queued up
