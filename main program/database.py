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
                password    TEXT    NOT NULL
            )
        """)

        cursor.execute("SELECT COUNT(*) FROM users")
        if cursor.fetchone()[0] == 0:
            cursor.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                ("user_a", "password_a")
            )

            cursor.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                ("user_b", "password_b")
            )

            cursor.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                ("user_c", "password_c")
            )
            conn.commit()
            
def check_login(username, password):
    with connection() as conn:
        cursor = conn.cursor()

        cursor.execute(
            "SELECT username FROM users WHERE username = ? AND password = ?",
            (username, password)
        )

        user = cursor.fetchone()

        if user:
            return True

        return False

def add_user(username, password):
    with connection() as conn:
        cursor = conn.cursor()

        try:
            cursor.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                (username, password)
            )
            conn.commit()
            return True

        except sqlite3.IntegrityError:
            return False