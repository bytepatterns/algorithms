"""
Running Balance per Account (medium) · patterns: window-function, running-total, window-frame

A table txn(id, account, day, amount) records deposits as positive amounts
and withdrawals as negative ones, and an account can have several
transactions on the same day. For every transaction, return the account's
balance right after it, as columns account, day, amount and balance, sorted
by account, then day, then id. Each transaction has to move the balance on
its own, one row at a time, even when two of them share a day.

Examples:

    Input:  txn = [(1, "A", "2026-09-01", 100), (2, "B", "2026-09-01", 50), (3, "A", "2026-09-02", -30), (4, "A", "2026-09-02", 20), (5, "B", "2026-09-03", -50)]
    Output: [("A", "2026-09-01", 100, 100), ("A", "2026-09-02", -30, 70), ("A", "2026-09-02", 20, 90),
             ("B", "2026-09-01", 50, 50), ("B", "2026-09-03", -50, 0)]
    Why:    A's two transactions on 09-02 give 70 and then 90, not 90 twice

    Input:  txn = [(1, "A", "2026-09-01", 40)]
    Output: [("A", "2026-09-01", 40, 40)]
    Why:    edge case, a single transaction is its own balance

Approach:
    SUM(amount) OVER (PARTITION BY account ORDER BY day, id ...) attaches to
    each row the sum of everything in its account up to that row, without
    folding any rows away the way GROUP BY would. The trap is the frame.
    When OVER has an ORDER BY and no frame, SQL uses RANGE BETWEEN UNBOUNDED
    PRECEDING AND CURRENT ROW, and RANGE treats all rows with the same sort
    key as one step, so two withdrawals on the same day would both report
    the end-of-day balance. Adding id to the ordering removes the ties, and
    ROWS makes the frame count physical rows, so the balance moves once per
    transaction. The window sorts each account once, O(n log n), and then
    keeps a running sum in one pass.

The lesson behind it: Window Functions
    https://bytepatterns.com/learn/sql/window-functions
    python sql/11-window-functions.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/sql/running-balance-per-account

Run it:  python problems/sql/08-running-balance-per-account.py
"""


import sqlite3

QUERY = """
SELECT account, day, amount,
       SUM(amount) OVER (
           PARTITION BY account
           ORDER BY day, id
           ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
       ) AS balance
FROM txn
ORDER BY account, day, id
"""

def run(txns):
    db = sqlite3.connect(":memory:")
    db.execute("CREATE TABLE txn (id INTEGER PRIMARY KEY, account TEXT, day TEXT, amount INTEGER)")
    db.executemany("INSERT INTO txn VALUES (?, ?, ?, ?)", txns)
    return db.execute(QUERY).fetchall()


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(run([(1, "A", "2026-09-01", 100), (2, "B", "2026-09-01", 50), (3, "A", "2026-09-02", -30), (4, "A", "2026-09-02", 20), (5, "B", "2026-09-03", -50)]), [('A', '2026-09-01', 100, 100), ('A', '2026-09-02', -30, 70), ('A', '2026-09-02', 20, 90), ('B', '2026-09-01', 50, 50), ('B', '2026-09-03', -50, 0)])
    check(run([(1, "A", "2026-09-01", 40)]), [('A', '2026-09-01', 40, 40)])
