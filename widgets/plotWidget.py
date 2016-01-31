#! python3

from tkinter import tix
from tkinter.constants import *
from tkinter import *
from tkinter.ttk import *

import sympy

class PlotWidget(Frame):
    def __init__(self, *args, **kargs):
        Frame.__init__(self, *args, **kargs)
        self.__makeWidgets()
    def __makeWidgets(self):
        Label(self, text="Plotting\n", justify="center").pack()
        row = Frame(self)
        lab = Label(row, text="Enter your expression.   ")
        self.ent = Entry(row)
        row.pack(fill=X)
        self.ent.pack(side=RIGHT,  expand=YES, fill=X)
        lab.pack(side=LEFT)
        Button(self, text="Plot", command=self.plot).pack(anchor=E)
    def plot(self):
        expr = sympy.sympify(self.ent.get())
        sympy.plotting.plot(expr)

if __name__ == '__main__':
    root = Tk()
    PlotWidget(root).pack(expand=YES, fill=BOTH)
    root.mainloop()
