#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket

port_list = [21, 22, 25, 80, 110, 443]
port_open = True

services = {
    'ftp': 21,
    'ssh' : 22,
    'smtp': 25,
    'http': 80
}

def retBanner(ip, port):
    try: 
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner
    except:
        return

def main():
    ip1 = '192.168.95.148'
    ip2 = '192.168.95.149'
    port = 21

    banner1 = retBanner(ip1, port)
    if banner1: print("[+] {} : {}".format(ip1, banner1))
    if banner2: print("[+] {} : {}".format(ip2, banner2))


if __name == '__main__':
    main()
