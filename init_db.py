import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO logs (title, content) VALUES (?, ?)",
            ('Temperature', '23.4 celsius')
            )

cur.execute("INSERT INTO logs (title, content) VALUES (?, ?)",
            ('Humidity', '67%')
            )

connection.commit()
connection.close()
