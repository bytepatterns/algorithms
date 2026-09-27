"""
CTEs and Recursion: Name a result, then build the next one on top of it.

A common table expression names a query so the next one can use it. Add
RECURSIVE and the CTE may refer to itself: an anchor row set, then a step
that joins the previous pass back onto the table, repeated until a pass
returns nothing.

Lesson 12 of SQL, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/sql/ctes-and-recursion

Run it:  python sql/12-ctes-and-recursion.py
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
    db.executescript("""CREATE TABLE gate (name TEXT, feeds TEXT);
      INSERT INTO gate VALUES ('spring',NULL),('mill','spring'),
        ('town','mill'),('harbour','town'),('quarry',NULL);""")
    check(db.execute("""
      WITH RECURSIVE downstream(name, hops) AS (
        SELECT name, 0 FROM gate WHERE name = 'spring'     -- anchor
        UNION ALL
        SELECT g.name, d.hops + 1                          -- one step further
        FROM gate g JOIN downstream d ON g.feeds = d.name)
      SELECT name, hops FROM downstream ORDER BY hops""").fetchall(), [('spring', 0), ('mill', 1), ('town', 2), ('harbour', 3)])
