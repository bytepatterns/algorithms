"""
String Compression: One read cursor, one write cursor, no second string.

Run-length coding replaces a stretch of identical characters with the
character and how many there were. Done in place it needs two cursors: read
walks the runs, write lays the output down behind it. The write cursor can
never catch up, because two characters are only ever replaced by two or
fewer. Runs of one stay bare, and a count above nine is written one digit at
a time.

Lesson 10 of Strings, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/strings/string-compression

Run it:  python strings/10-string-compression.py
"""


def compress(chars):
    write = read = 0
    while read < len(chars):
        c, run = chars[read], 0
        while read < len(chars) and chars[read] == c:
            read += 1                 # measure the whole run first
            run += 1
        chars[write] = c
        write += 1
        if run > 1:                   # a run of one stays bare
            for d in str(run):
                chars[write] = d
                write += 1
    return write, chars[:write]


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(compress(list("aabbc")), (5, ['a', '2', 'b', '2', 'c']))
