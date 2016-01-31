#!python3

from tkinter import *
from tkinter.messagebox import *
from tkinter.ttk import *
from tkinter import Label

with open("./resources/abouthelp.txt") as f:
    helptxt = f.read()

class WelcomeWidget(Frame):
    def __init__(self, *args, **kargs):
        Frame.__init__(self, *args, **kargs)
        self.__makeWidgets()
    def __makeWidgets(self):
        Label(self, text="Welcome to PyMath 0.1!\n", justify="center").pack()
        Label(self, text="Use the tabs to navigate between PyMath's different functions.", justify="center").pack()
        l = Label(self, text="About/Help", fg="blue", padx=10, pady=10)
        l.pack(side=BOTTOM, anchor=SE)
        l.config(cursor="hand2")
        l.bind("<Button-1>", self.showabout)
    def showabout(self, e):
        showinfo("About PyMath 0.1", helptxt)

if __name__ == '__main__':
    WelcomeWidget().mainloop()
