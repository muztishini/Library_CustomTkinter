import sqlite3;
 
con = sqlite3.connect("libdb.db")
cursor = con.cursor()
 
# создаем таблицу people
cursor.execute("""CREATE TABLE book
                (id INTEGER PRIMARY KEY AUTOINCREMENT,  
                name TEXT,
                author TEXT,
                genre TEXT,
                pages INTEGER,                 
                year INTEGER,
                quantity INTEGER)
            """)

