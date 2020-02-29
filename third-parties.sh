#!/bin/sh 
wget http://xael.org/norman/python/python-nmap/python-nmap-0.2.4.tar.gz -O nmap.tar.gz

tar -xzf nmap.tar.gz

cd python-nmap-0.2.4/

python setup.py install


