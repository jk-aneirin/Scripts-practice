#!/usr/bin/env python
import subprocess
import re
def lkquality(*gws):
    rstdict={}
    for gw in gws:
        lkrst=subprocess.Popen('ssh username@{} ping -c10 www.baidu.com'.format(gw),\
                shell=True,stdout=subprocess.PIPE)

        pct=re.search('(\d{1,2})%',lkrst.stdout.read()).group(1)
        rstdict[gw]=int(pct)
    return rstdict

def mofrt(gw):
    subprocess.call('ip route del 0/0 && ip route add default via {}'.format(gw),shell=True)

if __name__=='__main__':
    gws=['gw1','gw4','gw2','gw3']
    d=lkquality(*gws)
    print min(d.items(),key=lambda x:x[1])[0]
    #mofrt(gw)



