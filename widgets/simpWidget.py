#!python3
from tkinter import *
from tkinter.ttk import *
import sympy

simptypes = {
    "Simplify": sympy.simplify,
    "Expand": sympy.expand,
    "Factor": sympy.factor,
    "Cancel": sympy.cancel,
    "Apart": sympy.apart,
}

class SimpSelect(Frame):
    def __init__(self, *args, **kargs):
        Frame.__init__(self, *args, **kargs)
        Label(self, text="Select simplification method.").pack(side=TOP)
        self.var = StringVar()
        for type in reversed(sorted(simptypes)):
            Radiobutton(self, text=type, value=type, variable=self.var).pack(anchor=NW)
        self.var.set("Simplify")
    def getType(self):
        return self.var.get()

class SimpWidget(Frame):
    def __init__(self, *args, **kargs):
        Frame. __init__(self, *args, **kargs)
        self.__makeWidgets()
    def __makeWidgets(self):
        Label(self, text="Expression simplification\n", justify="center").pack()
        row = Frame(self)
        lab = Label(row, text="Enter your expression.  ")
        self.ent = Entry(row)
        row.pack(side=LEFT, expand=YES, fill=X, anchor=N)
        self.ent.pack(side=RIGHT,  expand=YES, fill=X)
        lab.pack(side=LEFT)
        Button(self, text="Simplify", command=self.simplify).pack(fill=X)
        self.simpselect = SimpSelect(self)
        self.simpselect.pack()

    def simplify(self):
        type = self.simpselect.getType()
        meth = simptypes[type]
        expr = sympy.sympify(self.ent.get())
        res  = str(meth(expr))
        self.ent.delete(0, END)
        self.ent.insert(0, res)

if __name__ == '__main__':
    root = Tk()
    s = SimpWidget(root)
    s.pack(expand=YES, fill=BOTH)
    root.mainloop()
