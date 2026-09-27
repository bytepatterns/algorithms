"""
Composite Indexes: Column order decides which queries the index can serve.

A composite index sorts by its first column, then by the second within that.
So it serves a filter on the leading column, or on a leading prefix, and
nothing else. Add every column the query reads and it becomes covering: the
engine answers from the index and never touches the table.

Lesson 13 of SQL, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/sql/composite-and-covering-indexes

Run it:  python sql/13-composite-and-covering-indexes.py
"""


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

import re


def _same(printed, expected):
    """Printed text vs the lesson's comment, which may add a note after it."""
    printed, expected = printed.strip(), expected.strip()
    printed = printed.replace("SCAN TABLE ", "SCAN ").replace("SEARCH TABLE ", "SEARCH ")
    wants = [expected] + [expected.rsplit(s, 1)[1].strip() for s in (" -> ", " = ") if s in expected]
    for want in wants + [w[1:] for w in wants if w.startswith("~")]:
        rest = want[len(printed):] if want.startswith(printed) else None
        if rest == "" or (rest and re.match(r"[\s,;:]+([A-Za-z]|\u2014|\u2013|-(?!\d)|\u2192|<-|\([A-Za-z]|#)", rest)):
            return True
    return False


def check_printed(*values, expect, sep=" ", end="\n"):
    """print(*values), then assert the line reads the way the lesson's comment says."""
    print(*values, sep=sep, end=end)
    forms = [sep.join(map(str, values))]
    if len(values) == 1 and isinstance(values[0], str):
        forms += [repr(values[0]), '"%s"' % values[0]] + (["(empty string)"] if not values[0] else [])
    if len(values) > 1 and isinstance(values[0], str):  # a leading label
        forms.append(sep.join(map(str, values[1:])))
    assert any(_same(f, expect) for f in forms), f"expected {expect!r}, got {forms[0]!r}"


if __name__ == "__main__":
    import sqlite3
    db = sqlite3.connect(":memory:")
    db.executescript("""CREATE TABLE dock (city TEXT, day TEXT, bikes INT);
      INSERT INTO dock VALUES ('Leeds','Mon',12),('Leeds','Tue',9),('Hull','Mon',4);""")
    q = "SELECT day, bikes FROM dock WHERE city = 'Leeds' ORDER BY day"
    check_printed(db.execute("EXPLAIN QUERY PLAN " + q).fetchall()[0][3], expect="SCAN dock")
    db.execute("CREATE INDEX i_cov ON dock(city, day, bikes)")
    check_printed(db.execute("EXPLAIN QUERY PLAN " + q).fetchall()[0][3], expect="SEARCH dock USING COVERING INDEX i_cov (city=?)")
    check_printed(db.execute(
      "EXPLAIN QUERY PLAN SELECT bikes FROM dock WHERE day='Mon'").fetchall()[0][3], expect="SCAN dock -- day is not the leading column")
