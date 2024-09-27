import sqlite3 as sq
conn = sq.connect('Library.db')


def create_tables():
    conn.execute('''
        CREATE TABLE iF NOT EXISTS books(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            publish_year INTEGER NOT NULL,
            price TEXT NOT NULL UNIQUE
        );
    ''')

def insert_books(title,author,publish_year,price):
    conn.execute("INSERT INTO books(title,author,publish_year,price) Values('%s','%s',%i,%f);"%(title,author,publish_year,price))
    res = conn.execute("Select * from books order by id Desc")
    print("Insert into books",res.fetchone())




create_tables()
insert_books('aa','aa',2023,23)