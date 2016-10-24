#!/usr/bin/env python
'''Usage: setsys.py [-t TIMESERVER] [-n HOSTNAME]

Options:
    -h --help
    -t  timeserver used by command ntpdate
    -n  hostname you want to use
'''
from subprocess import call
from docopt import docopt

def setTime(ntpserver): #ntpserver can use pool.ntp.org
    ret=call(['ntpdate',ntpserver])
    print ret
arggs=docopt(__doc__)
setTime(arggs['TIMESERVER'])
