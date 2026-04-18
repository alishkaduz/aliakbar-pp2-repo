"""
PhoneBook CLI — Practice 8
Run:  python phonebook.py
"""

import re
import csv
import sys
from connect import get_connection, init_db

PHONE_RE = re.compile(r"^\+?[\d\s\-()\[\]]{7,20}$")


def ask(label, required=False):
    while True:
        v = input(f"{label}: ").strip()
        if v or not required:
            return v
        print("required")


def show(rows, headers=("username", "first_name", "last_name", "phone")):
    if not rows:
        print("no results")
        return
    print(", ".join(headers))
    for r in rows:
        print(", ".join(str(x or "") for x in r))
    print(f"{len(rows)} row(s)")


# ── CRUD ────────────────────────────────────────────────────────────────────

def add_contact():
    username = ask("Username", required=True)
    phone    = ask("Phone",    required=True)
    if not PHONE_RE.match(phone):
        print("invalid phone"); return
    first = ask("First name")
    last  = ask("Last name")
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("CALL upsert_contact(%s,%s,%s,%s)", (username, first, last, phone))
        conn.commit()
    print("saved")


def update_contact():
    username  = ask("Username to update", required=True)
    new_first = ask("New first name (Enter to skip)")
    new_phone = ask("New phone (Enter to skip)")
    if new_phone and not PHONE_RE.match(new_phone):
        print("invalid phone"); return
    sets, vals = [], []
    if new_first: sets.append("first_name=%s"); vals.append(new_first)
    if new_phone: sets.append("phone=%s");      vals.append(new_phone)
    if not sets:
        print("nothing to update"); return
    vals.append(username)
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(f"UPDATE contacts SET {','.join(sets)} WHERE username=%s", vals)
        conn.commit()
    print("updated")


def import_csv():
    path = ask("CSV path [contacts.csv]") or "contacts.csv"
    try:
        rows = list(csv.DictReader(open(path, encoding="utf-8")))
    except FileNotFoundError:
        print(f"file not found: {path}"); return
    ok = bad = 0
    with get_connection() as conn:
        with conn.cursor() as cur:
            for r in rows:
                u, p = r.get("username","").strip(), r.get("phone","").strip()
                if not u or not p or not PHONE_RE.match(p):
                    print(f"skip: {r}"); bad += 1; continue
                cur.execute("CALL upsert_contact(%s,%s,%s,%s)",
                            (u, r.get("first_name",""), r.get("last_name",""), p))
                ok += 1
        conn.commit()
    print(f"imported {ok}, skipped {bad}")


def query_contacts():
    print("1 - by name  2 - phone prefix  3 - pattern (all fields)")
    c = input("choice: ").strip()
    with get_connection() as conn:
        with conn.cursor() as cur:
            if c == "1":
                n = ask("Name/surname", required=True)
                cur.execute("SELECT username,first_name,last_name,phone FROM contacts"
                            " WHERE first_name ILIKE %s OR last_name ILIKE %s",
                            (f"%{n}%", f"%{n}%"))
            elif c == "2":
                p = ask("Prefix", required=True)
                cur.execute("SELECT username,first_name,last_name,phone FROM contacts"
                            " WHERE phone LIKE %s", (f"{p}%",))
            else:
                p = ask("Pattern", required=True)
                cur.execute("SELECT * FROM search_contacts(%s)", (p,))
            show(cur.fetchall())


def delete_contact():
    username = ask("username (Enter to skip)")
    phone    = ask("phone (Enter to skip)")
    if not username and not phone:
        print("provide at least one"); return
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("CALL delete_contact(%s,%s)", (username or None, phone or None))
        conn.commit()
    print("deleted")


# Functions & Procedures

def fn_search():
    p = ask("Pattern", required=True)
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM search_contacts(%s)", (p,))
            show(cur.fetchall())


def fn_paged():
    lim = int(input("  Limit  [5]: ").strip() or 5)
    off = int(input("  Offset [0]: ").strip() or 0)
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM get_contacts_paged(%s,%s)", (lim, off))
            show(cur.fetchall())


def proc_bulk():
    print("enter lines as: username,first,last,phone  (blank line to finish)")
    data, lines = [], []
    while True:
        line = input("> ").strip()
        if not line:
            break
        lines.append(line)
    for line in lines:
        parts = [p.strip() for p in line.split(",")]
        if len(parts) < 4:
            print(f"skip (need 4 fields): {line}"); continue
        data.append(parts[:4])
    if not data:
        print("nothing to insert"); return
    # Build a 2-D text array literal for PostgreSQL
    arr = "ARRAY[" + ",".join(
        "ARRAY[" + ",".join(f"'{v}'" for v in row) + "]" for row in data
    ) + "]::TEXT[][]"
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(f"CALL bulk_insert_contacts({arr}, NULL)")
            invalid = cur.fetchone()
        conn.commit()
    print(f"done. invalid rows: {invalid[0] if invalid else 'none'}")


def proc_delete():
    username = ask("Username (Enter to skip)")
    phone    = ask("Phone (Enter to skip)")
    if not username and not phone:
        print("  [!] Provide at least one.\n"); return
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("CALL delete_contact(%s,%s)", (username or None, phone or None))
        conn.commit()
    print("deleted")


MENU = """
PhoneBook - Practice 8

1. add / upsert contact
2. update contact
3. import CSV
4. query contacts
5. delete contact
6. search_contacts(pattern)
7. get_contacts_paged(limit, offset)
8. bulk_insert_contacts
9. delete_contact procedure
0. exit
"""

ACTIONS = {
    "1": add_contact, "2": update_contact, "3": import_csv,
    "4": query_contacts, "5": delete_contact,
    "6": fn_search, "7": fn_paged, "8": proc_bulk, "9": proc_delete,
}

if __name__ == "__main__":
    try:
        init_db()
    except Exception as e:
        print(f"db connection failed: {e}"); sys.exit(1)

    while True:
        print(MENU)
        choice = input("choice: ").strip()
        if choice == "0":
            break
        action = ACTIONS.get(choice)
        if action:
            try:
                action()
            except Exception as e:
                print(f"error: {e}")
        else:
            print("invalid choice")