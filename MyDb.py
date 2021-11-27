import sqlite3
conn = sqlite3.connect("My_cats.db")

def create_table():
    cursor.execute("""CREATE TABLE IF NOT EXISTS types
    (id INTEGER PRIMARY KEY UNIQUE,
     type VARCHAR (100)  NOT NULL)""")
    

def insert_type():
    cursor.execute("""INSERT INTO types  VALUES (1, 'Australian Mist')""")
    cursor.execute("""INSERT INTO types  VALUES (2, 'AmericanWireHaired')""")
    cursor.execute("""INSERT INTO types  VALUES (3, 'RussianCat')""")
    conn.commit()

if __name__ == "__main__":
    cursor = conn.cursor()
    create_table()
    insert_type()
