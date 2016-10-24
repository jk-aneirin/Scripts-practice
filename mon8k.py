#!/usr/bin/envpython
import socket
import sys
import logging
import commands

logging.basicConfig(level= logging.DEBUG,\
        format = '%(asctime)s %(levelname)s %(message)s',\
        datefmt = '%a, %d %b %Y %H:%M:%S',\
        filename = '/tmp/msrv.log',\
        filemode = 'w')

def check_port(address,port):
    s = socket.socket()
    try:
        s.connect((address,port))
        return True
    except socket.error,e:
        return False

if __name__=="__main__":
    if check_port('10.0.0.10',8000):
        pass
    else:
        logging.warning('port 8000 connection fail')
        (status,output)=commands.getstatusoutput('docker start msrv')
        logging.info(output)
