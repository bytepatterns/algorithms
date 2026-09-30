"""
Department With the Highest Average Pay (medium) · patterns: group-by, cte, ties

A table employee(id, name, dept, salary) holds one row per person. Write a
query that returns the department with the highest average salary, together
with that average rounded to two decimals, as columns dept and avg_salary.
When several departments tie for the highest average, return all of them,
sorted by department.

Examples:

    Input:  employee = [(1, "Ana", "eng", 120), (2, "Cleo", "eng", 130), (3, "Dev", "ops", 95), (4, "Finn", "ops", 100), (5, "Gus", "hr", 70)]
    Output: [("eng", 125.0)]
    Why:    the averages are eng 125, ops 97.5 and hr 70

    Input:  employee = [(1, "Ana", "eng", 100), (2, "Ben", "eng", 110), (3, "Dev", "ops", 105)]
    Output: [("eng", 105.0), ("ops", 105.0)]
    Why:    both departments average 105, so both come back

    Input:  employee = [(1, "Ana", "sales", 100), (2, "Ben", "sales", 100), (3, "Cy", "sales", 101)]
    Output: [("sales", 100.33)]
    Why:    edge case, 301 / 3 is rounded to two decimals only for display

Approach:
    GROUP BY dept with AVG(salary) gives one row per department, and naming
    that result in a WITH clause lets the query read it twice: once to find
    the highest average with MAX, once to keep every department that reaches
    it. Comparing against the maximum rather than taking the first row after
    a sort is what keeps ties, since LIMIT 1 returns one arbitrary winner
    out of several. Rounding happens only in the last SELECT, because
    rounding before comparing could make two different averages look equal.
    Grouping is O(n) with hashing or O(n log n) with sorting, and the CTE
    has one row per department, so reading it twice costs almost nothing.

The lesson behind it: Aggregations & GROUP BY
    https://bytepatterns.com/learn/sql/aggregations-group-by
    python sql/04-aggregations-group-by.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/sql/department-with-the-highest-average-pay

Run it:  python problems/sql/05-department-with-the-highest-average-pay.py
"""


import sqlite3

QUERY = """
WITH dept_avg AS (
    SELECT dept, AVG(salary) AS avg_salary
    FROM employee
    GROUP BY dept
)
SELECT dept, ROUND(avg_salary, 2) AS avg_salary
FROM dept_avg
WHERE avg_salary = (SELECT MAX(avg_salary) FROM dept_avg)
ORDER BY dept
"""

def run(employees):
    db = sqlite3.connect(":memory:")
    db.execute("CREATE TABLE employee (id INTEGER PRIMARY KEY, name TEXT, dept TEXT, salary INTEGER)")
    db.executemany("INSERT INTO employee VALUES (?, ?, ?, ?)", employees)
    return db.execute(QUERY).fetchall()


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(run([(1, "Ana", "eng", 120), (2, "Cleo", "eng", 130), (3, "Dev", "ops", 95), (4, "Finn", "ops", 100), (5, "Gus", "hr", 70)]), [('eng', 125.0)])
    check(run([(1, "Ana", "eng", 100), (2, "Ben", "eng", 110), (3, "Dev", "ops", 105)]), [('eng', 105.0), ('ops', 105.0)])
    check(run([(1, "Ana", "sales", 100), (2, "Ben", "sales", 100), (3, "Cy", "sales", 101)]), [('sales', 100.33)])
