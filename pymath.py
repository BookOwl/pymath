#!python3
# Import tkinter and tix
from tkinter import *
from tkinter import tix
# Use ttk
from tkinter.ttk import *
# Import custom widgets
from widgets.factorWidget import FactorWidget
from widgets.welcomeWidget import WelcomeWidget
from widgets.simpWidget import SimpWidget
from widgets.eqsolve import EqSolveWidget
from widgets.plotWidget import PlotWidget

class PyCAS(Frame):
    def __init__(self, *args, **kargs):
        Frame.__init__(self, *args, **kargs)
        self.__makeWidgets()
    def __makeWidgets(self):
        # Using tix.NoteBook (looks ugly.)
        # self.nb = tix.NoteBook(self, name='nb', ipadx=6, ipady=6)
        # self.nb.pack(expand=YES, fill=BOTH, padx=5, pady=5)
        # self.nb.add("welcome", label="Home")
        # self.nb.add("factor", label="Factoring", underline=0)
        # self.nb.add("simp", label="Simplification", underline=0)
        # w = WelcomeWidget(self.nb.welcome)
        # w.pack(side=LEFT, padx=2, pady=2, fill=BOTH, expand=YES)
        # f = FactorWidget(self.nb.factor)
        # f.pack(side=LEFT, padx=2, pady=2, fill=BOTH, expand=YES)
        # s = SimpWidget(self.nb.simp)
        # s.pack(side=LEFT, padx=2, pady=2, fill=BOTH, expand=YES)

        # Using ttk.Notebook (simpler and looks better.)
        self.nb = Notebook(self)
        w = WelcomeWidget()
        f = FactorWidget()
        s = SimpWidget()
        e = EqSolveWidget()
        p = PlotWidget()
        self.nb.add(w, text="Welcome", underline=0)
        self.nb.add(f, text="Factoring", underline=0)
        self.nb.add(s, text="Simplifying", underline=0)
        self.nb.add(e, text="Single Equation Solving", underline=7)
        self.nb.add(p, text="Plotting", underline=0)
        self.nb.enable_traversal()
        self.nb.pack(expand=YES, fill=BOTH, padx=5, pady=5)

def main():
    root = Tk()
    root.tk.eval('package require Tix') # Without this, tix fails horribly.
    root.title("PyMath 0.1")
    PyCAS(root).pack(fill=BOTH, expand=YES)
    root.mainloop()

if __name__ == '__main__':
    main()
