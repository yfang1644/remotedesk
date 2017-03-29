#!/usr/bin/python
# encoding: utf-8
# File Name: makeform.py
# Author: Fang Yuan
# Mail: yfang@nju.edu.cn
# Created Time: Mon 30 May 2016 01:06:20 PM CST

from Tkinter import *


class MakeForm(Frame):
    def __init__(self, parent=None):
        self.vars = []
        list = ('用户名', '口令')
        Frame.__init__(self, parent)
        self.pack()
        fontsel = ('Courier', 20, 'bold')
        for e in list:
            row = Frame(self)
            lab = Label(row, font=fontsel, width=10, text=e)
            if e == '口令':
                en = Entry(row, width=16, font=fontsel, show='*')
            else:
                en = Entry(row, width=16, font=fontsel)
            row.pack(side=TOP, fill=X)
            lab.pack(side=LEFT)
            en.pack(side=RIGHT, expand=YES, fill=X, padx=5, pady=5)
            self.vars.append(en)

    def getlabels(self):
        return self.vars


if __name__ == '__main__':
    MakeForm().mainloop()
