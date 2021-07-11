from tkinter import *		
root = Tk()
root.geometry('300x250')
root.configure(bg ="dodger blue")
label = Label( text = "ATM", font = ('Helvetica', 18, 'bold'))
label.pack(side=TOP,anchor=NW)
def Page1():
    root.quit()
    import login
def Page2():
    root.quit()
    import register
loginbutton = Button(root,text = "LOGIN",cursor="hand2",fg = "white",bg = "darkblue",height = 4, width =20,command=Page1)
loginbutton.place(x=500, y=300)
registerbutton = Button( root,text = "REGISTER",cursor="hand2",fg = "white",bg = "darkblue",height = 4 , width = 20,command=Page2)
registerbutton.place(x=750, y=300)
root.mainloop()