"""Times Table Task"""
from tkinter import *
import random

class gui:
    def __init__(self, parent):
        data.gen()
        gui.entry1 = Entry (parent,width=20)
        gui.entry1.grid(row=1,column=2) 
        Button(parent,text="check", command=data.check).grid(row=2,column=1)
        Button(parent,text="next",command=data.next).grid(row=2,column=2)
        gui.answer=Label(parent, text = "")
        gui.answer.grid(row=3, columnspan=2,column=1)
        gui.question=Label(parent,text= "What is "+ str(data.rand1)+"*"+str(data.rand2)+" =")
        gui.question.grid(row=1,column=1)

class data():
    def gen():
        data.rand1=random.randint(1, 10)
        data.rand2=random.randint(1, 10)
        data.ans=data.rand1 * data.rand2

    def check():
        if int(gui.entry1.get()) == data.ans :
            gui.answer.configure(text="Correct")
        else:
            gui.answer.configure(text="Incorrect")
    def next():
        data.gen()
        gui.question.configure(text= "What is "+ str(data.rand1)+" * "+str(data.rand2)+" =")
        gui.answer.configure( text = "")
        gui.entry1.delete(0, END)



   
root = Tk()
gui(root)
root.mainloop()