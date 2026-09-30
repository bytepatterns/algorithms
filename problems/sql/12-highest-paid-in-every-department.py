"""
Highest Paid in Every Department (medium) · patterns: correlated-subquery, max, ties

A table employee(id, name, dept, salary) holds one row per person. Write a
query that returns, for every department, the people who earn that
department's highest salary, as columns dept, name and salary. When several
people share the top salary of a department, return all of them. Sort by
dept, then name.

Examples:

    Input:  employee = [(1, "Ana", "eng", 120), (2, "Ben", "eng", 150), (3, "Cy", "ops", 90), (4, "Dee", "ops", 80)]
    Output: [("eng", "Ben", 150), ("ops", "Cy", 90)]

    Input:  employee = [(1, "Ana", "eng", 150), (2, "Ben", "eng", 150), (3, "Cy", "eng", 100)]
    Output: [("eng", "Ana", 150), ("eng", "Ben", 150)]
    Why:    Ana and Ben tie for the top of eng, so both come back

    Input:  employee = [(1, "Gus", "hr", 70)]
    Output: [("hr", "Gus", 70)]
    Why:    edge case, the only person in a department is its top earner

Approach:
    A correlated subquery is re-evaluated for each outer row with that row's
    values in scope, so (SELECT MAX(salary) FROM employee WHERE dept =
    e.dept) is "the top salary of this person's department". Keeping the
    rows whose salary equals it returns every top earner, ties included,
    because equality does not pick a winner the way LIMIT 1 does. An
    equivalent form groups once in a derived table, SELECT dept, MAX(salary)
    per department, and joins it back on both columns; the planner often
    turns the correlated form into exactly that. RANK() OVER (PARTITION BY
    dept ORDER BY salary DESC) = 1 is a third answer. Done naively the
    subquery rescans the table per row, O(n²); with an index on (dept,
    salary) each lookup is O(log n).

The lesson behind it: Subqueries
    https://bytepatterns.com/learn/sql/subqueries
    python sql/06-subqueries.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/sql/highest-paid-in-every-department

Run it:  python problems/sql/12-highest-paid-in-every-department.py
"""


import sqlite3

QUERY = """
SELECT e.dept, e.name, e.salary
FROM employee AS e
WHERE e.salary = (
    SELECT MAX(salary)
    FROM employee
    WHERE dept = e.dept
)
ORDER BY e.dept, e.name
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
    check(run([(1, "Ana", "eng", 120), (2, "Ben", "eng", 150), (3, "Cy", "ops", 90), (4, "Dee", "ops", 80)]), [('eng', 'Ben', 150), ('ops', 'Cy', 90)])
    check(run([(1, "Ana", "eng", 150), (2, "Ben", "eng", 150), (3, "Cy", "eng", 100)]), [('eng', 'Ana', 150), ('eng', 'Ben', 150)])
    check(run([(1, "Gus", "hr", 70)]), [('hr', 'Gus', 70)])
