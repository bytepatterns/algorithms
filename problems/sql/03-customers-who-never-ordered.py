"""
Customers Who Never Ordered (easy) · patterns: left-join, anti-join

Two tables: customer(id, name) and orders(id, customer_id), where
orders.customer_id points at customer.id. Guest checkouts are stored with a
NULL customer_id. Write a query that returns the names of the customers who
have never placed an order, as a single column name, sorted by name.

Examples:

    Input:  customer = [(1, "Ana"), (2, "Ben"), (3, "Cy")]
            orders   = [(10, 1), (11, 1), (12, 3)]
    Output: [("Ben",)]
    Why:    Ana has two orders and Cy has one

    Input:  customer = [(1, "Ana"), (2, "Ben")]
            orders   = [(10, 1), (11, None)]
    Output: [("Ben",)]
    Why:    order 11 was a guest checkout and belongs to nobody

    Input:  customer = [(1, "Ana"), (2, "Ben")]
            orders   = []
    Output: [("Ana",), ("Ben",)]
    Why:    edge case, with no orders at all every customer qualifies

Approach:
    A LEFT JOIN keeps every customer and pairs each one with its orders; a
    customer with no order is paired with a single row of NULLs. Testing a
    column that can never be NULL in a real order, such as o.id, picks out
    exactly those customers. This shape is called an anti-join, and NOT
    EXISTS (SELECT 1 FROM orders o WHERE o.customer_id = c.id) expresses the
    same thing. The tempting WHERE id NOT IN (SELECT customer_id FROM
    orders) is wrong here: the guest order puts a NULL in that list, x NOT
    IN (..., NULL) is never true, and the query returns nothing. With an
    index on orders.customer_id each customer costs one index lookup, O(n
    log m) for n customers and m orders.

The lesson behind it: INNER and OUTER JOINs
    https://bytepatterns.com/learn/sql/joins-inner-outer
    python sql/05-joins-inner-outer.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/sql/customers-who-never-ordered

Run it:  python problems/sql/03-customers-who-never-ordered.py
"""


import sqlite3

QUERY = """
SELECT c.name
FROM customer c
LEFT JOIN orders o ON o.customer_id = c.id
WHERE o.id IS NULL
ORDER BY c.name
"""

def run(customers, orders):
    db = sqlite3.connect(":memory:")
    db.execute("CREATE TABLE customer (id INTEGER PRIMARY KEY, name TEXT)")
    db.execute("CREATE TABLE orders (id INTEGER PRIMARY KEY, customer_id INTEGER)")
    db.executemany("INSERT INTO customer VALUES (?, ?)", customers)
    db.executemany("INSERT INTO orders VALUES (?, ?)", orders)
    return db.execute(QUERY).fetchall()


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(run([(1, "Ana"), (2, "Ben"), (3, "Cy")], [(10, 1), (11, 1), (12, 3)]), [('Ben',)])
    check(run([(1, "Ana"), (2, "Ben")], [(10, 1), (11, None)]), [('Ben',)])
    check(run([(1, "Ana"), (2, "Ben")], []), [('Ana',), ('Ben',)])
