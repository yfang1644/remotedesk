#!/usr/bin/python
# encoding: utf-8
# File Name: ResetPassword.py

from Tkinter import *             # get base widget set
from inputs import Inputs


class ResetPassword(Frame):
    def __init__(self, parent=None):
        self.vars = []
        list = ('旧口令', '新口令', '重复新口令')
        Frame.__init__(self, parent)
        self.pack()
        Label(self, font=('Roman', 18), text='重置口令').pack()
        setfont = ('Roman', 16, 'normal')
        for e in list:
            passwd = Inputs(e, self)
            self.vars.append(passwd)
            passwd.pack()

        Button(self, text='确定', command=self.quit).pack()

    def getinfo(self):
        return (self.vars[0].getlabel(),
                self.vars[1].getlabel(),
                self.vars[2].getlabel())


if __name__ == '__main__':
    ResetPassword().mainloop()
