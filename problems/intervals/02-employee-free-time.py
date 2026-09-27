"""
Employee Free Time (hard) · patterns: intervals, merge

Each employee has a list of busy intervals, already sorted and
non-overlapping within that employee. Return the positive-length stretches
of time during which every employee is free, in order. A stretch before the
first busy interval or after the last one does not count — only gaps between
busy time.

Examples:

    Input:  schedules = [[[1, 2], [5, 6]], [[1, 3]], [[4, 10]]]
    Output: [[3, 4]]
    Why:    after 3 nobody is busy until 4, and from 4 onwards the third employee is

    Input:  schedules = [[[1, 3], [6, 7]], [[2, 4]], [[2, 5], [9, 12]]]
    Output: [[5, 6], [7, 9]]
    Why:    busy time runs 1-5, then 6-7, then 9-12

    Input:  schedules = [[[1, 2]], [[1, 2]]]
    Output: []
    Why:    edge case, the busy time is one solid block with no gap inside it

Approach:
    Free time is the complement of the union of all busy intervals, so the
    employee each interval belongs to is irrelevant once they are pooled.
    Sorting by start lets one sweep maintain the furthest finish reached; an
    interval that begins after it exposes a gap, and one that begins earlier
    merely extends coverage. Tracking the maximum finish rather than the
    previous one is what handles an interval fully contained inside another.
    Time is O(n log n) for the sort, space O(n) for the pooled list.

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/intervals/employee-free-time

Run it:  python problems/intervals/02-employee-free-time.py
"""


def free_time(schedules):
    busy = sorted(b for person in schedules for b in person)
    out, end = [], busy[0][1]                 # furthest finish so far
    for start, finish in busy[1:]:
        if start > end:                       # a hole nobody is covering
            out.append([end, start])
        end = max(end, finish)                # max, not finish: nesting
    return out


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(free_time([[[1, 2], [5, 6]], [[1, 3]], [[4, 10]]]), [[3, 4]])
    check(free_time([[[1, 3], [6, 7]], [[2, 4]], [[2, 5], [9, 12]]]), [[5, 6], [7, 9]])
    check(free_time([[[1, 2]], [[1, 2]]]), [])
