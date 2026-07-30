



import sqlite3
from pathlib import Path

DATABASE = Path("database/history.db")


def get_connection():

    DATABASE.parent.mkdir(exist_ok=True)

    conn = sqlite3.connect(DATABASE)

    conn.row_factory = sqlite3.Row

    return conn