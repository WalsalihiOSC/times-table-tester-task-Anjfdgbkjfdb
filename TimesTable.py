"""Times Table Task"""

from tkinter import *
import random


class TimesTable:
    def __init__(self, parent):

        self.rand1=random.randint(1, 10)
        self.rand2=random.randint(1, 10)
        self.ans=self.rand1 * self.rand2

        canvas1 = Canvas(parent)
        canvas1.grid()
        self.entry1 = Entry (parent) 
        canvas1.create_window(300,50,window=self.entry1)
        checkbtn=Button(parent,text="check", command=self.check)
        checkbtn.grid()
        next=Button(parent,text="next",command=self.next)
        next.grid()
        self.text=Label(parent, text = "")
        self.text.grid()
        self.question=Label(parent,text= self.rand1)
        self.question.grid()
        self.question1=Label(parent,text= self.rand2)
        self.question1.grid()

    def next(self):
        self.rand1=random.randint(1, 10)
        self.rand2=random.randint(1, 10)
        self.ans=self.rand1 * self.rand2
        self.question.configure(text=self.rand1)
        self.question1.configure(text=self.rand2)

    def check(self):
        if int(self.entry1.get()) == self.ans :
            self.text.configure(text="Correct")
            self.text.grid()
        else:
            self.text.configure(text="Incorrect")
            self.text.grid()


root = Tk()
TimesTable(root)
root.mainloop()