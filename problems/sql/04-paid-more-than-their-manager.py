"""
Paid More Than Their Manager (easy) · patterns: self-join

A table employee(id, name, salary, manager_id) holds everyone in a company,
and manager_id is the id of the person they report to, or NULL at the top.
Write a query that returns every employee who earns strictly more than their
direct manager, as columns name, salary and manager_salary, sorted by name.

Examples:

    Input:  employee = [(1, "Ana", 120, None), (2, "Ben", 90, 1), (3, "Cleo", 130, 1), (4, "Dev", 95, 3), (5, "Finn", 100, 4)]
    Output: [("Cleo", 130, 120), ("Finn", 100, 95)]
    Why:    Cleo out-earns Ana, and Finn out-earns Dev, who reports to Cleo

    Input:  employee = [(1, "Ana", 100, None), (2, "Ben", 100, 1)]
    Output: []
    Why:    edge case, an equal salary is not more

Approach:
    The manager's salary sits in another row of the same table, so the table
    is joined to itself: alias e is the employee, alias m is the manager,
    and m.id = e.manager_id lines each person up with their boss. After
    that, the comparison is an ordinary WHERE. The inner join is deliberate:
    the person at the top has a NULL manager_id, matches nothing and
    disappears, which is right because nobody can out-earn a manager they do
    not have. A correlated subquery, e.salary > (SELECT salary FROM employee
    WHERE id = e.manager_id), gives the same answer. With id as the primary
    key each manager lookup is O(log n), so the whole query is O(n log n).

The lesson behind it: INNER and OUTER JOINs
    https://bytepatterns.com/learn/sql/joins-inner-outer
    python sql/05-joins-inner-outer.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/sql/paid-more-than-their-manager

Run it:  python problems/sql/04-paid-more-than-their-manager.py
"""


import sqlite3

QUERY = """
SELECT e.name, e.salary, m.salary AS manager_salary
FROM employee e
JOIN employee m ON m.id = e.manager_id
WHERE e.salary > m.salary
ORDER BY e.name
"""

def run(employees):
    db = sqlite3.connect(":memory:")
    db.execute("CREATE TABLE employee (id INTEGER PRIMARY KEY, name TEXT, salary INTEGER, manager_id INTEGER)")
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
    check(run([(1, "Ana", 120, None), (2, "Ben", 90, 1), (3, "Cleo", 130, 1), (4, "Dev", 95, 3), (5, "Finn", 100, 4)]), [('Cleo', 130, 120), ('Finn', 100, 95)])
    check(run([(1, "Ana", 100, None), (2, "Ben", 100, 1)]), [])
