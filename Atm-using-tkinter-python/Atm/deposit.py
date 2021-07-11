from tkinter import *
from tkinter import messagebox
import sqlite3


root=Tk()

root.geometry('350x400')
root.config(bg='#CCCCCC')

code = Label(root,bg='#CCCCCC', text = "IFSC code",font=('Helvetica', 18, 'bold')).place(x = 350, y = 140) 
text=Entry(root,width=40,bd=1)
text.pack()
text.place(x=600,y=140, height=35)

name = Label(root,bg='#CCCCCC', text = "AccountHolderName",font=('Helvetica', 18, 'bold')).place(x = 350, y =15) 
text=Entry(root,width=40,bd=1)
text.pack()
text.place(x=600,y=10, height=35)

number = Label(root,bg='#CCCCCC', text = "AccountNumber",font=('Helvetica', 18, 'bold')).place(x = 350, y =70) 
text=Entry(root,width=40,bd=1)
text.pack()
text.place(x=600,y=70, height=35)

amount = Label(root,bg='#CCCCCC', text = "Enteramount",font=('Helvetica', 18, 'bold')).place(x = 350, y =210) 
text=Entry(root,width=40,bd=1)
text.pack()
text.place(x=600,y=210, height=35)


def display_number(text, number):
    text.insert(END, number)
def delete():
    text.delete(0,'end')
def amount():
    messagebox.showinfo('confirmation', 'Amount has been Credited')
    root.quit()
b1=Button(root,text='1', bg="skyblue",command=lambda: display_number(text, 1))
b1.pack()
b1.place(x=500,y=260)
b1.config(width=10,height=5)

b2=Button(root,text='2',bg="skyblue",command=lambda: display_number(text, 2))
b2.pack()
b2.place(x=600,y=260)
b2.config(width=10,height=5)

b3=Button(root,text='3',bg="skyblue",command=lambda: display_number(text, 3))
b3.pack()
b3.place(x=700,y=260)
b3.config(width=10,height=5)

b4=Button(root,text='4',bg="skyblue",command=lambda: display_number(text, 4))
b4.pack()
b4.place(x=500,y=360)
b4.config(width=10,height=5)

b5=Button(root,text='5',bg="skyblue",command=lambda: display_number(text, 5))
b5.pack()
b5.place(x=600,y=360)
b5.config(width=10,height=5)

b6=Button(root,text='6',bg="skyblue",command=lambda: display_number(text, 6))
b6.pack()
b6.place(x=700,y=360)
b6.config(width=10,height=5)

b7=Button(root,text='7',bg="skyblue",command=lambda: display_number(text, 7))
b7.pack()
b7.place(x=500,y=460)
b7.config(width=10,height=5)

b8=Button(root,text='8',bg="skyblue",command=lambda: display_number(text, 8))
b8.pack()
b8.place(x=600,y=460)
b8.config(width=10,height=5)

b9=Button(root,text='9',bg="skyblue",command=lambda: display_number(text, 9))
b9.pack()
b9.place(x=700,y=460)
b9.config(width=10,height=5)

b10=Button(root,text='0',bg="skyblue",command=lambda: display_number(text, 0))
b10.pack()
b10.place(x=600,y=560)
b10.config(width=10,height=5)

b11=Button(root,text='CLear',command=delete)
b11.pack()
b11.place(x=500,y=560)
b11.config(width=10,height=5)

b12=Button(root,text='Submit',command=amount)
b12.pack()
b12.place(x=700,y=560)
b12.config(width=10,height=5)


root.mainloop()