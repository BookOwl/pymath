#!python3
from tkinter import *
from tkinter.messagebox import *
from tkinter.ttk import *
import numpy

def mode(data):
    d = {}
    for n in data:
        if n not in d:
            d[n] = 0
        d[n] += 1
    max = (0, -1)
    for n in d:
        if d[n] > max[1]:
            max = (n, d[n])
    return max[0]

def range(data):
    return abs(max(data) - min(data))

class StatsWidget(Frame):
    def __init__(self, *args, **kargs):
        Frame.__init__(self, *args, **kargs)
        self.__makeWidgets()
    def __makeWidgets(self):
        Label(self, text="Statistics\n", justify="center").pack()
        row = Frame(self)
        lab = Label(row, text="Enter your data.  ")
        self.ent = Entry(row)
        row.pack(fill=X, anchor=NW)
        self.ent.pack(side=RIGHT,  expand=YES, fill=X)
        lab.pack(side=LEFT)
        self.b = Button(self, text="Calculate")
        self.b.pack(side=RIGHT, anchor=NE)
        self.b.config(command=self.calcStats)
        # Result labels
        f = Frame(self)
        self.mean = Label(f, text="Mean: ")
        self.median = Label(f, text="Median: ")
        self.mode = Label(f, text="Mode: ")
        self.range = Label(f, text="Range: ")
        self.stddev = Label(f, text="Std. Deviation: ")
        self.mean.pack(anchor=NW)
        self.median.pack(anchor=NW)
        self.mode.pack(anchor=NW)
        self.range.pack(anchor=NW)
        self.stddev.pack(anchor=NW)
        f.pack(side=LEFT, anchor=NW)
    def calcStats(self):
        try:
            d = self.ent.get()
            d = [float(n.strip()) for n in d.split(",")]
            mean = numpy.mean(d)
            m = mode(d)
            r = range(d)
            median = numpy.median(d)
            stdev = numpy.std(d)
            self.mean["text"] = "Mean: %s" % mean
            self.median["text"] = "Median: %s" % median
            self.mode["text"] = "Mode: %s" % m
            self.range["text"] = "Range: %s" % r
            self.stddev["text"] = "Std. Deviation: %s" % stdev
        except Exception as e:
            showerror("ERROR!", str(e))

if __name__ == '__main__':
    root = Tk()
    StatsWidget(root).pack(expand=YES, fill=BOTH)
    root.mainloop()
