import sqlite3
import hashlib


db = sqlite3.connect("backend/users.db")

cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY,
username TEXT UNIQUE,
password TEXT,
balance REAL
)
""")

db.commit()


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def register(username, password):
    try:
        cursor.execute(
            "INSERT INTO users VALUES(NULL,?,?,?)",
            (username, hash_password(password), 1000)
        )
        db.commit()
        return "REGISTERED"
    except:
        return "USER_EXISTS"


def login(username, password):
    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, hash_password(password))
    )

    user = cursor.fetchone()

    if user:
        return user

    return None


def deposit(username, amount):
    cursor.execute(
        "UPDATE users SET balance=balance+? WHERE username=?",
        (amount, username)
    )
    db.commit()


def withdraw(username, amount):
    cursor.execute(
        "UPDATE users SET balance=balance-? WHERE username=?",
        (amount, username)
    )
    db.commit()
