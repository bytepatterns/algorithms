"""
INNER and OUTER JOINs: Match rows across tables — and decide who survives a miss.

A join lines up rows from two tables on a matching condition. INNER JOIN
keeps only the pairs that matched. LEFT JOIN keeps every left-hand row
regardless, padding the right side with NULL. Choosing between them is
really choosing what a missing match should mean.

Lesson 5 of SQL, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/sql/joins-inner-outer

Short video on this lesson: https://www.youtube.com/@bytepatterns

Run it:  python sql/05-joins-inner-outer.py
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
      CREATE TABLE dog (id INTEGER, name TEXT);
      CREATE TABLE adoption (dog_id INTEGER, adopter TEXT);
      INSERT INTO dog VALUES (1, 'Pepper'), (2, 'Rusty'), (3, 'Nell');
      INSERT INTO adoption VALUES (1, 'Yusuf'), (3, 'Marta');
    """)
    rows = db.execute("""
      SELECT dog.name, adoption.adopter
      FROM dog LEFT JOIN adoption ON adoption.dog_id = dog.id
    """).fetchall()
    check(rows, [('Pepper', 'Yusuf'), ('Rusty', None), ('Nell', 'Marta')])
