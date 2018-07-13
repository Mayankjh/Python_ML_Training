# Databse in Python

## SQL Lite

**  steps to initialize:
-> import database module
->connect to database
-> aquire cursor. with connection,cursor()
-> execute SQl statement. With execute(),executemany()
->fetch the results.with fetchone(),fetchmany() or fetchall()
-> commit changes. connection.commit()
-> close thec onneccton. Use close.connection() or the with keyword.

## Example Program

# database with python
import sqlite3 as sq
conn = sq.connect("courses.db")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE courses(
               number INTEGER PRIMARY KEY,
               name text,
               ects real);""")
cursor.execute("""INSERT INTO courses VALUES
               ("02820","Python programming",5);""")
conn.commit

## Fetch Syntax

cursor.execute("SELECT * FROM courses;")
print(cursor.fetchone()) # Return one row at a time with fetch one
for row in cursor:
    print(row)

## Limiting no. of rows
cursor.execute("SELECT * FROM courses ORDER BY number LIMIT 2;")
print(cursor.fetchall())

## search for specific values

 cursor.execute("Select * from courses where number=? or name=? or ects=?",("2327",12,6))
 rows = cursor.fetchall()
 print(rows)

## paramaterize search data into python variable

param ={'ects':10.0}
cursor.execute("SELECT number From courses WHERE ects=?",(param['ects'],))
print(cursor.fetchall())
conn.close()