import sqlite3

conn = sqlite3.connect('example.db')
cur = conn.cursor()
cur.execute('''
CREATE TABLE IF NOT EXISTS users
(id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
age INTEGER NOT NULL)
''')

conn.commit()

cur.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Michael', 18))
cur.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Alex', 20))
conn.commit()

cur.execute("SELECT * FROM users")
rows = cur.fetchall()

for row in rows:
   print(row)

conn.close()
