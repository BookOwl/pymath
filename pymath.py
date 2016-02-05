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
from widgets.statsWidget import StatsWidget

class PyCAS(Frame):
    def __init__(self, *args, **kargs):
        Frame.__init__(self, *args, **kargs)
        self.__makeWidgets()
    def __makeWidgets(self):
        self.nb = Notebook(self)
        w = WelcomeWidget()
        f = FactorWidget()
        s = SimpWidget()
        e = EqSolveWidget()
        p = PlotWidget()
        st = StatsWidget()
        self.nb.add(w, text="Welcome", underline=0)
        self.nb.add(f, text="Factoring", underline=0)
        self.nb.add(s, text="Simplifying", underline=0)
        self.nb.add(e, text="Single Equation Solving", underline=7)
        self.nb.add(p, text="Plotting", underline=0)
        self.nb.add(st, text="Statistics", underline=1)
        self.nb.enable_traversal()
        self.nb.pack(expand=YES, fill=BOTH, padx=5, pady=5)

def main():
    root = Tk()
    root.tk.eval('package require Tix') # Without this, tix fails horribly.
    root.title("PyMath 0.3")
    PyCAS(root).pack(fill=BOTH, expand=YES)
    root.mainloop()

if __name__ == '__main__':
    main()
