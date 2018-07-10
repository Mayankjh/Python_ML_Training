from tkinter import *

window = Tk()
def kmtom():
    print(e_value.get())
    miles = float(e_value.get())*1.6
    t.insert(END,miles)
    
b = Button(window,text='Calculate',background='pink',command=kmtom)
b.pack()
b.grid(row=0,column=0)

e_value=StringVar()

e = Entry(window,textvariable=e_value)
e.grid(row=0,column=1)
t=Text(window,height=1,width=20)
t.grid(row=0,column=2)
window.mainloop()