import fnmatch
import os
import subprocess
import getopt
import sys
def usage():
    print '''
    Usage:bziplog.py [-d DIR] [-n PATTERN]
    using pbzip2 compress files in DIR
    Options:
        -h help
        -d files in this dir
        -n files matching this pattern
        '''
def lslog(path):
    for file in os.listdir(path):
        if not fnmatch.fnmatch(file,'*.bz2'):
            yield file

if __name__=='__main__':
    opts,args=getopt.getopt(sys.argv[1:],"d:n:h")
    for opt,arg in opts:
        if opt=='-d':
            opepath=arg
        elif opt=='-n':
            fpattern=arg
        elif opt=='-h':
            usage()
            sys.exit()
    for f in lslog(opepath):
        if not fnmatch.fnmatch(f,fpattern):
            p=subprocess.Popen("sudo niceall pbzip2 /var/log/wumii/crawler/{}".format(f),shell=True)
            print p.wait()