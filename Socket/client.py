#!/usr/bin/env python
# coding: utf8

import sys
import time
import socket
import threading
from random import randrange


class Client(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = None
        self.mock = None

    def connect(self):
        '''连接'''
        if self.sock is None:
            self.sock = socket.socket()  # 创建 socket 对象
            addr = (self.host, self.port)
            self.sock.connect(addr)      # 向服务器发起连接

    def disconnect(self):
        '''断开连接'''
        if self.sock is not None:
            self.sock.close()

    def send(self, msg):
        if not isinstance(msg, bytes):
            msg = str(msg).encode('utf8')
        self.sock.sendall(msg)

    def recv(self):
        '''持续接收消息并打印'''
        msg = None
        while msg != b'':
            if msg is not None:
                print('\n[recv from server] %s\n' % msg)
            try:
                msg = self.sock.recv(1024)  # 接受客户端数据
            except socket.error:
                print('exit')
                return

    def user_input(self):
        '''接受用户输入，并发送消息'''
        msg = None
        while msg != 'exit':
            msg = input('\n>>> ')
            self.send(msg)
            time.sleep(0.1)

    def __enter__(self):
        '''
        1. 建立连接
        2. 向服务器发送 "Hello"
        3. 返回实例本身
        '''
        self.connect()
        self.send("hello")
        return self

    def __exit__(self, type, value, traceback):
        '''
        1. 向服务器发送 'bye'
        2. 断开连接
        '''
        self.send('bye')
        self.disconnect()


if __name__ == '__main__':
    with Client('127.0.0.1', 10001) as c:   # 创建客户端并连接服务器
        # 需求：发消息的时候，同时可以接收消息，并且把消息打印出来
        t = threading.Thread(target=c.recv)
        t.setDaemon(True)
        t.start()
        c.user_input()
