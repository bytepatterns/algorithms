"""
WHERE and Filtering: Filter in the database, not in your application loop.

WHERE runs a yes-or-no test on every candidate row and keeps only the
passes. Combine tests with AND and OR, and remember the odd one out: NULL
means unknown, so mites = NULL is never true. You must ask IS NULL.

Lesson 2 of SQL, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/sql/where-and-filtering

Run it:  python sql/02-where-and-filtering.py
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
      CREATE TABLE hive (name TEXT, mites INTEGER, queen_seen INTEGER);
      INSERT INTO hive VALUES ('Willow', 12, 1), ('Chalk', 47, 1),
                              ('Beacon', 3, 0), ('Long Mead', 51, 0);
    """)
    rows = db.execute("""
      SELECT name, mites FROM hive
      WHERE mites > 40 AND queen_seen = 0
    """).fetchall()
    check(rows, [('Long Mead', 51)])
