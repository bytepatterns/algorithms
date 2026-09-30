"""
Author Book Counts in One Query (medium) · patterns: n-plus-one, left-join, group-by

Two tables: author(id, name) and book(id, author_id, title). A page lists
every author with the number of books they wrote. Its code first runs SELECT
id, name FROM author and then, inside a loop, one SELECT COUNT(*) FROM book
WHERE author_id = ? per author, which is N + 1 statements for N authors.
Rewrite it as a single query that returns name and books for every author,
including authors with no books, sorted by name. The database must receive
exactly one statement.

Examples:

    Input:  author = [(1, "Ana"), (2, "Ben"), (3, "Cy")]
            book   = [(10, 1, "Dune"), (11, 1, "Emma"), (12, 3, "Ivy")]
    Output: rows = [("Ana", 2), ("Ben", 0), ("Cy", 1)], statements = 1
    Why:    the loop version would send 4 statements for these 3 authors

    Input:  author = [(1, "Ana")]
            book   = []
    Output: rows = [("Ana", 0)], statements = 1
    Why:    edge case, an author without books still appears, with 0

Approach:
    The loop pays one round trip per author, and each trip is a separate
    parse, plan and network hop, which is what makes an N + 1 page slow as
    the list grows. One LEFT JOIN from author to book brings all the pairs
    back in a single statement, and GROUP BY turns them into one count per
    author. LEFT keeps authors with no books, and COUNT(b.id) counts only
    real books, because COUNT of a column skips NULL while COUNT(*) counts
    the NULL-filled row of a bookless author as 1. The code records every
    statement SQLite runs with set_trace_callback, so the example proves the
    page now costs one statement instead of N + 1. With an index on
    book.author_id the join is O(n log m) for n authors and m books.

The lesson behind it: The N+1 Query Problem
    https://bytepatterns.com/learn/sql/n-plus-one-problem
    python sql/10-n-plus-one-problem.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/sql/author-book-counts-in-one-query

Run it:  python problems/sql/07-author-book-counts-in-one-query.py
"""


import sqlite3

QUERY = """
SELECT a.name, COUNT(b.id) AS books
FROM author a
LEFT JOIN book b ON b.author_id = a.id
GROUP BY a.id, a.name
ORDER BY a.name
"""

def setup(authors, books):
    db = sqlite3.connect(":memory:")
    db.execute("CREATE TABLE author (id INTEGER PRIMARY KEY, name TEXT)")
    db.execute("CREATE TABLE book (id INTEGER PRIMARY KEY, author_id INTEGER, title TEXT)")
    db.executemany("INSERT INTO author VALUES (?, ?)", authors)
    db.executemany("INSERT INTO book VALUES (?, ?, ?)", books)
    return db

def run(authors, books):
    db = setup(authors, books)
    sent = []
    db.set_trace_callback(sent.append)        # record every statement SQLite runs
    rows = db.execute(QUERY).fetchall()
    return rows, len(sent)


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(run([(1, "Ana"), (2, "Ben"), (3, "Cy")], [(10, 1, "Dune"), (11, 1, "Emma"), (12, 3, "Ivy")]), ([('Ana', 2), ('Ben', 0), ('Cy', 1)], 1))
    check(run([(1, "Ana")], []), ([('Ana', 0)], 1))
