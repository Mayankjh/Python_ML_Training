from tkinter import *

root = Tk()
#frame is a rectangular area that can contain other
topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame,text="Button 1",fg="red")
button2 = Button(topFrame,text="Button 2",fg="blue")
button3 = Button(topFrame,text="Button 3",fg="green")
button4 = Button(bottomFrame,text="Button 4",fg="purple")

# These button will be on top
button1.pack(side=LEFT) #place as far as possible
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)

root.mainloop()
