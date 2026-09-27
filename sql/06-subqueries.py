"""
Subqueries: A query inside a query, answered before the outer one runs.

A subquery is a complete query used as a value. Wrapped in brackets, it runs
first and hands its answer to the outer query. An uncorrelated one runs
once. A correlated one references the outer row, so it runs again for every
row — convenient to write, easy to make expensive.

Lesson 6 of SQL, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/sql/subqueries

Run it:  python sql/06-subqueries.py
"""


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    import sqlite3
    db = sqlite3.connect(":memory:")
    db.executescript("""
      CREATE TABLE turbine (name TEXT, mwh REAL);
      INSERT INTO turbine VALUES ('T1', 410.0), ('T2', 180.0),
                                 ('T3', 395.0), ('T4', 215.0);
    """)
    rows = db.execute("""
      SELECT name, mwh FROM turbine
      WHERE mwh < (SELECT AVG(mwh) FROM turbine)   -- inner runs first: 300.0
    """).fetchall()
    check(rows, [('T2', 180.0), ('T4', 215.0)])
