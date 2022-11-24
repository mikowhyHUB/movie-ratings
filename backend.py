import sqlite3

# creating database


def database():
    conn = sqlite3.connect('films.db')
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS films (id INTEGER PRIMARY KEY, title TEXT, year INTEGER, director TEXT, rating REAL) ")
    conn.commit()
    conn.close()

# creating button functions


def add_film(title, year, director, rating):
    conn = sqlite3.connect('films.db')
    cur = conn.cursor()
    # null is for id
    cur.execute("INSERT INTO films VALUES (NULL, ?,?,?,?)",
                (title, year, director, rating))
    conn.commit()
    conn.close()


def view_list():
    conn = sqlite3.connect('films.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM films")
    data = cur.fetchall()
    conn.close()
    return data
# empty strings for error protection


def search(title="", year="", director="", rating=""):
    conn = sqlite3.connect('films.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM films WHERE title=? OR year=? OR director=? OR rating=?",
                (title, year, director, rating))
    data = cur.fetchall()
    conn.close()
    return data


def delete(id):
    conn = sqlite3.connect('films.db')
    cur = conn.cursor()
    # null is for id
    cur.execute("DELETE FROM films WHERE id=?", (id,))
    conn.commit()
    conn.close()


def update(id, title, year, director, rating):
    conn = sqlite3.connect('films.db')
    cur = conn.cursor()
    # null is for id
    cur.execute("UPDATE films SET title=?, year=?,director=?,rating=? WHERE id=?",
                (title, year, director, rating, id))
    conn.commit()
    conn.close()


database()

# update(3, 'THe test', '999', 'tarantino', '10')
# add_film('Test3', 1237, 'Bans', 9)
# delete(2)
# print(search(title='', year='2137'))
print(view_list())
