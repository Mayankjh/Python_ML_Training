# python gui

fg : foreground color
bg : background color

# Import messagebox
usage : import tkinter.messagebox
root = Tk()

Label widget



from tkinter import *

root =Tk()
lb=Label(root,text='Hola Amigos')
lb.pack()
root.mainloop()



     Frame

root=Tk()
# frame is a rectangular area contain
topFrame = Frame(root)
topFrame.pack()

bottomFrame=Frame(root) 
bottomFrame.pack(side=BOTTOM)

button1=Button(topFrame,text='Button 1',fg='red')
button2=Button(topFrame,text='Button 2',fg='blue')
button3=Button(topFrame,text='Button 3',fg='green')
button4=Button(bottomFrame,text='Button 4',fg='purple')

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)

root.mainloop()

=> root.quit()


=> import tkinter.messagebox
     
