"""
Aggregations & GROUP BY: Fold many rows into one number per group.

Aggregates like SUM, COUNT and AVG squeeze a pile of rows into one value.
GROUP BY decides how many piles there are — one per distinct value. Filter
individual rows with WHERE, then filter whole groups with HAVING, which is
the only place an aggregate can be tested.

Lesson 4 of SQL, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/sql/aggregations-group-by

Run it:  python sql/04-aggregations-group-by.py
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
      CREATE TABLE pluck (picker TEXT, day TEXT, kilos REAL);
      INSERT INTO pluck VALUES ('Meena','Mon',18.0), ('Meena','Tue',22.0),
                               ('Ravi','Mon',9.5), ('Ravi','Tue',8.0),
                               ('Suri','Mon',30.0);
    """)
    rows = db.execute("""
      SELECT picker, SUM(kilos) AS total, COUNT(*) AS days
      FROM pluck GROUP BY picker HAVING SUM(kilos) >= 20
    """).fetchall()
    check(rows, [('Meena', 40.0, 2), ('Suri', 30.0, 1)])
