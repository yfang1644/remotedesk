#!/usr/bin/python
# File Name: client.py

from socket import *              # portable socket interface plus constants


class Client():
    def __init__(self, host='192.168.1.101', port=54321):
        self.sockobj = socket(AF_INET, SOCK_STREAM)
        self.sockobj.connect((host, port))

    def send(self, message):
        self.sockobj.send(message)

    def receive(self, cnt):
        return self.sockobj.recv(cnt)

    def close(self):
        self.sockobj.close()
