#!python3
from tkinter import *
from tkinter.ttk import *
import sympy

class FactorWidget(Frame):
    def __init__(self, *args, **kargs):
        Frame.__init__(self, *args, **kargs)
        self.__makeWidgets()

    def __makeWidgets(self):
        Label(self, text="Expression factoring\n", justify="center").pack()
        # Create entry
        row = Frame(self)
        lab = Label(row, text="Enter your expression.   ")
        self.ent = Entry(row)
        row.pack(fill=X)
        self.ent.pack(side=RIGHT,  expand=YES, fill=X)
        lab.pack(side=LEFT)
        # Create results Label
        self.res = Label(self, text="Result")
        self.res.pack()
        # Create button and bind return key
        Button(self, text="Factor", command = self.__factor).pack(anchor=SE)
        self.ent.bind("<Return>", (lambda e: self.__factor()))

    def __factor(self):
        print("Factoring..")
        expr = sympy.sympify(self.ent.get())
        fexpr = sympy.factor(expr)
        print(str(fexpr))
        self.res["text"] = "Your expression factors as %s" % str(fexpr)

if __name__ == '__main__':
    root = Tk()
    FactorWidget(root).pack(fill=BOTH, expand=YES)
    root.mainloop()
