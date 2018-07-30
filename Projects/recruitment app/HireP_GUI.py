from tkinter import *
from tkinter import messagebox
from hire_DB import *


def logi():
    if logiDB(E2.get(),E3.get(),E4.get(),E5.get(),E6.get()):
        L11['text']='Hired'
    else:
        L11['text']='Not Hired'

def deci():
    if deciDB(E2.get(),E3.get(),E4.get(),E5.get(),E6.get()):
        L12['text']='Hired'
    else:
        L12['text']='Not Hired'
    

def rafo():
    if rafoDB(E2.get(),E3.get(),E4.get(),E5.get(),E6.get()):
        L13['text']='Hired'
    else:
        L13['text']='Not Hired'
        

def svm():
    if svmDB(E2.get(),E3.get(),E4.get(),E5.get(),E6.get()):
        L14['text']='Hired'
    else:
        L14['text']='Not Hired'

        
def final():
    n=0
    l=[L11['text'],L12['text'],L13['text'],L14['text']]
    for i in l:
        if i=='Hired':
            n+=1
        else:
            n-=1
    if E1.get()=='' or (E2.get()==0 and E3.get()==0 or E4.get()==0 or E5.get()==0 or E6.get()==0):
        messagebox.showinfo('error!','Data Empty!!')
        return
    if n>=0:
        messagebox.showinfo('yaaay!','Hired!')
        finalDB(E1.get(),E2.get(),E3.get(),E4.get(),E5.get(),E6.get(),1)
    else:
        messagebox.showinfo('naaa!','Not Hired!')
        finalDB(E1.get(),E2.get(),E3.get(),E4.get(),E5.get(),E6.get(),0)
    
    

root=Tk()
root.config(background='#92857c')
root.geometry('700x660')

Label(root,text='Hire Predictor',bg='#92857c',fg='#fff',borderwidth='2',relief='ridge',font=('',30)).grid(row=0,column=0,columnspan=5,pady=10,ipadx=60)

l1=Label(root,text='Name : ',bg='#92857c',fg='#fff',font=('',15)).grid(row=1,pady=15,sticky=E)
l2=Label(root,text='Percentage : ',bg='#92857c',fg='#fff',font=('',15)).grid(row=2,pady=15,sticky=E)
l3=Label(root,text='Backlogs : ',bg='#92857c',fg='#fff',font=('',15)).grid(row=3,pady=15,sticky=E)
l4=Label(root,text='Internship : ',bg='#92857c',fg='#fff',font=('',15)).grid(row=4,pady=15,sticky=E)
l5=Label(root,text='FirstRound : ',bg='#92857c',fg='#fff',font=('',15)).grid(row=5,pady=15,sticky=E)
l5=Label(root,text='Communication : ',bg='#92857c',fg='#fff',font=('',15)).grid(row=6,pady=15,sticky=E)

E1,E2,E3,E4,E5,E6=StringVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar()

e1=Entry(root,font=('',13),textvariable=E1).grid(row=1,column=1,padx=20)
e2=Entry(root,font=('',13),textvariable=E2).grid(row=2,column=1)
e3=Entry(root,font=('',13),textvariable=E3).grid(row=3,column=1)
e4=Entry(root,font=('',13),textvariable=E4).grid(row=4,column=1)
e5=Entry(root,font=('',13),textvariable=E5).grid(row=5,column=1)
e6=Entry(root,font=('',13),textvariable=E6).grid(row=6,column=1)

Label(root,bg='#92857c',width=15).grid(row=0,rowspan=4,column=2,columnspan=2)

b1=Button(root,text='Logistic',width=13,command=logi,font=('',13),bg='#928584',fg='#fff').grid(row=2,column=4,ipadx=5,ipady=4)
b2=Button(root,text='Decision Tree',width=13,command=deci,font=('',13),bg='#928584',fg='#fff').grid(row=3,column=4,ipadx=5,ipady=4)
b3=Button(root,text='Random Forest',width=13,command=rafo,font=('',13),bg='#928584',fg='#fff').grid(row=4,column=4,ipadx=5,ipady=4)
b4=Button(root,text='SVM',width=13,command=svm,font=('',13),bg='#928584',fg='#fff').grid(row=5,column=4,ipadx=5,ipady=4)


L1=Label(root,text='Logistic Result',font=('',12),bg='#92857c',borderwidth=2,relief='solid').grid(row=7,column=0,pady=10,ipadx=5)
L2=Label(root,text='Decision Tree Result',font=('',12),bg='#92857c',borderwidth=2,relief='solid').grid(row=7,column=1,ipadx=5)
L3=Label(root,text='Random Forest Result',font=('',12),bg='#92857c',borderwidth=2,relief='solid').grid(row=7,column=2,ipadx=5)
L4=Label(root,text='SVM Result',font=('',12),bg='#92857c',borderwidth=2,relief='solid').grid(row=7,column=4,ipadx=5)

L11=Label(root,font=('',12),height=3,width=13,bg='#fff',borderwidth=2,relief='solid')
L11.grid(row=8,column=0)
L12=Label(root,font=('',12),height=3,width=13,bg='#fff',borderwidth=2,relief='solid')
L12.grid(row=8,column=1)
L13=Label(root,font=('',12),height=3,width=13,bg='#fff',borderwidth=2,relief='solid')
L13.grid(row=8,column=2)
L14=Label(root,font=('',12),height=3,width=11,bg='#fff',borderwidth=2,relief='solid')
L14.grid(row=8,column=4)

BF=Button(root,text='Final Result',width=25,font=('',15),bg='#928584',fg='#fff',command=final).grid(row=9,column=0,columnspan=5,ipady=5,pady=20)

root.mainloop()