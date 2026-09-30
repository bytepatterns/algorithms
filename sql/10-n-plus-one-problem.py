"""
The N+1 Query Problem: One query for the list, then one more for every single row.

You fetch a list, then loop over it and query once per item. One query
becomes N+1. Each trip is cheap on its own and ruinous in aggregate, because
latency and planning cost apply every time. Fix it by fetching the related
rows in one go — a join, or a single IN (...).

Lesson 10 of SQL, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/sql/n-plus-one-problem

Short video on this lesson: https://www.youtube.com/@bytepatterns

Run it:  python sql/10-n-plus-one-problem.py
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
    db.executescript("""CREATE TABLE job (id INT, addr TEXT);
      CREATE TABLE part (job_id INT, name TEXT);
      INSERT INTO job VALUES (1,'Mill Lane'), (2,'Quay St'), (3,'Fern Rd');
      INSERT INTO part VALUES (1,'elbow'), (2,'washer'), (3,'valve');""")
    sent = []
    db.set_trace_callback(sent.append)          # count statements sent to SQLite
    for (job_id,) in db.execute("SELECT id FROM job").fetchall():   # 1 query
        db.execute("SELECT name FROM part WHERE job_id = ?", (job_id,))  # +1 each
    check(len(sent), 4)  # the N+1 pattern
    sent.clear()
    db.execute("SELECT addr, name FROM job JOIN part ON part.job_id = job.id")
    check(len(sent), 1)  # one trip, all the parts
