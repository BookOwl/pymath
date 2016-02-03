#! python3

from tkinter import tix
from tkinter.constants import *
from tkinter import *
from tkinter.messagebox import *
from tkinter.ttk import *

import sympy

class EqWidget(Frame):
    def __init__(self, *args, **kargs):
        Frame.__init__(self, *args, **kargs)
        self.__makeWidgets()
    def __makeWidgets(self):
        self.e1 = Entry(self)
        self.e1.grid(row=0, column=0, sticky=EW)
        Label(self, text=" = ", justify="center").grid(row=0, column=1)
        self.e2 = Entry(self)
        self.e2.grid(row=0, column=2, sticky=EW)
        Label(self, text="What variable do you want to solve for?", justify="center").grid(columnspan=2, sticky=E)
        self.syment = Entry(self)
        self.syment.grid(row=1, column=2, sticky=W)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(2, weight=1)
    def getEq(self):
        try:
            exp1 = self.e1.get()
            exp1 = sympy.sympify(exp1)
            exp2 = self.e2.get()
            exp2 = sympy.sympify(exp2)
            sym = sympy.symbols(self.syment.get())
            return sympy.Eq(exp1, exp2), sym
        except Exception as e:
            showerror("ERROR!", str(e))

class EqSolveWidget(Frame):
    def __init__(self, *args, **kargs):
        Frame.__init__(self, *args, **kargs)
        self.__makeWidgets()
    def __makeWidgets(self):
        # Label(self, text="Single equation solving.\n", justify="center").grid(columnspan=2)
        # self.eq = EqWidget(self)
        # self.eq.grid(columnspan=2, sticky=EW)
        # Button(self, text="Solve", command=self.solve).grid(row=2, column=1, sticky=W)
        # self.res = Label(self, text="Solutions: ")
        # self.res.grid(row=2, column=0, sticky=W)
        # self.rowconfigure(1, weight=1)
        # self.columnconfigure(0, weight=1)
        # self.columnconfigure(2, weight=1)
        Label(self, text="Single equation solving.\n", justify="center").pack()
        self.eq = EqWidget(self)
        self.eq.pack(fill=X)
        Button(self, text="Solve", command=self.solve).pack(side=RIGHT, anchor=N)
        self.res = Label(self, text="Solutions: ")
        self.res.pack(side=LEFT, anchor=N)
    def solve(self):
        try:
            eq, var = self.eq.getEq()
            print(eq, var)
            sols = sympy.solve(eq, var)
            print(sols)
            sols = ['%s = %s' % (str(var), s) for s in sols]
            solstr = ", ".join(sols)
            if len(sols) == 0:
                solstr = "None"
            solstr = "Solutions: " + solstr
            print(solstr)
            self.res["text"] = solstr
        except Exception as e:
            showerror("ERROR!", str(e))

def testEqWidget():
    root = Tk()
    f = Frame(root)
    f.pack(expand=YES, fill=BOTH, padx=10, pady=10)
    eq = EqWidget(f)
    eq.pack(expand=YES, fill=BOTH)
    Button(f, text="Get Equation", command=(lambda : print(eq.getEq()))).pack()
    root.mainloop()
def testEQSolveWidget():
    root = Tk()
    f = Frame(root)
    f.pack(expand=YES, fill=BOTH)
    eq = EqSolveWidget(f)
    eq.pack(fill=BOTH, anchor=N)
    root.mainloop()
if __name__ == '__main__':
    #testEqWidget()
    testEQSolveWidget()
