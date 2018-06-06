import sys
import os
import time
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyPathMonitor(FileSystemEventHandler):
    def __init__(self,dpath):
        self.dpath=dpath

    def fcopy(self,file):
        shutil.copy(file,self.dpath)

    def on_created(self,event):
        super(MyPathMonitor,self).on_created(event)
        if not event.is_directory:
            print "created name:{0}".format(event.src_path)

    def on_modified(self,event):
        super(MyPathMonitor,self).on_modified(event)
        if not event.is_directory:
            fname=event.src_path
            self.fcopy(fname)

def help():
    print "sys.argv[1]:the Dir which will be monitor\nsys.argv[2]:modified file will be backup here\
            \nctrl+c exit "

if __name__=='__main__':
    if len(sys.argv)!=3:
        help()
        sys.exit()

    mpath=sys.argv[1]
    dpath=sys.argv[2]

    if not os.path.isdir(dpath):
        print "dpath must be dir!"
        sys.exit()

    event_handler=MyPathMonitor(dpath)
    observer=Observer()
    observer.schedule(event_handler,mpath)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
