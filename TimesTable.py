"""Times Table Task"""
from tkinter import *
import random

class gui:
    def __init__(self, parent):
        data.gen()
        gui.entry1 = Entry (parent,width=20)
        gui.entry1.grid() 
        Button(parent,text="check", command=data.check).grid()
        Button(parent,text="next",command=data.next).grid()
        gui.answer=Label(parent, text = "")
        gui.answer.grid()
        gui.question=Label(parent,text= "What is "+ str(data.rand1)+"*"+str(data.rand2)+" =")
        gui.question.grid()

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



   
root = Tk()
gui(root)
root.mainloop()