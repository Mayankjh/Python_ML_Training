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
    print(" 1) Insert : 1\n 2) Update: 2\n 3) Delete :3\n 4) Search: 4\n 5) View: 5")
    a = int(input("Enter Your Choice :"))
    if a==1:
        Insertdata()
    elif a==2:
        update()
    elif a==3:
        search()
    elif a==4:
        show_all()
    else:
        print('Enter your choice wisely No such option present')
    

# inserstion through variable

#courses = ("02345","NonLinear Signal IDk",12)
#cursor.execute("INSERT INTO courses values(?,?,?);",filedata)
def Insertdata():
    name= str(input("Enter Your Name:-"))
    age= int(input("Enter Your age:-"))
    aim= str(input("Enter Your aim:-"))
    cursor.execute("INSERT INTO filedata values(NULL,?,?,?);",(name,age,aim))
    conn.commit()
    print("inserted successfully...")
    conn.close()
    
def delete():
    show_all()
    nam=str(input("Enter the name of the person whose data is to deleted : "))
    cursor.execute("DELETE FROM filedata where name=?",(nam,))
    conn.commit()
    cursor.execute("SELECT * FROM filedata;")
    print(cursor.fetchall())
    conn.close()
    
def update():
    show_all()
    a = input("Enter the thing You want to update 'name' or 'age' or 'aim' :")
    
    if a=='name':
        prev = str(input("Enter Prev Name:"))
        new=str(input("Enter new Name:"))
        cursor.execute("update filedata set name=? where name=?",(new,prev))
        conn.commit()
        show_all()
        conn.close()
    elif a=='age':
        n = str(input("Enter Name:"))
        new=int(input("Enter new age:"))
        i=str(input("Enter ID:"))
        cursor.execute("update filedata set age=? where name=? and id=?",(new,n,i))
        conn.commit()
        show_all()
        conn.close()
    elif a=='aim':
        n = str(input("Enter Name:"))
        new=str(input("Enter new Aim:"))
        i=str(input("Enter ID:"))
        cursor.execute("update filedata set age=? where name=? and id=?",(new,n,i))
        conn.commit()
        show_all()
        conn.close()
    else:
        print("Wrong Input")

def show_all():
      cursor.execute("SELECT * FROM filedata;")
      print(cursor.fetchall())

def search():
    a = input("Search BY 'name' or 'age' or 'aim' or 'id' :")
    
    if a=='name':
        search=str(input("Enter the name to search:"))
        cursor.execute("Select * from filedata where name=?",(search,))
        rows = cursor.fetchall()
        print(rows)
        
    elif a=='age':
        search=int(input("Enter the age to search:"))
        cursor.execute("Select * from filedata where age=?",(search,))
        rows = cursor.fetchall()
        print(rows)
        
    elif a=='aim':
        search=str(input("Enter the aim to search:"))
        cursor.execute("Select * from filedata where aim=?",(search,))
        rows = cursor.fetchall()
        print(rows)
    elif a=='id':
        search=str(input("Enter the id to search:"))
        cursor.execute("Select * from filedata where id=?",(search,))
        rows = cursor.fetchall()
        print(rows)
        
    else:
        print("Wrong Input")
    
# cursor.execute("SELECT * FROM courses;")
# print(cursor.fetchall())
#Insertdata()
#show_all()
#update()
#delete()
#search()
InitiateProcess()