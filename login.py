#!/usr/bin/python
# encoding:utf-8
# FileName: login.py


import os
import sys
from Tkinter import *
from resetPassword import *
from makeform import *
from client import *


def fetch(event):
    x = ents.getlabels()
    user = x[0].get()
    pw = x[1].get()
    str = user + ':' + pw
    print str
    req = Client(userhost, 54321)
    req.send(str)
    str = req.receive(1024)
    req.close()
    if str == 'root':
        head.config(text='该用户不存在\n ')
    elif str == 'ROOT':
        head.config(text='口令错误\n ')
    else:
        head.config(text='Login as %@%s' % (user, str))
        remote = 'rdesktop %s -u%s -p%s -xlan' % (str, user, pw)
        os.system(remote)


def resetpassword():
    head.config(text='口令重置')
    win = Toplevel()
    win.title("Reset Password")
    win.protocol('WM_DELETE_WINDOW', win.quit)
    r = ResetPassword(win)
    r.pack()
    win.focus_set()          # take over input focus,
    win.grab_set()           # disable other windows while I'm open,
    win.mainloop()        # and wait here until win destroyed
    passwd = r.getinfo()
    print passwd
    win.destroy()
    if passwd[1] != passwd[2]:
        head.config(text='repeated password\n differs')


if __name__ == '__main__':
    root = Tk()
    root.title('Login Windows')
    head = Label(root, text='电子实验中心', font=('AR PL UMing CN', 20, 'normal'))
    head.pack(side=TOP, padx=10, pady=10)
    Label(root, text='Blue Genie 云桌面', font=('AR PL UKai CN', 20, 'normal')).pack(
        side=TOP)
    ents = MakeForm(root)
    root.bind('<Return>', fetch)
    Button(root, text='重置口令', command=resetpassword).pack(side=TOP, pady=10)

    if len(sys.argv) == 2:
        userhost = sys.argv[1]
    else:
        userhost = '192.168.200.47'
    root.mainloop()
