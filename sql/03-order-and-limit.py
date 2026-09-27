"""
ORDER BY and LIMIT: Sort once in the engine, then take only the slice you show.

ORDER BY sorts the result; LIMIT cuts it short. Together they answer every
"top N" question in one round trip, and the engine can often stop early
instead of sorting everything. Alone, LIMIT is a trap: with no ORDER BY, the
rows you keep are simply the ones that arrived first.

Lesson 3 of SQL, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/sql/order-and-limit

Run it:  python sql/03-order-and-limit.py
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
      CREATE TABLE runner (bib INTEGER, name TEXT, seconds INTEGER);
      INSERT INTO runner VALUES (14, 'Ada', 9120), (7, 'Bruno', 8755),
                                (22, 'Chi', 9040), (3, 'Dara', 8890);
    """)
    podium = db.execute("""
      SELECT name, seconds FROM runner
      ORDER BY seconds ASC
      LIMIT 3
    """).fetchall()
    check(podium, [('Bruno', 8755), ('Dara', 8890), ('Chi', 9040)])
