#!/usr/bin/env python
"""Usage: resetvpn.py [-s SERVER -p SERVERPORT -m METHOD]

Options:
    -h  --help
    -s  the address of server
    -p  the port of server [default: 32143]
    -m  encryption method [default: aes-128-cfb]
"""
from docopt import docopt
import json
import os

def mdfconf(s,p=None,m=None):
    with open('/etc/shadowsocks/config.json') as json_file:
        ct=json.load(json_file)
        ct['server']=s
        if p is not None:
            ct['server_port']=p
        if m is not None:
            ct['method']=m
        return ct

def store(data):
    with open('/etc/shadowsocks/config.json','w') as json_file:
        json_file.write(json.dumps(data))

def rst():
    os.system('sudo service sslocal restart')

if __name__=='__main__':
    arggs=docopt(__doc__)
    data=mdfconf(arggs['SERVER'],arggs['SERVERPORT'],arggs['METHOD'])
    store(data)
    rst()
