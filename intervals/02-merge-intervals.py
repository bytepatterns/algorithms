"""
Merge Intervals: Hold one block open, stretch it while they touch, close it on a gap.

Sort by start, then hold exactly one block open.

If the next interval starts at or before the open block's end, they touch:
stretch the end to whichever is larger. Otherwise there is a gap, so close
the block and open a new one. Every interval is looked at once.

Lesson 2 of Intervals, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/intervals/merge-intervals

Run it:  python intervals/02-merge-intervals.py
"""


if __name__ == "__main__":
    spans = [(1, 3), (2, 6), (8, 10), (9, 11)]
    spans.sort()                       # by start — the whole trick
    merged = [list(spans[0])]
    for s, e in spans[1:]:
        if s <= merged[-1][1]:         # touches or overlaps the open block
            merged[-1][1] = max(merged[-1][1], e)
        else:
            merged.append([s, e])      # real gap: close this one, open the next
    print(merged)
