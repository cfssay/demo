"""Demo fixture: deliberate injection patterns for code scanning.

NOT REAL CODE. Nothing calls this in production and it connects to nothing; it
exists so CodeQL raises alerts that the platform's governed remediation
workflow can be shown fixing.
"""
import os
import sqlite3
import sys


def lookup_user(conn: sqlite3.Connection, user_id: str):
    cur = conn.cursor()
    # DELIBERATE FLAW: user input concatenated straight into SQL.
    cur.execute("SELECT name FROM users WHERE id = '" + user_id + "'")
    return cur.fetchall()


def archive_report(name: str) -> None:
    # DELIBERATE FLAW: untrusted input interpolated into a shell command.
    os.system("tar -czf /tmp/reports.tgz " + name)


def main() -> None:
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE users (id TEXT, name TEXT)")
    print(lookup_user(conn, sys.argv[1]))
    archive_report(sys.argv[1])


if __name__ == "__main__":
    main()
