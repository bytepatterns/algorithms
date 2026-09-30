"""
Users Retained Month Over Month (hard) · patterns: cte, self-join, retention

An app logs every session in activity(user_id, day), with day as a
YYYY-MM-DD date, and a user can have many sessions in a month. A user is
active in a month if they have at least one session in it, and retained in a
month if they are active in it and were also active in the calendar month
right before it. For every month that has activity, return month as YYYY-MM,
the number of active users and the number of retained users, sorted by
month.

Examples:

    Input:  activity = [(1, "2026-01-05"), (1, "2026-01-20"), (2, "2026-01-09"), (1, "2026-02-02"), (3, "2026-02-14"), (2, "2026-03-01"), (3, "2026-03-30")]
    Output: [("2026-01", 2, 0), ("2026-02", 2, 1), ("2026-03", 2, 1)]
    Why:    user 1 is retained in February and user 3 in March; user 2 skipped February, so March does not count them

    Input:  activity = [(1, "2026-04-10"), (1, "2026-06-10")]
    Output: [("2026-04", 1, 0), ("2026-06", 1, 0)]
    Why:    May has no activity, so it gets no row, and June's previous month is May, not April

    Input:  activity = [(7, "2025-12-31"), (7, "2026-01-01"), (8, "2026-01-15")]
    Output: [("2025-12", 1, 0), ("2026-01", 2, 1)]
    Why:    edge case, the month before January is December of the previous year

Approach:
    The CTE monthly turns the raw log into the grain the question is asked
    at, one row per user per active month, and DISTINCT is what makes
    several sessions in a month count once. The main query reads that CTE
    twice, as the current month and as the month before, which is exactly
    what a named result is for. The join is a LEFT JOIN so that users who
    were not active the month before still count as active; COUNT(*) counts
    every current row, while COUNT(prev.user_id) skips the NULLs the left
    join leaves behind and so counts only retained users. Computing the
    previous month with date arithmetic rather than string tricks handles
    the December to January step and treats a gap month correctly. Building
    the CTE is O(n log n), and the self-join is a lookup per row on at most
    n rows.

The lesson behind it: CTEs and Recursion
    https://bytepatterns.com/learn/sql/ctes-and-recursion
    python sql/12-ctes-and-recursion.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/sql/users-retained-month-over-month

Run it:  python problems/sql/14-users-retained-month-over-month.py
"""


import sqlite3

QUERY = """
WITH monthly AS (
    SELECT DISTINCT user_id, strftime('%Y-%m', day) AS month
    FROM activity
)
SELECT cur.month,
       COUNT(*) AS active,
       COUNT(prev.user_id) AS retained
FROM monthly AS cur
LEFT JOIN monthly AS prev
       ON prev.user_id = cur.user_id
      AND prev.month = strftime('%Y-%m', cur.month || '-01', '-1 month')
GROUP BY cur.month
ORDER BY cur.month
"""

def run(rows):
    db = sqlite3.connect(":memory:")
    db.execute("CREATE TABLE activity (user_id INTEGER, day TEXT)")
    db.executemany("INSERT INTO activity VALUES (?, ?)", rows)
    return db.execute(QUERY).fetchall()


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(run([(1, "2026-01-05"), (1, "2026-01-20"), (2, "2026-01-09"), (1, "2026-02-02"), (3, "2026-02-14"), (2, "2026-03-01"), (3, "2026-03-30")]), [('2026-01', 2, 0), ('2026-02', 2, 1), ('2026-03', 2, 1)])
    check(run([(1, "2026-04-10"), (1, "2026-06-10")]), [('2026-04', 1, 0), ('2026-06', 1, 0)])
    check(run([(7, "2025-12-31"), (7, "2026-01-01"), (8, "2026-01-15")]), [('2025-12', 1, 0), ('2026-01', 2, 1)])
