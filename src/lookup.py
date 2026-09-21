"""Demo fixture: a deliberate SQL-injection pattern for code scanning.

NOT REAL CODE. Nothing calls this in production; it exists so CodeQL raises an
alert that the platform's remediation workflow can be shown fixing.
"""
import sqlite3
import sys


def lookup_user(conn: sqlite3.Connection, user_id: str):
    cur = conn.cursor()
    # DELIBERATE FLAW: user input concatenated straight into SQL.
    cur.execute("SELECT name FROM users WHERE id = '" + user_id + "'")
    return cur.fetchall()


def main() -> None:
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE users (id TEXT, name TEXT)")
    print(lookup_user(conn, sys.argv[1]))


if __name__ == "__main__":
    main()
