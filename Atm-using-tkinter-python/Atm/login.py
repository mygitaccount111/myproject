from tkinter import *
from tkinter import messagebox
import sqlite3

def login_response():
    try:
        con = sqlite3.connect('userdata.db')
        c = con.cursor()
        for row in c.execute("Select * from record"):
            username = row[0]
            pwd = row[5]
        
    except Exception as ep:
        messagebox.showerror('', ep)

    uname = email_tf.get()
    upwd = pwd_tf.get()
    check_counter=0
    if uname == "":
       warn = "Username can't be empty"
    else:
        check_counter += 1
    if upwd == "":
        warn = "Password can't be empty"
    else:
        check_counter += 1
    if check_counter == 2:
        if (uname == username and upwd == pwd):
            messagebox.showinfo('Login Status', 'Logged in Successfully!')
            import menu
        else:
            messagebox.showerror('Login Status', 'invalid username or password')
    else:
        messagebox.showerror('', warn)
ws = Tk()
ws.title('ATM MACHINE')
ws.config(bg='#0B5A81')

f = ('Times', 14)
center_frame = Frame(
    ws, 
    bd=2, 
    bg='#CCCCCC',   
    relief=SOLID, 
    padx=50, 
    pady=50
    )

Label(
    center_frame, 
    text="Enter username", 
    bg='#CCCCCC',
    font=f).grid(row=0, column=0, sticky=W, pady=10)

Label(
    center_frame, 
    text="Enter Password", 
    bg='#CCCCCC',
    font=f
    ).grid(row=1, column=0, pady=10)

email_tf = Entry(
   center_frame, 
    font=f
    )
pwd_tf = Entry(
    center_frame, 
    font=f,
    show='*'
    )
login_btn = Button(
   center_frame, 
    width=15, 
    text='Login', 
    font=f, 
    relief=SOLID,
    cursor='hand2',
    command=login_response
    )

email_tf.grid(row=0, column=1, pady=10, padx=20)
pwd_tf.grid(row=1, column=1, pady=10, padx=20)
login_btn.grid(row=2, column=1, pady=10, padx=20)
center_frame.place(x=450, y=50)

ws.mainloop()