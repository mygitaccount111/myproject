from tkinter import *
from tkinter import messagebox
import sqlite3

f = ('Times', 14)

con = sqlite3.connect('feedback.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS record(
                    bname text,
                    brname text, 
                    baname text, 
                    feedback text
                )
            ''')
con.commit()

ws = Tk()
ws.title('Feedback')
ws.geometry('700x500')
ws.config(bg='#0B5A81')

def feedback_record():
    check_counter=0
    warn = ""
    if register_bname.get() == "":
       warn = "Bankname can't be empty"
    else:
        check_counter += 1
    if register_brname.get() == "":
       warn = "Branchplace can't be empty"
    else:
        check_counter +=1 
    if register_baname.get() == "":
        warn = "Bankaccountname can't be empty"
    else:
        check_counter += 1
    if  var.get() == "":
        warn = "Select Account Type"
    else:
        check_counter += 1
    if register_feedback.get() == "":
       warn = "Feedback can't be empty"
    else:
        check_counter +=1
    if check_counter >=4 :        
        try:
            con = sqlite3.connect('feedback.db')
            cur = con.cursor()
            cur.execute("INSERT INTO record VALUES (:bname, :brplace, :baname, :feedback)", {
                            'bname': register_bname.get(),
                            'brplace': register_brname.get(),
                            'baname': register_baname.get(),
                            'feedback': register_feedback.get(),

            })
            con.commit()
            messagebox.showinfo('confirmation', 'Thanks for the feedback ')
            ws.quit()
        except Exception as ep:
            messagebox.showerror('', ep) 
    else:
        messagebox.showerror('Error', warn)

var = StringVar()
var.set('savings')

frame = Frame(
    ws, 
    bd=2,   
    relief=SOLID, 
    padx=10, 
    pady=10
    )

Label(frame ,text = "Bank Name",font=f).grid(row = 0,column = 0)
Label(frame ,text = "Branch Place",font=f).grid(row = 1,column = 0)
Label(frame ,text = "Branch Account Name", font=f).grid(row = 2,column = 0)
Label(frame ,text = "Account type", font=f).grid(row = 3,column = 0)
Label(frame ,text = " feedback",font=f).grid(row = 4,column = 0)

comment_frame = LabelFrame(
    frame,
    padx=10, 
    pady=10,
    )
register_bname = Entry(
    frame, 
    font=f
    )
register_brname = Entry(
    frame, 
    font=f
    )
register_baname = Entry(
    frame, 
    font=f
    )

savings= Radiobutton(
    comment_frame, 
    text='savings',
    variable=var,
    value='savings',
    font=('Times', 10)
)
current= Radiobutton(
    comment_frame, 
    text='current',
    variable=var,
    value='current',
    font=('Times', 10)
)
others = Radiobutton(
    comment_frame, 
    text='others',
    variable=var,
    value='others',
    font=('Times', 10)
)
register_feedback = Entry(
     frame, 
    font=f
    )
register_btn = Button(
    frame, 
    text='Send', 
    font=f, 
    relief=SOLID,
    cursor='hand2',
    command=feedback_record
)

register_bname.grid(row=0, column=1, pady=10, padx=20)
register_brname.grid(row=1, column=1, pady=10, padx=20)
register_baname.grid(row=2, column=1, pady=10, padx=20)
register_feedback.grid(row=4, column=1, pady=10, padx=20,ipadx=20,ipady=30)
register_btn.grid(row=7, column=1, pady=10, padx=20)
frame.place(x=450, y=50)
comment_frame.grid(row=3, column=1, pady=10, padx=20)
savings.pack(expand=True, side=LEFT)
current.pack(expand=True, side=LEFT)
others.pack(expand=True, side=LEFT)
ws.mainloop()
