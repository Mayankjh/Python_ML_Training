#database with python

import sqlite3 as sq
conn = sq.connect("courses.db")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE if not exists courses(
               number INTEGER PRIMARY KEY,
               name text,
               ects real);""")

# normal insertion

#cursor.execute("""INSERT INTO courses VALUES("02820","Python programming",5);""")

# inserstion through variable

#courses = ("02345","NonLinear Signal IDk",12)
#cursor.execute("INSERT INTO courses values(?,?,?);",courses)

# many entries at once
#courses = [("2323","introduction to cognitive Science",6),("2327","introduction to Python",3)]
#cursor.executemany("INSERT INTO courses values(?,?,?);",courses)
#conn.commit()

#Fetch data from db

#cursor.execute("SELECT * FROM courses;")
#print(cursor.fetchone()) # Return one row at a time with fetch one
#for row in cursor:
#    print(row)

# Limiting no. of rows
#cursor.execute("SELECT * FROM courses ORDER BY number LIMIT 2;")
#print(cursor.fetchall())


# search for specific values

# cursor.execute("Select * from courses where number=? or name=? or ects=?",("2327",12,6))
# rows = cursor.fetchall()
# print(rows)

#paramaterize search data into python variable

# param ={'ects':10.0}
# cursor.execute("SELECT number From courses WHERE ects=?",(param['ects'],))
# print(cursor.fetchall())

# Updating data in SQLlite
# cursor.execute("update courses set name=?,ects=? where number=?",('MAX','99','2327'))
# cursor.execute("SELECT * FROM courses;")
# print(cursor.fetchall())

# deleting From database
cursor.execute("DELETE FROM courses where number=?",("2345",))
conn.commit()
cursor.execute("SELECT * FROM courses;")
print(cursor.fetchall())
conn.close()