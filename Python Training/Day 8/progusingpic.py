import tkinter as tk

root = tk.Tk()

logo = tk.PhotoImage(file="logo.png")
w1 = tk.Label(root,image=logo).pack(side="right")
explain = """Kya aap Online hotel dhund rhe hai,
come to trivago, Trivago does the same work for you instantly comparing
diff websites to get you the best deal
HOTEL, TRIVAGO"""
 
w2 = tk.Label(root,justify=tk.LEFT,padx=10,text=explain).pack(side="left")
root.mainloop() 