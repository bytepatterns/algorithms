"""
Isolation Levels: How much of another transaction's mess you are allowed to see.

Transactions run at the same time, so the engine must decide what one may
see of another's unfinished work. The levels are a ladder: read uncommitted,
read committed, repeatable read, serializable. Each rung rules out one more
anomaly and allows a little less concurrency.

Lesson 14 of SQL, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/sql/isolation-levels

Run it:  python sql/14-isolation-levels.py
"""


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    import sqlite3, os, tempfile
    path = os.path.join(tempfile.mkdtemp(), "ward.db")
    sqlite3.connect(path).executescript("""PRAGMA journal_mode=WAL;
      CREATE TABLE bed (ward TEXT, free INT); INSERT INTO bed VALUES ('ivy',3);""")
    writer = sqlite3.connect(path, isolation_level=None)
    reader = sqlite3.connect(path, isolation_level=None)
    writer.execute("BEGIN IMMEDIATE"); writer.execute("UPDATE bed SET free=0")
    reader.execute("BEGIN")                          # snapshot taken here
    check(reader.execute("SELECT free FROM bed").fetchone(), (3,))  # uncommitted hidden
    writer.execute("COMMIT")
    check(reader.execute("SELECT free FROM bed").fetchone(), (3,))  # repeatable
    reader.execute("COMMIT")
    check(reader.execute("SELECT free FROM bed").fetchone(), (0,))
