#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import sys
import os

def retBanner(ip, port):
    try: 
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        return s.recv(1024)
    except:
        print('[-] no return for IP {} in  Port {}'.format(ip, port))
        return

def checkVulns(banner, filename):
    f = open(filename, "r")
    for line in f.readlines():
        if line.strip('\n') in banner:
            print('[+] Server is vulnerable: {}'.format(banner.strip('\n')))

def get_argument():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        if not os.path.isfile(filename):
            print('[-] {} does not exist.'.format(filename))
            exit(0)
        if not os.access(filename, os.R_OK):
            print('[-] {} access denied.'.format(filename))
            exit(0)
        print("[+] Reading Vulnerabilities From: {}".format(filename))
        return filename
    else:
        print("[-] Usage: {} <vulnerable file banner>".format(sys.argv[0]))
        exit(0)

def main():
        filename = get_argument()
        port_list = [21, 22, 25, 80, 110, 443]
        for x in range(1, 255):
            ip = '192.168.100.{}'.format(str(x))
            for port in port_list:
                banner = retBanner(ip, port)
                if banner:
                    print("[+] {} : {}".format(ip, banner))
                    checkVulns(banner, filename)

if __name__ == '__main__':
    main()

# Continue Page 16 File I/O