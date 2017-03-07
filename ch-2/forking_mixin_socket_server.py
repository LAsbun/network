#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/2/20 下午1:38
# @Author  : sws
# @Site    : 使用 ForkingMixin
# @File    : forking_mixin_socket_server.py
# @Software: PyCharm

import os
import socket
import threading
import SocketServer

SERVER_HOST = 'localhost'
SERVER_PORT = 0  # 动态是设置端口
BUF_SIZE = 10
ECHO_MSG = 'hello echo server!'

class ForkingClient(object):

    '''
        Client
    '''

    def __init__(self, ip, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.sock.connect((ip, port))
        self.cuId = os.getpid()

    def run(self):
        # cuId = os.getpid()
        cuId = self.cuId
        print 'Pid...{0} '.format(cuId)

        send_data = self.sock.send(ECHO_MSG)

        print 'Sent: {0} characters, so far ..'.format(send_data)

        respon = self.sock.recv(BUF_SIZE)

        print 'Pid..: {0} received {1}'.format(cuId, respon)


    def shutdown(self):
        print 'Pid: {0} is shutdowning.'.format(self.cuId)
        self.sock.close()


class ForkingServerRequestHandler(SocketServer.BaseRequestHandler):

    def handle(self):

        data = self.request.recv(BUF_SIZE)
        cuId = os.getpid()

        res =  '{0}:{1}'.format(cuId, data)

        print '{0}...Sending'.format(cuId)

        self.request.send(res)
        return


class ForkingServer(SocketServer.ForkingMixIn, SocketServer.TCPServer):

    pass


def main():
    server = ForkingServer((SERVER_HOST, SERVER_PORT), ForkingServerRequestHandler)

    ip, port = server.server_address

    server_thread = threading.Thread(target=server.serve_forever)

    server_thread.setDaemon(True)
    server_thread.start()

    client1 = ForkingClient(ip, port)
    client1.run()
    cl2 = ForkingClient(ip, port)
    cl2.run()

    server.shutdown()
    client1.shutdown()
    cl2.shutdown()
    server.socket.close()

if __name__ == "__main__":
    main()