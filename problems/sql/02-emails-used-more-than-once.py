"""
Emails Used More Than Once (easy) · patterns: group-by, having

A table account(id, email) holds one row per sign-up, and a signup form
without a uniqueness check has let some emails in several times. Write a
query that returns every email that appears on more than one account, with
the number of accounts that use it, as columns email and uses, sorted by
email. Emails are compared exactly as stored.

Examples:

    Input:  account = [(1, "a@x.io"), (2, "b@x.io"), (3, "a@x.io"), (4, "c@x.io"), (5, "b@x.io"), (6, "a@x.io")]
    Output: [("a@x.io", 3), ("b@x.io", 2)]
    Why:    c@x.io is used once, so it is not a duplicate

    Input:  account = [(1, "a@x.io"), (2, "b@x.io")]
    Output: []
    Why:    edge case, no email repeats, so no row comes back

Approach:
    GROUP BY email folds every set of rows that share an email into one
    group, and COUNT(*) counts the rows in it. The filter has to run after
    that fold, because a single row knows nothing about how many others
    share its email, which is exactly what HAVING is for: WHERE filters rows
    before grouping, HAVING filters groups after it. Without ORDER BY a
    database may return groups in any order, so the sort is part of the
    answer. The usual follow-up is to delete the extra accounts and keep the
    oldest one per email: DELETE FROM account WHERE id NOT IN (SELECT
    MIN(id) FROM account GROUP BY email). Grouping costs O(n) with hashing
    or O(n log n) with sorting, and an index on email lets the database read
    the groups already in order.

The lesson behind it: Aggregations & GROUP BY
    https://bytepatterns.com/learn/sql/aggregations-group-by
    python sql/04-aggregations-group-by.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/sql/emails-used-more-than-once

Run it:  python problems/sql/02-emails-used-more-than-once.py
"""


import sqlite3

QUERY = """
SELECT email, COUNT(*) AS uses
FROM account
GROUP BY email
HAVING COUNT(*) > 1
ORDER BY email
"""

def run(accounts):
    db = sqlite3.connect(":memory:")
    db.execute("CREATE TABLE account (id INTEGER PRIMARY KEY, email TEXT)")
    db.executemany("INSERT INTO account VALUES (?, ?)", accounts)
    return db.execute(QUERY).fetchall()


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(run([(1, "a@x.io"), (2, "b@x.io"), (3, "a@x.io"), (4, "c@x.io"), (5, "b@x.io"), (6, "a@x.io")]), [('a@x.io', 3), ('b@x.io', 2)])
    check(run([(1, "a@x.io"), (2, "b@x.io")]), [])
