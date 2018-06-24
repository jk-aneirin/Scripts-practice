#!/usr/bin/env python
import os
import logging
from logging.handlers import TimedRotatingFileHandler

CRITICAL = 50
FATAL = CRITICAL
ERROR = 40
WARNING = 30
WARN = WARNING
INFO = 20
DEBUG = 10
NOTSET = 0

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))
ROOT_PATH = os.path.join(CURRENT_PATH, os.pardir)
LOG_PATH = os.path.join(ROOT_PATH, 'log')

class LogHandler(logging.Logger):
    def __init__(self,name,level = DEBUG,stream = True,file = True):
        self.name = name
        self.level = level
        # unbound method,has parameter 'self'
        #logging.Logger.__init__(self,self.name,level = level)
        # bound method,omit parameter 'self'
        super(LogHandler,self).__init__(name,level = level)
        if stream:
            self.__setStreamHandler__()
        if file:
            self.__setFileHandler__()

    def __setFileHandler__(self,level = None):
        file_name = os.path.join(LOG_PATH,'{name}.log'.format(name = self.name))
        file_handler = TimedRotatingFileHandler(filename = file_name,when = 'D',interval = 1,backupCount = 7)
        file_handler.suffix = '%Y%m%d.log'
        if not level:
            file_handler.setLevel(self.level)
        else:
            file_handler.setLevel(level)

        formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
        file_handler.setFormatter(formatter)

        self.file_handler = file_handler
        self.addHandler(file_handler)

    def __setStreamHandler__(self,level = None):
        stream_handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
        stream_handler.setFormatter(formatter)
        if not level:
            stream_handler.setLevel(self.level)
        else:
            stream_handler.setLevel(self.level)

        self.addHandler(stream_handler)

    def resetName(self,name):
        self.name = name
        self.removeHandler(self.file_handler)
        self.__setFileHandler__()

if __name__ == '__main__':
    log = LogHandler('test')
    log.info('this is a test msg')
