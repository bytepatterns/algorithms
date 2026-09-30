"""
Calendar Without Double Booking (medium) · patterns: sorted-intervals, bisect-insert, half-open-intervals

A meeting room accepts booking requests one at a time. Each request is a
half-open span [start, end), so a booking ending at 20 does not clash with
one starting at 20. book(start, end) must add the span and return True if it
overlaps no accepted booking, and otherwise leave the calendar unchanged and
return False. There are up to 1,000 requests and 0 ≤ start < end ≤ 10^9.
Keep the accepted bookings sorted so that each request is checked against
only its neighbours.

Examples:

    Input:  book(10, 20), book(15, 25), book(20, 30)
    Output: [True, False, True]
    Why:    [15, 25) overlaps [10, 20); [20, 30) only touches it

    Input:  book(5, 10), book(1, 5), book(3, 4)
    Output: [True, True, False]
    Why:    [3, 4) falls inside [1, 5)

    Input:  book(1, 2), book(1, 2)
    Output: [True, False]
    Why:    edge case, the same span twice

Approach:
    Accepted bookings never overlap, so when they are sorted by start their
    end times are sorted too, and a new span only has to be compared with
    its two neighbours in that order. bisect_right on the start times finds
    where the new span would go: the booking just before it is the latest
    one starting at or before the new start, and it clashes only if it ends
    after that start; the booking just after it clashes only if it starts
    before the new end. Using half-open spans makes touching bookings legal
    with plain strict comparisons. Each check is O(log n); inserting into a
    Python list shifts elements, so a booking costs O(n) in the worst case,
    which a balanced tree or sorted container would bring down to O(log n).
    Space is O(n).

The lesson behind it: Insert Interval
    https://bytepatterns.com/learn/intervals/insert-interval
    python intervals/03-insert-interval.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/intervals/calendar-without-double-booking

Run it:  python problems/intervals/10-calendar-without-double-booking.py
"""


from bisect import bisect_right

class Calendar:
    def __init__(self):
        self.starts, self.ends = [], []

    def book(self, start, end):
        i = bisect_right(self.starts, start)
        if i and self.ends[i - 1] > start:                 # previous one still running
            return False
        if i < len(self.starts) and self.starts[i] < end:  # next one starts too soon
            return False
        self.starts.insert(i, start)
        self.ends.insert(i, end)
        return True

def run(requests):
    calendar = Calendar()
    return [calendar.book(s, e) for s, e in requests]


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(run([(10, 20), (15, 25), (20, 30)]), [True, False, True])
    check(run([(5, 10), (1, 5), (3, 4)]), [True, True, False])
    check(run([(1, 2), (1, 2)]), [True, False])
