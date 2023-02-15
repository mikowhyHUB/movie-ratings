import sqlite3


class Database:

    def __init__(self, db: str) -> None:
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS films (id INTEGER PRIMARY KEY, title TEXT, year INTEGER, director TEXT, rating REAL) ")
        self.conn.commit()

    def add_film(self, title: str, year: str, director: str, rating: str) -> None:
        """This function adds a new film to the films table in the database. It takes four parameters and inserts
        them into the table."""
        self.cur.execute("INSERT INTO films VALUES (NULL, ?,?,?,?)",
                         (title, year, director, rating))
        self.conn.commit()

    def view_list(self) -> list:
        """This function is used to view a list of films from the films table in the database. It returns the data
        from the query in the form of a list"""
        self.cur.execute("SELECT * FROM films")
        data = self.cur.fetchall()
        return data

    def search(self, title: str = "", year: str = "", director: str = "", rating: str = "") -> list:
        """This function searches a database for films with the given parameters."""
        self.cur.execute("SELECT * FROM films WHERE title=? OR year=? OR director=? OR rating=?",
                         (title, year, director, rating))
        data = self.cur.fetchall()
        return data

    def delete(self, id: str) -> None:
        """This function deletes a record from the films table in the database. """
        self.cur.execute("DELETE FROM films WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id: str, title: str, year: str, director: str, rating: str) -> None:
        """This method updates an existing film in the database with the given id.
        The changes are then committed to the database."""
        self.cur.execute("UPDATE films SET title=?, year=?,director=?,rating=? WHERE id=?",
                         (title, year, director, rating, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
