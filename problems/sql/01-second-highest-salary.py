"""
Second Highest Salary (easy) · patterns: scalar-subquery, aggregate

A table employee(id, name, salary) holds one row per person, and several
people may earn the same amount. Write a query that returns exactly one row
with one column, second_highest: the second-highest distinct salary. When
there is no second distinct salary, the row must still come back, holding
NULL.

Examples:

    Input:  employee = [(1, "Ana", 300), (2, "Ben", 200), (3, "Cy", 100)]
    Output: [(200,)]
    Why:    300 is the highest, and the highest salary below it is 200

    Input:  employee = [(1, "Ana", 300), (2, "Ben", 300), (3, "Cy", 200)]
    Output: [(200,)]
    Why:    two people share 300, but salaries are compared as distinct values

    Input:  employee = [(1, "Ana", 300)]
    Output: [(None,)]
    Why:    edge case, one row still comes back and it holds NULL

Approach:
    The scalar subquery (SELECT MAX(salary) FROM employee) produces one
    value, the top salary, and the outer WHERE keeps only the rows below it,
    so a repeated top salary is removed in one go. The outer MAX then picks
    the best of what is left. The empty case needs no special code: an
    aggregate without GROUP BY always returns one row, and MAX of no rows is
    NULL. The popular alternative, ORDER BY salary DESC with LIMIT 1 OFFSET
    1 over the distinct salaries, returns no row at all when there is no
    second salary, so it has to be wrapped in another SELECT to turn that
    into NULL. The query reads the table twice, O(n), and an index on salary
    turns both maximums into O(log n) lookups.

The lesson behind it: Subqueries
    https://bytepatterns.com/learn/sql/subqueries
    python sql/06-subqueries.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/sql/second-highest-salary

Run it:  python problems/sql/01-second-highest-salary.py
"""


import sqlite3

QUERY = """
SELECT MAX(salary) AS second_highest
FROM employee
WHERE salary < (SELECT MAX(salary) FROM employee)
"""

def run(employees):
    db = sqlite3.connect(":memory:")
    db.execute("CREATE TABLE employee (id INTEGER PRIMARY KEY, name TEXT, salary INTEGER)")
    db.executemany("INSERT INTO employee VALUES (?, ?, ?)", employees)
    return db.execute(QUERY).fetchall()


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(run([(1, "Ana", 300), (2, "Ben", 200), (3, "Cy", 100)]), [(200,)])
    check(run([(1, "Ana", 300), (2, "Ben", 300), (3, "Cy", 200)]), [(200,)])
    check(run([(1, "Ana", 300)]), [(None,)])
