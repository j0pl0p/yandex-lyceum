import sqlite3

con = sqlite3.connect("films_db.sqlite")
cur = con.cursor()

result = cur.execute('''SELECT title 
FROM films 
WHERE title like "%Астерикс%" AND title NOT like "%Обеликс%"''').fetchall()

for elem in result:
    print(elem[0])

con.close()
