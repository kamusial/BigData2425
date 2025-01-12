import sqlite3

conn = sqlite3.connect('data\\results.db')
c = conn.cursor()

c.execute('SELECT name FROM sqlite_master')
all = c.fetchall()

for table in all:
    print(table[0])

conn.close()