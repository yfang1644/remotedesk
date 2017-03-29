#!/usr/bin/python
# File Name: server.py

from socket import *                    # get socket constructor and constants
from threading import Thread, Lock


def handleClient(connection, userdb):     # in spawned thread: reply
    mutex.acquire()
    while 1:
        data = connection.recv(1024)
        if not data:
            break
        list = data.split(':')
        user = list[0]
        passwd = list[1]

        item = userdb.get(user)
        if item:
            if item['passwd'] == passwd:
                finduser = item['host']
            else:
                finduser = 'ROOT'
        else:
            finduser = 'root'
        connection.send(finduser)
        connection.close()
        print 'connects closed'
        break

    mutex.release()


def loadusers(shadowfile):
    rf = open(shadowfile, 'r')
    content = rf.readlines()
    rf.close()
    db = {}
    for line in content:
        list = line.split(':')
        db[list[0]] = {'passwd': list[1], 'host': list[2].strip('\n')}
    return db


if __name__ == '__main__':
    userdb = loadusers('/home/dlna/netcomputer/passwd')

    sockobj = socket(AF_INET, SOCK_STREAM)    # make a TCP socket object
    sockobj.bind(('', 54321))                 # bind it to server port number
    sockobj.listen(5)                         # listen, allow 5 pending connects

    mutex = Lock()
    while 1:                                      # wait for next connection,
        connection, address = sockobj.accept()    # pass to thread for service
        print 'Server connected by', address,
        Thread(target=handleClient, args=(connection, userdb)).start()
