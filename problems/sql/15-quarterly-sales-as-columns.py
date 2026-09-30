"""
Quarterly Sales as Columns (easy) · patterns: pivot, case-when, group-by

A table sales(region, quarter, amount) holds one row per sale, with quarter
a number from 1 to 4. Write a query that turns the quarters into columns:
one row per region with columns region, q1, q2, q3 and q4, each holding that
region's total for the quarter, or 0 when the region sold nothing in it.
Sort by region.

Examples:

    Input:  sales = [("east", 1, 100), ("east", 2, 50), ("west", 1, 70), ("east", 1, 30), ("west", 4, 20)]
    Output: [("east", 130, 50, 0, 0), ("west", 70, 0, 0, 20)]

    Input:  sales = [("north", 3, 5), ("north", 3, 5), ("north", 3, 5)]
    Output: [("north", 0, 0, 15, 0)]
    Why:    every sale falls in quarter 3, the other three columns still appear as 0

    Input:  sales = []
    Output: []
    Why:    edge case, no sales means no regions and no rows

Approach:
    This is a pivot by conditional aggregation. GROUP BY region collapses
    each region into one row, and each output column is a SUM over a CASE
    expression that passes a row's amount through only when it belongs to
    that column's quarter and contributes 0 otherwise. The CASE is a
    per-column filter: WHERE quarter = 1 would throw the other quarters'
    rows away for every column, while the CASE lets each column keep its own
    rows. The ELSE 0 is deliberate, because SUM over nothing but NULLs is
    NULL, not 0. Some databases have a PIVOT keyword or FILTER (WHERE …)
    clause, but CASE inside an aggregate works everywhere. The query reads
    the table once and groups it, O(n) with hashing.

The lesson behind it: WHERE and Filtering
    https://bytepatterns.com/learn/sql/where-and-filtering
    python sql/02-where-and-filtering.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/sql/quarterly-sales-as-columns

Run it:  python problems/sql/15-quarterly-sales-as-columns.py
"""


import sqlite3

QUERY = """
SELECT region,
       SUM(CASE WHEN quarter = 1 THEN amount ELSE 0 END) AS q1,
       SUM(CASE WHEN quarter = 2 THEN amount ELSE 0 END) AS q2,
       SUM(CASE WHEN quarter = 3 THEN amount ELSE 0 END) AS q3,
       SUM(CASE WHEN quarter = 4 THEN amount ELSE 0 END) AS q4
FROM sales
GROUP BY region
ORDER BY region
"""

def run(rows):
    db = sqlite3.connect(":memory:")
    db.execute("CREATE TABLE sales (region TEXT, quarter INTEGER, amount INTEGER)")
    db.executemany("INSERT INTO sales VALUES (?, ?, ?)", rows)
    return db.execute(QUERY).fetchall()


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(run([("east", 1, 100), ("east", 2, 50), ("west", 1, 70), ("east", 1, 30), ("west", 4, 20)]), [('east', 130, 50, 0, 0), ('west', 70, 0, 0, 20)])
    check(run([("north", 3, 5), ("north", 3, 5), ("north", 3, 5)]), [('north', 0, 0, 15, 0)])
    check(run([]), [])
