import subprocess
import sys
res=[]
commands="du -sh /home/xl"
hosts=["server1","server2"]
def GetSize(hosts):
    for host in hosts:
        ssh=subprocess.Popen(["ssh",host,commands],shell=False,stdout=subprocess.PIPE,\
                stderr=subprocess.PIPE)
        res.append(ssh.stdout.readlines())
    print res
GetSize(hosts)
