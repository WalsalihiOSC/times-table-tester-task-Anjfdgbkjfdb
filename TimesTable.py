"""Times Table Task"""

from tkinter import *

class TimesTable:
    def __init__(self, parent):

        Label(parent,text="4*5 = ").grid()
        canvas1 = Canvas(parent)
        canvas1.grid()
        self.entry1 = Entry (parent) 
        canvas1.create_window(300,0,window=self.entry1)
        checkbtn=Button(parent,text="check", command=self.check)
        checkbtn.grid()
        self.text=Label(parent, text = "")
        self.text.grid()

    def check(self):
        if self.entry1.get() == "20":
            self.text.configure(text="Correct")
            self.text.grid()
        else:
            self.text.configure(text="Incorrect")
            self.text.grid()


root = Tk()
TimesTable(root)
root.mainloop()