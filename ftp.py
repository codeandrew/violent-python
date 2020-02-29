#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket

port = 21
banner = "FreeFloat FTP Server"
print("[+] Checking for {} on port {}".format(banner, str(port)))

port_list = [21, 22, 25, 80, 110, 443]
port_open = True

services = {
    'ftp': 21,
    'ssh' : 22,
    'smtp': 25,
    'http': 80
}

socket.setdefaulttimeout(2)
s = socket.socket()

ip = "192.168.95.148"
s.connect((ip, services.ftp))

answer = s.recv(1024)

print(answer)

