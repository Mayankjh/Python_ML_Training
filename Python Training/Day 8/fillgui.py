from tkinter import *

root = Tk()

one = Label(root,text="One",bg="red",fg="white")
one.pack()
two = Label(root,text="two",bg="green",fg="black")
two.pack(fill=X)# fill= x makes widget as wide as parent
three = Label(root,text="Three",bg="blue",fg="white")
three.pack(side=LEFT,fill=Y)# fill= x makes widget as wide as parent
root.mainloop()

