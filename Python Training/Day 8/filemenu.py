from tkinter import *

def doNothing():
    print("ok ok I won't")

root= Tk()

menu = Menu(root)
root.config(menu=menu)

submenu = Menu(menu)
menu.add_cascade(label="File",menu=submenu)
submenu.add_command(label="New Project",command=doNothing)
submenu.add_command(label="New...",command=doNothing)
submenu.add_separator()
submenu.add_command(label="Exit",command=doNothing)

editMenu = Menu(menu)
menu.add_cascade(label="Edit",menu=editMenu)
submenu.add_command(label="Redo",command=doNothing)
root.mainloop()
