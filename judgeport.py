#coding=UTF-8
"""Usage: judgeport.py -a ADDRESS -p PORT

Options:
    -h --help
    -a  the address to be tested
    -p  the port to be tested
"""

#注意：
#Usage的冒号后需要加空格；Usage以一个空行结束；
#Options每一行以'-'开头；同一行相同可选参数以空格隔开；选项和描述间需要两个或以上的空格；
#可以定义默认值([default:value])
from docopt import docopt
import socket
import re
import sys
def check_server(address,port):
    s=socket.socket()
    try:
        s.connect((address,port))
        return True
    except socket.error,e:
        return False

if __name__=='__main__':
    arggs=docopt(__doc__)
    if check_server(arggs['ADDRESS'],int(arggs['PORT'])):
        print 'OK'
    else:
        print 'SHIT'
