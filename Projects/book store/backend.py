import sqlite3 as sq
 
    
conn=sq.connect('db')
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY autoincrement , title TEXT, 
                    author TEXT, year INTEGER, isbn INTEGER);""")
conn.commit()
        
def insert(title, author, year, isbn):
    cursor.execute("INSERT INTO book VALUES(NULL,?,?,?,?)", (title,author,year,isbn))
    conn.commit() 
        
def view():
    cursor.execute("SELECT * FROM book")
    rows = cursor.fetchall() 
        
    return rows
    
def search(title="", author="", year="", isbn=""):
    cursor.execute("SELECT * FROM book WHERE title = ? OR author = ? OR year = ? "
                    "OR isbn = ?", (title, author, year, isbn))
    rows = cursor.fetchall()
        #conn.close()
    return rows     
    
def delete(id):
    cursor.execute("DELETE FROM book WHERE id = ?", (id,))
    conn.commit()
    
def update(id, title, author, year, isbn):
    cursor.execute("UPDATE book SET title = ?, author = ?, year = ?, isbn = ? WHERE id = ?", (title, author, year, isbn, id))
    conn.commit()
        
def __del__():
    conn.close()
        
        
def prints():
    print('Database Connected...')           
    