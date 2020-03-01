#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket

def retBanner(ip, port):
    try: 
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        return s.recv(1024)
    except:
        print('[-] no return for IP {} in  Port {}'.format(ip, port))
        return

def checkVulns(banner):
    f = open("vulnerable_banners.txt")
    for line in f.readlines():
        if line.strip('\n') in banner:
            print('[+] Server is vulnerable: {}'.format(banner.strip('\n')))

def main():
    port_list = [21, 22, 25, 80, 110, 443]
    for x in range(1, 255):
        ip = '192.168.100.{}'.format(str(x))
        for port in port_list:
            banner = retBanner(ip, port)
            if banner:
                print("[+] {} : {}".format(ip, banner))
                checkVulns(banner)

if __name__ == '__main__':
    main()

# Continue Page 16 File I/O