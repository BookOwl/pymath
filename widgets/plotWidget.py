#! python3

from tkinter.tix import *
from tkinter.constants import *
from tkinter import *
from tkinter.messagebox import *
from tkinter.ttk import *

import sympy

class LabledEntry(Frame):
    def __init__(self, *args, text="", **kargs):
        print(kargs)
        Frame.__init__(self, *args, **kargs)
        self.__txt = text
        self.__makeWidgets()
    def __makeWidgets(self):
        Label(self, text=self.__txt).pack(side=LEFT)
        self.__ent = Entry(self)
        self.__ent.pack(fill=X)
    def get(self):
        return self.__ent.get()
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
        self.xminvar = IntVar()
        self.xminvar.set(-10)
        self.xmin = Control(self, label="X Axis Min: ", variable=self.xminvar, pady=5)
        self.xmaxvar = IntVar()
        self.xmaxvar.set(10)
        self.xmax = Control(self, label="X Axis Max: ", variable=self.xmaxvar, pady=5)
        self.yminvar = IntVar()
        self.yminvar.set(-10)
        self.ymin = Control(self, label="Y Axis Min: ", variable=self.yminvar, pady=5)
        self.ymaxvar = IntVar()
        self.ymaxvar.set(10)
        self.ymax = Control(self, label="Y Axis Max: ", variable=self.ymaxvar, pady=5)
        for w in ("xmin", "xmax", "ymin", "ymax"):
            eval("self." + w).pack(anchor=E)
        Button(self, text="Plot", command=self.plot).pack(anchor=E)
    def plot(self):
        try:
            expr = sympy.sympify(self.ent.get())
            sympy.plotting.plot(expr,
                                xlim=(self.xminvar.get(), self.xmaxvar.get()),
                                ylim=(self.yminvar.get(), self.ymaxvar.get()),
                                legend=True)
        except Exception as e:
            showerror("ERROR!", str(e))

if __name__ == '__main__':
    root = Tk()
    root.tk.eval('package require Tix')
    #LabledEntry(root, text="Spam? ").pack()
    PlotWidget(root).pack()
    root.mainloop()
