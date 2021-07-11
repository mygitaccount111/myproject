from tkinter import *		
root = Tk()
root.geometry('300x250')
root.configure(bg ="dodger blue")
def Page1():
    root.quit()
    import withdraw
def Page2():
    root.quit()
    import deposit
def Page3():
    root.quit()
    import feedback
def Page4():
    root.quit()
    import review
withdrawlbutton = Button(root,text = "WITHDRAW",cursor="hand2",fg = "white",bg = "darkblue",height = 4, width =20,command=Page1)
withdrawlbutton.place(x=500, y=300)
depositbutton = Button( root,text = "DEPOSIT",cursor="hand2",fg = "white",bg = "darkblue",height = 4 , width = 20,command=Page2)
depositbutton.place(x=750, y=300)
feedbackbutton = Button(root,text = "FEEDBACK",cursor="hand2",fg = "white",bg = "darkblue",height = 4, width =20,command=Page3)
feedbackbutton.place(x=500, y=400)
reviewbutton = Button( root,text = "REVIEW",cursor="hand2",fg = "white",bg = "darkblue",height = 4 , width = 20,command=Page4)
reviewbutton.place(x=750, y=400)
root.mainloop()
