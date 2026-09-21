"""Demo fixture: deliberate security flaws for code scanning.

NOT REAL CODE. Nothing imports this, it connects to nothing, and every value in
it is invented. It exists so CodeQL raises alerts that the platform's governed
remediation workflow (SKL-SEC-012) can be shown fixing.

Several unrelated flaw classes are present on purpose, so the fixture does not
depend on any single CodeQL query firing.
"""
import hashlib
import os
import sqlite3
import subprocess
import sys

# py/hardcoded-credentials — invented value, not a real secret.
DB_PASSWORD = "hunter2-not-a-real-password"


def connect() -> dict:
    return {"user": "admin", "password": DB_PASSWORD}


def hash_password(password: str) -> str:
    # py/weak-sensitive-data-hashing — MD5 for a password.
    return hashlib.md5(password.encode()).hexdigest()


def compute(expr: str):
    # py/code-injection — eval on caller-supplied text.
    return eval(expr)


def read_report(name: str) -> str:
    # py/path-injection — unsanitised path joined onto a base directory.
    with open("/var/reports/" + name) as fh:
        return fh.read()


def archive(name: str) -> None:
    # py/shell-command-constructed-from-input — shell=True with concatenation.
    subprocess.call("tar -czf /tmp/reports.tgz " + name, shell=True)


def lookup_user(conn: sqlite3.Connection, user_id: str):
    # py/sql-injection — user input concatenated straight into SQL.
    cur = conn.cursor()
    cur.execute("SELECT name FROM users WHERE id = '" + user_id + "'")
    return cur.fetchall()


def main() -> None:
    arg = sys.argv[1]
    print(compute(arg))
    print(read_report(arg))
    archive(arg)
    os.system("echo " + arg)
    print(hash_password(arg))
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE users (id TEXT, name TEXT)")
    print(lookup_user(conn, arg))


if __name__ == "__main__":
    main()
