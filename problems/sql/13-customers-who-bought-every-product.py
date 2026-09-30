"""
Customers Who Bought Every Product (medium) · patterns: group-by, having, count-distinct

A shop keeps its catalogue in product(key) and every sale in
purchase(customer_id, product_key). Every product_key in purchase exists in
product, and a customer can buy the same product many times. Write a query
that returns the customers who have bought every product in the catalogue at
least once, as a single column customer_id, sorted.

Examples:

    Input:  product = [5, 6], purchase = [(1, 5), (2, 6), (3, 5), (3, 6), (1, 6)]
    Output: [(1,), (3,)]
    Why:    customers 1 and 3 bought both 5 and 6; customer 2 never bought 5

    Input:  product = [5, 6, 7], purchase = [(1, 5), (1, 5), (1, 6), (2, 5), (2, 6), (2, 7)]
    Output: [(2,)]
    Why:    customer 1 has three rows but only two different products

    Input:  product = [8], purchase = []
    Output: []
    Why:    edge case, nobody bought anything

Approach:
    "Bought every product" is relational division, and the counting form is
    the one that fits in an interview: group the purchases by customer,
    count the distinct products in each group, and keep the groups whose
    count equals the size of the catalogue. DISTINCT inside the count is
    what stops a customer who bought the same item twice from passing with a
    product missing, and the comparison has to live in HAVING because the
    count only exists after GROUP BY has folded the rows. The count is safe
    because every purchased key exists in product; without that guarantee
    you would join to product first so stray keys cannot inflate it. The
    double NOT EXISTS form ("there is no product this customer has not
    bought") returns the same rows. Grouping costs O(n log n) with a sort or
    O(n) with hashing.

The lesson behind it: Aggregations & GROUP BY
    https://bytepatterns.com/learn/sql/aggregations-group-by
    python sql/04-aggregations-group-by.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/sql/customers-who-bought-every-product

Run it:  python problems/sql/13-customers-who-bought-every-product.py
"""


import sqlite3

QUERY = """
SELECT customer_id
FROM purchase
GROUP BY customer_id
HAVING COUNT(DISTINCT product_key) = (SELECT COUNT(*) FROM product)
ORDER BY customer_id
"""

def run(products, purchases):
    db = sqlite3.connect(":memory:")
    db.execute("CREATE TABLE product (key INTEGER PRIMARY KEY)")
    db.execute("CREATE TABLE purchase (customer_id INTEGER, product_key INTEGER REFERENCES product(key))")
    db.executemany("INSERT INTO product VALUES (?)", [(k,) for k in products])
    db.executemany("INSERT INTO purchase VALUES (?, ?)", purchases)
    return db.execute(QUERY).fetchall()


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(run([5, 6], [(1, 5), (2, 6), (3, 5), (3, 6), (1, 6)]), [(1,), (3,)])
    check(run([5, 6, 7], [(1, 5), (1, 5), (1, 6), (2, 5), (2, 6), (2, 7)]), [(2,)])
    check(run([8], []), [])
