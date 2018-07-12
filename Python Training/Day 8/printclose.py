from tkinter import *

def Quit(event):
    root.destroy()
def Clickme(event):
    print("You just clicked me!!")
root = Tk()
b1 = Button(text="Print Messege", fg="green")
b2 = Button(text="Quit", fg="red")
b1.grid(row=0,column=0)
b2.grid(row=0,column=1)
b1.bind("<Button-1>",Clickme)
b2.bind("<Button-1>",Quit)
root.mainloop()
