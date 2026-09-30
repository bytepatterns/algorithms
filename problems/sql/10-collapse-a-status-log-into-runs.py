"""
Collapse a Status Log Into Runs (hard) · patterns: gaps-and-islands, window-function, row-number

A monitor writes at most one row per day into status_log(day, status), with
day as a YYYY-MM-DD date and status either 'up' or 'down'. Some days have no
row because the monitor was offline. Collapse the log into runs: a run is a
stretch of consecutive calendar days that all have a row with the same
status. Return status, start_day, end_day and days for every run, sorted by
start_day. A missing day ends a run just like a change of status does.

Examples:

    Input:  status_log = [("2026-09-01", "up"), ("2026-09-02", "up"), ("2026-09-03", "down"), ("2026-09-04", "up"), ("2026-09-05", "up")]
    Output: [("up", "2026-09-01", "2026-09-02", 2), ("down", "2026-09-03", "2026-09-03", 1), ("up", "2026-09-04", "2026-09-05", 2)]

    Input:  status_log = [("2026-09-01", "up"), ("2026-09-02", "up"), ("2026-09-04", "up")]
    Output: [("up", "2026-09-01", "2026-09-02", 2), ("up", "2026-09-04", "2026-09-04", 1)]
    Why:    nothing was recorded on 09-03, so the up run breaks there

    Input:  status_log = [("2026-09-30", "down")]
    Output: [("down", "2026-09-30", "2026-09-30", 1)]
    Why:    edge case, a single row is a run of one day

Approach:
    This is the gaps-and-islands pattern. Number the rows of each status in
    day order with ROW_NUMBER() OVER (PARTITION BY status ORDER BY day) and
    subtract that number from the day number. Within a run both values climb
    by one per row, so the difference stays the same; the moment a calendar
    day is skipped for that status, the day number jumps by more than the
    row number and the difference changes. A skipped day can be a day with
    the other status or a day with no row, and the one formula catches both,
    which is why the partition by status is essential. Grouping by status
    and that difference yields one group per run, and MIN, MAX and COUNT(*)
    describe it. A version with LAG that flags each row where a run starts
    and then sums the flags works too, but needs one more step. The window
    sorts each status once, O(n log n), and the grouping is linear.

The lesson behind it: Window Functions
    https://bytepatterns.com/learn/sql/window-functions
    python sql/11-window-functions.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/sql/collapse-a-status-log-into-runs

Run it:  python problems/sql/10-collapse-a-status-log-into-runs.py
"""


import sqlite3

QUERY = """
WITH keyed AS (
    SELECT day, status,
           julianday(day)
             - ROW_NUMBER() OVER (PARTITION BY status ORDER BY day) AS grp
    FROM status_log
)
SELECT status, MIN(day) AS start_day, MAX(day) AS end_day, COUNT(*) AS days
FROM keyed
GROUP BY status, grp
ORDER BY start_day
"""

def run(rows):
    db = sqlite3.connect(":memory:")
    db.execute("CREATE TABLE status_log (day TEXT PRIMARY KEY, status TEXT)")
    db.executemany("INSERT INTO status_log VALUES (?, ?)", rows)
    return db.execute(QUERY).fetchall()


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(run([("2026-09-01", "up"), ("2026-09-02", "up"), ("2026-09-03", "down"), ("2026-09-04", "up"), ("2026-09-05", "up")]), [('up', '2026-09-01', '2026-09-02', 2), ('down', '2026-09-03', '2026-09-03', 1), ('up', '2026-09-04', '2026-09-05', 2)])
    check(run([("2026-09-01", "up"), ("2026-09-02", "up"), ("2026-09-04", "up")]), [('up', '2026-09-01', '2026-09-02', 2), ('up', '2026-09-04', '2026-09-04', 1)])
    check(run([("2026-09-30", "down")]), [('down', '2026-09-30', '2026-09-30', 1)])
