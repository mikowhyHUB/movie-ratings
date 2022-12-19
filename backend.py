import sqlite3

# creating database


class Database:

    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS films (id INTEGER PRIMARY KEY, title TEXT, year INTEGER, director TEXT, rating REAL) ")
        self.conn.commit()

    # creating button functions

    def add_film(self, title, year, director, rating):
        # null is for id
        self.cur.execute("INSERT INTO films VALUES (NULL, ?,?,?,?)",
                         (title, year, director, rating))
        self.conn.commit()

    def view_list(self):
        self.cur.execute("SELECT * FROM films")
        data = self.cur.fetchall()
        return data
    # empty strings for error protection

    def search(self, title="", year="", director="", rating=""):
        self.cur.execute("SELECT * FROM films WHERE title=? OR year=? OR director=? OR rating=?",
                         (title, year, director, rating))
        data = self.cur.fetchall()
        return data

    def delete(self, id):
        # null is for id
        self.cur.execute("DELETE FROM films WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, title, year, director, rating):
        # null is for id
        self.cur.execute("UPDATE films SET title=?, year=?,director=?,rating=? WHERE id=?",
                         (title, year, director, rating, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
