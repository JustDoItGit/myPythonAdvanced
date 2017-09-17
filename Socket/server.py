#!/usr/bin/env python
# coding: utf8

import socket
import threading


def client_recv(client_socks, cli_sock):
    '''接受客户端消息'''
    for i in range(10):
        try:
            msg = cli_sock.recv(1024)  # 接受客户端数据
        except socket.error:
            print('cli(%r) exit' % cli_sock)
            return

        if not msg:
            return
        else:
            broadcast(client_socks, msg)
            print(msg)


def broadcast(client_socks, msg):
    '''广播'''
    print('[send to clients] %s' % msg)
    for c_sock in client_socks:
        try:
            c_sock.send(msg)
        except BrokenPipeError:
            pass


def main():
    '''Server 端主函数'''
    addr = ('127.0.0.1', 10001)
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.bind(addr)  # 端口绑定
    server_sock.listen(1024)
    client_socks = []

    while True:
        print('[server] i am listening')
        cli_sock, cli_addr = server_sock.accept()  # 等待客户端连接
        print(cli_addr)
        client_socks.append(cli_sock)

        t = threading.Thread(target=client_recv, args=(client_socks, cli_sock))
        t.setDaemon(True)  # 设置线程保护
        t.start()


if __name__ == '__main__':
    main()
