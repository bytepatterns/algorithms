"""
Transactions & ACID: All of the writes land, or none of them do.

A transaction wraps several statements into one unit of work: Atomic (all or
nothing), Consistent (constraints always hold), Isolated (others do not see
your half-finished state) and Durable (a commit survives a crash). If any
step fails, the engine unwinds every earlier step with it.

Lesson 8 of SQL, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/sql/transactions-acid

Run it:  python sql/08-transactions-acid.py
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
      CREATE TABLE loan (museum TEXT, objects INTEGER CHECK (objects >= 0));
      INSERT INTO loan VALUES ('Hallam', 3), ('Verrey', 0);
    """)
    try:
        with db:   # commits at the end, rolls back if the block raises
            db.execute("UPDATE loan SET objects = objects + 1 WHERE museum = 'Hallam'")
            db.execute("UPDATE loan SET objects = objects - 1 WHERE museum = 'Verrey'")
    except sqlite3.IntegrityError:
        pass       # Verrey would go to -1, so the CHECK fires
    check(db.execute("SELECT * FROM loan").fetchall(), [('Hallam', 3), ('Verrey', 0)])  # the first UPDATE was undone as well
