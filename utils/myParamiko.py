#!/usr/bin/env python
#coding:UTF-8
import paramiko
import os
from paramiko.ssh_exception import NoValidConnectionsError
import cmd

class Myssh():
    def __init__(self,host,user,passwd):
        self.ssh=paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            self.ssh.connect(host,username=user,password=passwd)
        except NoValidConnectionsError:
            print "connect failed!"
            exit(1)
    def runCommand(self,command):
            '''在远程主机上执行命令，并将命令执行结果打印出来'''
            stdin,stdout,stderr=self.ssh.exec_command(command)
            print stdout.readlines()
    def fileDownload(self,filename):
            '''从远程主机下载文件，默认保存在该脚本文件相同目录'''
            #fname=os.path.basename(filename)
            ftp=self.ssh.open_sftp()
            ftp.get(filename,filename)#被下载的文件需在用户的家目录
            ftp.close()
    def fileUpload(self,localpath,remotepath):
            ftp=self.ssh.open_sftp()
            ftp.put(localpath,remotepath)
            ftp.close()
r=Myssh('192.168.81.130','xl','123456')
