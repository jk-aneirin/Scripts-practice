#!/usr/bin/env python
import socket,struct
import subprocess
import re

gws=['ip1','ip2','ip3','ip4']
def lkquality(*gws):
    rstdict={}
    for gw in gws:
        lkrst=subprocess.Popen('ssh username@{} ping -c5 www.baidu.com'.format(gw),\
                shell=True,stdout=subprocess.PIPE)

        pct=re.search('(\d{1,2})%',lkrst.stdout.read()).group(1)
        rstdict[gw]=int(pct)
    return rstdict

def get_df_gw():
    with open('/proc/net/route') as fh:
        for line in fh:
            fields=line.strip().split()
            if fields[1] != '00000000' or not int(fields[3], 16) & 2:
                continue
            return socket.inet_ntoa(struct.pack("<L", int(fields[2], 16)))

def mofrt():
    lk=lkquality(*gws)
    print lk
    curgw=get_df_gw()
    bestgw=min(lk.items(),key=lambda x:x[1])[0]
    if lk[curgw]==lk[bestgw]:
        print 'gw ok'
    else:
        print 'change gw'
        #subprocess.call('sudo ip route del 0/0 && sudo ip route add default via {}'.format(bestgw),shell=True)

if __name__=='__main__':
    mofrt()


