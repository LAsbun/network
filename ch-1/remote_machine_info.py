#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/2/15 下午1:34
# @Author  : sws
# @Site    : 获取远程设备的信息
# @File    : remote_machine_info.py
# @Software: PyCharm

import socket

def get_remote_machine_info():
    remote_host = 'www.lasbun.com'
    try:
        ip_address = socket.gethostbyname(remote_host)
        print 'Ip is {0}'.format(ip_address)
    except socket.error, err_msg:
        print '{0}:{1}'.format(remote_host, err_msg)

get_remote_machine_info()