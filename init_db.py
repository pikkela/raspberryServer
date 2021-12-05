
import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO bme_data (temp, press, humid) VALUES (?, ?, ?)",
            (20.14, 48.9, 30.3)
            )

cur.execute("INSERT INTO bme_data (temp, press, humid) VALUES (?, ?, ?)",
            (89.33, 12.43, 43.32)
            )

connection.commit()
connection.close()
