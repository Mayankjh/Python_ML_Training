# id
# name 
# age 
# aim
# 
# functions:
# 1)create
# 2)insert
# 3)update
# 4)delete
# 4)search
# 5)view

# create datbase
import sqlite3 as sq
conn = sq.connect("filedata.db")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE if not exists filedata(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name text,
               age integer,
               aim text);""")
print("Connected to data base")

def InitiateProcess():
    print("1) Insert : 1\n 2) Update: 2\n 3) Delete :3\n 4) Search\n 5) View")
    a = int(input("Enter Your Choice"))
    

# inserstion through variable

#courses = ("02345","NonLinear Signal IDk",12)
#cursor.execute("INSERT INTO courses values(?,?,?);",courses)
def Insertdata():
    name= str(input("Enter Your Name:-"))
    age= int(input("Enter Your age:-"))
    aim= str(input("Enter Your aim:-"))
    cursor.execute("INSERT INTO filedata values(NULL,?,?,?);",(name,age,aim))
    conn.commit()
    print("inserted successfully...")
    conn.close()
    
def delete():
    nam=str(input("Enter the name of the person whose data is to deleted : "))
    cursor.execute("DELETE FROM filedata where name=?",(nam,))
    conn.commit()
    cursor.execute("SELECT * FROM filedata;")
    print(cursor.fetchall())
    conn.close()
    
def update():
    a = input("Enter the thing You want to update 'name' or 'age' or 'aim' :")
    
    if a=='name':
        b=str(input())
    cursor.execute("update courses set name=?,ects=? where number=?",('MAX','99','2327'))
# cursor.execute("SELECT * FROM courses;")
# print(cursor.fetchall())
#Insertdata()
delete()