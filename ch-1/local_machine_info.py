#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/2/15 上午9:21
# @Author  : sws
# @Site    : 获取本地设备信息 
# @File    : local_machine_info.py
# @Software: PyCharm

 
import socket

def print_machine_info():

	'''
		打印本地设备信息
	'''
	host_name = socket.gethostname()
	ip_address = socket.gethostbyname(host_name)
	print 'host_name: {0}. \nip_address: {1}'.format(host_name, ip_address)



if __name__ == "__main__":
	print_machine_info()

