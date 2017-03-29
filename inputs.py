#!/usr/bin/python
# encoding: utf-8
# File Name: inputs.py

from Tkinter import *


def printlabel(event):
    print inx.getlabel()


class Inputs(Frame):
    def __init__(self, label='', parent=None):
        Frame.__init__(self, parent)
        self.pack()
        Label(self, text=label, font=('Roman', 16), width=16, padx=5).pack(side=LEFT)
        self.en = Entry(self, font=('Roman', 16), show='x')
        self.en.pack(padx=5)

    def getlabel(self):
        return self.en.get()

if __name__ == '__main__':
    root = Tk()
    root.bind('<Return>', printlabel)
    inx = Inputs('In1')
    inx.mainloop()
