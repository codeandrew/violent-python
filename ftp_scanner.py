#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket

port_list = [21, 22, 25, 80, 110, 443]
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
        return s.recv(1024)
    except:
        print('[-] no return for {}'.format(ip))
        return

def checkVulns(banner):
    if 'FreeFloat Ftp Server (Version 1.00)' in banner:
        print('[+] FreeFloat FTP Server is vulnerable.')
    elif '3Com 3CDaemon FTP Server Version 2.0' in banner:
        print('[+] 3CDaemon FTP Server is vulnerable.')
    elif 'Ability Server 2.34' in banner:
        print('[+] Ability FTP Server is vulnerable.')
    elif 'Sami FTP Server 2.0.2' in banner:
        print('[+] Sami FTP Server is vulnerable.')
    else:
        print('[-] FTP Server is not vulnerable.')
    return

def main():
    ip1 = '192.168.100.102'
    ip2 = '192.168.100.17'
    port = 21

    banner1 = retBanner(ip1, port)
    banner2 = retBanner(ip2, port)
    print(banner1, banner2)
    if banner1:
        print("[+] {} : {}".format(ip1, banner1))
        checkVulns(banner1)
    if banner2:
        print("[+] {} : {}".format(ip2, banner2))
        checkVulns(banner2)

if __name__ == '__main__':
    main()
