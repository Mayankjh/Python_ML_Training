from tkinter import *

window = Tk()
window.title("Weight Converter")
def clear_entry(event):
     e.delete(0, END)
     
def weightconv():
    clearall()
    print(e_value.get())
    grams = str(float(e_value.get())*1000)
    gramsw= (grams +" grams")
    pounds = str(float(e_value.get())*2.20462)
    poundsw = (pounds + " pounds")
    ounces = str(float(e_value.get())*35.274)
    ouncesw = (ounces + " ounces")
    t.insert(END,gramsw)
    t1.insert(END,poundsw)
    t2.insert(END,ouncesw)
def clearall():
    t.delete(1.0,END)
    t1.delete(1.0,END)
    t2.delete(1.0,END)
# Calculate button    
b = Button(window,text='Calculate',background='pink',command=weightconv,width=20)
b.pack()
b.grid(row=0,column=0)

# clear Button
b1 = Button(window, text='Clear',background='pink', command=clearall,width=20 )
b1.grid(row=0,column=1)
#input text
e_value=StringVar()
e = Entry(window,textvariable=e_value,width=25)
e.insert(0, "Enter Value in KG") 
e.bind("<Button-1>", clear_entry) 
e.grid(row=0,column=2)

#grams
t=Text(window,height=1,width=25)
t.grid(row=1,column=0)

#pounds
t1=Text(window,height=1,width=25)
t1.grid(row=1,column=1)

#ounces
t2=Text(window,height=1,width=25)
t2.grid(row=1,column=2)

window.mainloop()