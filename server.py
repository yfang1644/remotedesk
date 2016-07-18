#!/usr/bin/python
# File Name: server.py

from socket import *                    # get socket constructor and constants
from threading import Thread, Lock

def handleClient(connection):                    # in spawned thread: reply
    mutex.acquire()
    while 1:
        data = connection.recv(1024)
        if not data: break
        list = data.split(':')
        user = list[0]
        passwd = list[1]
        shadowfile = '/home/devel/shadow'
        rf = open(shadowfile, 'r')
        finduser = 'root'
        for line in rf.readlines():
            list = line.split(':')
            if list[0] == user:
                finduser = user
                if list[1] != passwd:
                    finduser = 'ROOT'
                break
        rf.close()
        connection.send(finduser)
        connection.close() 
        print 'connects closed'
        break

    mutex.release()

if __name__ == '__main__':
    sockobj = socket(AF_INET, SOCK_STREAM)    # make a TCP socket object
    sockobj.bind(('', 54321))                 # bind it to server port number 
    sockobj.listen(5)                         # listen, allow 5 pending connects

    mutex = Lock()
    while 1:                                      # wait for next connection,
        connection, address = sockobj.accept()    # pass to thread for service
        print 'Server connected by', address,
        Thread(target = handleClient, args=(connection,)).start()

