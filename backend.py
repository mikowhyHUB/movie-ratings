import sqlite3


def database():
    conn = sqlite3.connect('films.db')
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS films (id INTEGER PRIMARY KEY, film title TEXT, year INTEGER, director TEXT, rating REAL) ")
    conn.commit()
    conn.close()


database()
