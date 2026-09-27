"""
Insert Interval: The list is already sorted, so slot the new block in with three passes.

Because the list is already sorted and non-overlapping, only one thing is
unknown: where the new block lands.

Copy every interval that ends before the new one starts. Absorb every
interval that touches it, widening the block as you go. Copy the rest
untouched. No sort, one pass.

Lesson 3 of Intervals, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/intervals/insert-interval

Run it:  python intervals/03-insert-interval.py
"""


if __name__ == "__main__":
    booked = [(1, 3), (6, 9), (12, 16)]
    new, out, i = [4, 8], [], 0
    while i < len(booked) and booked[i][1] < new[0]:
        out.append(booked[i]); i += 1        # ends before the new block starts
    while i < len(booked) and booked[i][0] <= new[1]:
        new = [min(new[0], booked[i][0]), max(new[1], booked[i][1])]   # absorb
        i += 1
    out.append(tuple(new))
    print(out + booked[i:])
