"""
Async and the Event Loop: One thread, politely taking turns.

Async concurrency runs on one thread. A coroutine executes until it hits an
await, hands control back to the event loop, and the loop resumes whichever
task is ready. No preemption, so no surprise interleavings — but nobody else
runs while you refuse to yield.

Lesson 7 of Concurrency, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/concurrency/async-await-event-loop

Run it:  python concurrency/07-async-await-event-loop.py
"""


import asyncio

async def worker(name, rounds):
    for step in range(1, rounds + 1):
        print(name, "step", step)
        await asyncio.sleep(0)       # yield: let the loop run someone else

async def main():
    await asyncio.gather(worker("A", 2), worker("B", 2))


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

import io
import re
import sys


def _same(printed, expected):
    """Printed text vs the lesson's comment, which may add a note after it."""
    printed, expected = printed.strip(), expected.strip()
    wants = [expected] + [expected.rsplit(s, 1)[1].strip() for s in (" -> ", " = ") if s in expected]
    for want in wants + [w[1:] for w in wants if w.startswith("~")]:
        rest = want[len(printed):] if want.startswith(printed) else None
        if rest == "" or (rest and re.match(r"[\s,;:]+([A-Za-z]|\u2014|\u2013|-(?!\d)|\u2192|<-|\([A-Za-z]|#)", rest)):
            return True
    return False


class expect_output:
    """Capture everything the block prints and compare it line by line."""

    def __init__(self, *lines):
        self.lines = list(lines)

    def __enter__(self):
        self.buffer, self.stdout = io.StringIO(), sys.stdout
        sys.stdout = self.buffer

    def __exit__(self, *exc):
        sys.stdout = self.stdout
        printed = self.buffer.getvalue()
        print(printed, end="")
        got = [line.rstrip() for line in printed.splitlines()]
        want = self.lines
        if len(want) == 1 and " / " in want[0] and len(got) > 1:
            want = want[0].split(" / ")
        assert exc[0] or _lines_match(got, want), f"expected {want!r}, got {got!r}"


def _lines_match(got, want):
    if not want:
        return not got
    if want[0].strip() in ("...", "\u2026"):  # the lesson elides some lines
        return any(_lines_match(got[i:], want[1:]) for i in range(len(got) + 1))
    return bool(got) and _same(got[0], want[0]) and _lines_match(got[1:], want[1:])


if __name__ == "__main__":
    with expect_output("A step 1", "B step 1", "A step 2", "B step 2"):
        asyncio.run(main())
