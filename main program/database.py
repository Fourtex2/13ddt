import sqlite3
import os

db_location = os.path.join(os.path.dirname(__file__), "data", "database.db") #defines where the data file and database are


def connection(): #makes the database
    os.makedirs(os.path.dirname(db_location), exist_ok=True)
    return sqlite3.connect(db_location)

def create_tables():
    with connection() as conn:
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                username    TEXT    NOT NULL UNIQUE,
                password    TEXT    NOT NULL UNIQUE,
            )
        """)
        # Seed children if table is empty
        cursor.execute("SELECT COUNT(*) FROM users")
        if cursor.fetchone()[0] == 0:
            cursor.execute("INSERT INTO users (username, password) VALUES (user_a, password_a)")
            cursor.execute("INSERT INTO users (username, password) VALUES (user_b, password_b)")
            cursor.execute("INSERT INTO users (username, password) VALUES (user_c, password_c)")
        conn.commit()


def load_user() -> list[dict]:
    with connection() as conn:
        cur = conn.cursor()
        cur.execute("SELECT username, password FROM users ORDER BY id")
        return [{"username": row[0], "password": row[1]} for row in cur.fetchall()]