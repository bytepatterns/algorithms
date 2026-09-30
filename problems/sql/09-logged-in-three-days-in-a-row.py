"""
Logged In Three Days in a Row (medium) · patterns: window-function, consecutive-rows, dedupe

A table login(person, day) gets one row every time someone signs in, with
day stored as a YYYY-MM-DD date, and a person can sign in several times on
the same day. Write a query that returns every person who signed in on at
least three consecutive calendar days, as a single column person, sorted,
with each person listed once.

Examples:

    Input:  login = [("kim", "2026-09-01"), ("kim", "2026-09-02"), ("kim", "2026-09-03"), ("lee", "2026-09-01"), ("lee", "2026-09-02"), ("lee", "2026-09-04")]
    Output: [("kim",)]
    Why:    lee misses 09-03, so lee never has three days in a row

    Input:  login = [("max", "2026-09-01"), ("max", "2026-09-02"), ("max", "2026-09-02"), ("max", "2026-09-03")]
    Output: [("max",)]
    Why:    signing in twice on 09-02 must not hide the streak

    Input:  login = [("ria", "2026-08-31"), ("ria", "2026-09-01"), ("ria", "2026-09-02")]
    Output: [("ria",)]
    Why:    edge case, a streak can cross the end of a month

Approach:
    After the logins are reduced to one row per person and day, the rows of
    a person sorted by day have a simple property: three consecutive days
    means that some day is exactly two calendar days after the day two rows
    before it. LAG(day, 2) fetches that earlier day without a self-join, and
    julianday turns the dates into day numbers, so the month boundary needs
    no special handling. The deduplication step matters. Without it, a
    second sign-in on 09-02 sits between 09-02 and 09-03, the row two back
    from 09-03 is 09-02, the gap is 1 and a real streak is missed. The same
    idea works on other databases with their own date math: on PostgreSQL
    day - two_back = 2 for DATE columns, on MySQL DATEDIFF(day, two_back) =
    2. Sorting each person's days costs O(n log n).

The lesson behind it: Window Functions
    https://bytepatterns.com/learn/sql/window-functions
    python sql/11-window-functions.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/sql/logged-in-three-days-in-a-row

Run it:  python problems/sql/09-logged-in-three-days-in-a-row.py
"""


import sqlite3

QUERY = """
WITH days AS (
    SELECT DISTINCT person, day
    FROM login
),
with_two_back AS (
    SELECT person, day,
           LAG(day, 2) OVER (PARTITION BY person ORDER BY day) AS two_back
    FROM days
)
SELECT DISTINCT person
FROM with_two_back
WHERE julianday(day) - julianday(two_back) = 2
ORDER BY person
"""

def run(logins):
    db = sqlite3.connect(":memory:")
    db.execute("CREATE TABLE login (person TEXT, day TEXT)")
    db.executemany("INSERT INTO login VALUES (?, ?)", logins)
    return db.execute(QUERY).fetchall()


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(run([("kim", "2026-09-01"), ("kim", "2026-09-02"), ("kim", "2026-09-03"), ("lee", "2026-09-01"), ("lee", "2026-09-02"), ("lee", "2026-09-04")]), [('kim',)])
    check(run([("max", "2026-09-01"), ("max", "2026-09-02"), ("max", "2026-09-02"), ("max", "2026-09-03")]), [('max',)])
    check(run([("ria", "2026-08-31"), ("ria", "2026-09-01"), ("ria", "2026-09-02")]), [('ria',)])
