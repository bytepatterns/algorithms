"""
Query Execution Order: SQL is written top-down but evaluated in a different order.

You write SELECT first, but the engine runs it fifth. The real order is
FROM, WHERE, GROUP BY, HAVING, SELECT, ORDER BY. That single fact explains
most beginner errors: why WHERE cannot see a column alias, and why an
aggregate filter has to live in HAVING.

Lesson 9 of SQL, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/sql/query-execution-order

Run it:  python sql/09-query-execution-order.py
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
    db.executescript("""CREATE TABLE apple (variety TEXT, kilos REAL, rotten INT);
      INSERT INTO apple VALUES ('Dabinett',60,0), ('Dabinett',40,0),
        ('Kingston',30,0), ('Kingston',90,1), ('Yarlington',55,0);""")
    check(db.execute("""
      SELECT variety, SUM(kilos) AS total   -- 5th: build the output row
      FROM apple                            -- 1st: choose the source
      WHERE rotten = 0                      -- 2nd: bin the bad fruit
      GROUP BY variety                      -- 3rd: one bin per variety
      HAVING SUM(kilos) >= 50               -- 4th: skip small pressings
      ORDER BY total DESC                   -- 6th: heaviest first
    """).fetchall(), [('Dabinett', 100.0), ('Yarlington', 55.0)])
