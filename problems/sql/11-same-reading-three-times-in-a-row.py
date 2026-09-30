"""
Same Reading Three Times in a Row (medium) · patterns: self-join, consecutive-rows, distinct

A sensor appends one row per reading to reading(id, value). The id column
counts up by exactly 1 per row with no gaps, so it records the order the
readings arrived in. Write a query that returns every value that was read at
least three times in a row, as a single column value, sorted, with each
value listed once.

Examples:

    Input:  reading = [(1, 1), (2, 1), (3, 1), (4, 2), (5, 1), (6, 2), (7, 2)]
    Output: [(1,)]
    Why:    rows 1 to 3 all read 1; 2 appears three times but never three rows in a row

    Input:  reading = [(1, 7), (2, 7), (3, 7), (4, 7), (5, 3), (6, 3), (7, 3)]
    Output: [(3,), (7,)]
    Why:    a run of four 7s contains two runs of three, but 7 is still listed once

    Input:  reading = [(1, 5), (2, 5)]
    Output: []
    Why:    edge case, two equal rows are not enough

Approach:
    Give the table three aliases and let the join conditions describe the
    shape of a run: b is the row right after a and c the row after that, and
    both must hold a's value. An inner join keeps only the combinations
    where all three rows exist and agree, so each surviving a row is the
    first reading of a run of at least three. A run of four starts twice (at
    its first and second row) and a value can have several separate runs,
    which is why the query needs DISTINCT. The join works because the ids
    have no gaps; if they could, you would number the rows yourself with
    ROW_NUMBER() or compare neighbours with LAG. With the primary key index
    each join lookup is O(log n), so the whole query runs in O(n log n).

The lesson behind it: INNER and OUTER JOINs
    https://bytepatterns.com/learn/sql/joins-inner-outer
    python sql/05-joins-inner-outer.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/sql/same-reading-three-times-in-a-row

Run it:  python problems/sql/11-same-reading-three-times-in-a-row.py
"""


import sqlite3

QUERY = """
SELECT DISTINCT a.value
FROM reading AS a
JOIN reading AS b ON b.id = a.id + 1 AND b.value = a.value
JOIN reading AS c ON c.id = a.id + 2 AND c.value = a.value
ORDER BY a.value
"""

def run(rows):
    db = sqlite3.connect(":memory:")
    db.execute("CREATE TABLE reading (id INTEGER PRIMARY KEY, value INTEGER)")
    db.executemany("INSERT INTO reading VALUES (?, ?)", rows)
    return db.execute(QUERY).fetchall()


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(run([(1, 1), (2, 1), (3, 1), (4, 2), (5, 1), (6, 2), (7, 2)]), [(1,)])
    check(run([(1, 7), (2, 7), (3, 7), (4, 7), (5, 3), (6, 3), (7, 3)]), [(3,), (7,)])
    check(run([(1, 5), (2, 5)]), [])
