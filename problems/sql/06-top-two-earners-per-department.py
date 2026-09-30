"""
Top Two Earners per Department (medium) · patterns: window-function, top-n-per-group

A table employee(id, name, dept, salary) holds one row per person. For each
department, return everyone whose salary is one of the two highest distinct
salaries in that department, so people who tie are all kept. Return columns
dept, name and salary, sorted by department, then salary from high to low,
then name.

Examples:

    Input:  employee = [(1, "Ana", "eng", 120), (2, "Ben", "eng", 90), (3, "Cleo", "eng", 130), (4, "Dev", "ops", 95), (5, "Eve", "ops", 80), (6, "Finn", "ops", 100)]
    Output: [("eng", "Cleo", 130), ("eng", "Ana", 120), ("ops", "Finn", 100), ("ops", "Dev", 95)]

    Input:  employee = [(1, "Ana", "eng", 120), (2, "Ben", "eng", 120), (3, "Cleo", "eng", 110), (4, "Dev", "eng", 100)]
    Output: [("eng", "Ana", 120), ("eng", "Ben", 120), ("eng", "Cleo", 110)]
    Why:    Ana and Ben share the top salary, so the two highest distinct salaries are 120 and 110

    Input:  employee = [(1, "Ana", "eng", 120), (2, "Gus", "hr", 70)]
    Output: [("eng", "Ana", 120), ("hr", "Gus", 70)]
    Why:    edge case, a department with one person returns that person

Approach:
    DENSE_RANK() OVER (PARTITION BY dept ORDER BY salary DESC) numbers the
    distinct salaries of each department 1, 2, 3 and gives tied people the
    same number without leaving a gap, so rank 2 always means the second
    distinct salary. ROW_NUMBER would keep exactly two people and drop one
    of a tied pair, and RANK would give the third person in the tie example
    rank 3. The filter cannot go in the same query: the logical order is
    FROM, WHERE, GROUP BY, HAVING, then SELECT, and window functions are
    computed in SELECT, after WHERE has already run. So the ranking lives in
    a subquery and the outer query filters on it. The window sorts each
    department, O(n log n) overall.

The lesson behind it: Query Execution Order
    https://bytepatterns.com/learn/sql/query-execution-order
    python sql/09-query-execution-order.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/sql/top-two-earners-per-department

Run it:  python problems/sql/06-top-two-earners-per-department.py
"""


import sqlite3

QUERY = """
SELECT dept, name, salary
FROM (
    SELECT dept, name, salary,
           DENSE_RANK() OVER (PARTITION BY dept ORDER BY salary DESC) AS rnk
    FROM employee
) AS ranked
WHERE rnk <= 2
ORDER BY dept, salary DESC, name
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
    check(run([(1, "Ana", "eng", 120), (2, "Ben", "eng", 90), (3, "Cleo", "eng", 130), (4, "Dev", "ops", 95), (5, "Eve", "ops", 80), (6, "Finn", "ops", 100)]), [('eng', 'Cleo', 130), ('eng', 'Ana', 120), ('ops', 'Finn', 100), ('ops', 'Dev', 95)])
    check(run([(1, "Ana", "eng", 120), (2, "Ben", "eng", 120), (3, "Cleo", "eng", 110), (4, "Dev", "eng", 100)]), [('eng', 'Ana', 120), ('eng', 'Ben', 120), ('eng', 'Cleo', 110)])
    check(run([(1, "Ana", "eng", 120), (2, "Gus", "hr", 70)]), [('eng', 'Ana', 120), ('hr', 'Gus', 70)])
