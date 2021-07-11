from tkinter import *
from tkinter import messagebox
import sqlite3

f = ('Times', 14)

con = sqlite3.connect('review.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS record(
                    fname text,
                    lname text, 
                    email text, 
                    feedback text
                )
            ''')
con.commit()

ws = Tk()
ws.title('Review')
ws.geometry('700x500')
ws.config(bg='#0B5A81')

def review_record():
    check_counter=0
    warn = ""
    if register_fname.get() == "":
       warn = "FirstName can't be empty"
    else:
        check_counter += 1
    if register_lname.get() == "":
       warn = "LastName can't be empty"
    else:
        check_counter +=1 
    if register_email.get() == "":
        warn = "Email can't be empty"
    else:
        check_counter += 1
    if  var.get() == "":
        warn = "Select Review"
    else:
        check_counter += 1
    if register_feedback.get() == "":
       warn = "Feedback can't be empty"
    else:
        check_counter +=1
    if check_counter >=4 :        
        try:
            con = sqlite3.connect('review.db')
            cur = con.cursor()
            cur.execute("INSERT INTO record VALUES (:fname, :lname, :email, :feedback)", {
                            'fname': register_fname.get(),
                            'lname': register_lname.get(),
                            'email': register_email.get(),
                            'feedback': register_feedback.get(),

            })
            con.commit()
            messagebox.showinfo('confirmation', 'Thanks for the Review ')
            ws.quit()
        except Exception as ep:
            messagebox.showerror('', ep) 
    else:
        messagebox.showerror('Error', warn)

var = StringVar()
var.set('good')

frame = Frame(
    ws, 
    bd=2,   
    relief=SOLID, 
    padx=10, 
    pady=10
    )

Label(frame ,text = "First Name",font=f).grid(row = 0,column = 0)
Label(frame ,text = "Last Name",font=f).grid(row = 1,column = 0)
Label(frame ,text = "Email Id", font=f).grid(row = 2,column = 0)
Label(frame ,text = "Rating", font=f).grid(row = 3,column = 0)
Label(frame ,text = " feedback",font=f).grid(row = 4,column = 0)

comment_frame = LabelFrame(
    frame,
    padx=10, 
    pady=10,
    )
register_fname = Entry(
    frame, 
    font=f
    )
register_lname = Entry(
    frame, 
    font=f
    )
register_email = Entry(
    frame, 
    font=f
    )

good= Radiobutton(
    comment_frame, 
    text='Good',
    variable=var,
    value='good',
    font=('Times', 10)
)
worst = Radiobutton(
    comment_frame, 
    text='Worst',
    variable=var,
    value='worst',
    font=('Times', 10)
)
average = Radiobutton(
    comment_frame, 
    text='average',
    variable=var,
    value='average',
    font=('Times', 10)
)
register_feedback = Entry(
     frame, 
    font=f
    )
register_btn = Button(
    frame, 
    text='Submit', 
    font=f, 
    relief=SOLID,
    cursor='hand2',
    command=review_record
)

register_fname.grid(row=0, column=1, pady=10, padx=20)
register_lname.grid(row=1, column=1, pady=10, padx=20)
register_email.grid(row=2, column=1, pady=10, padx=20)
register_feedback.grid(row=4, column=1, pady=10, padx=20,ipadx=20,ipady=30)
register_btn.grid(row=7, column=1, pady=10, padx=20)
frame.place(x=450, y=50)
comment_frame.grid(row=3, column=1, pady=10, padx=20)
good.pack(expand=True, side=LEFT)
worst.pack(expand=True, side=LEFT)
average.pack(expand=True, side=LEFT)
ws.mainloop()
