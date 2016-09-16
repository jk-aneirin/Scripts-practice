import Pyro4
import platform
import os
from collections import namedtuple
import cStringIO
import cpuinfo
import re
class GetSysInfo():
    def __init__(self):
        self.disk_ntuple=namedtuple('partition','device mountpoint fstype')
        self.usage_ntuple=namedtuple('usage','total used free percent')
    def disk_partitions(self,all=False):
        phydevs=[]
        f=open('/proc/filesystems','r')
        for line in f:
            if not line.startswith('nodev'):
                phydevs.append(line.strip())
        retlist=[]
        f=open('/etc/mtab','r')
        for line in f:
            if not all and line.startswith('none'):
                continue
            fields=line.split()
            device=fields[0]
            mountpoint=fields[1]
            fstype=fields[2]
            if not all and fstype not in phydevs:
                continue
            if device=='none':
                device=''
            ntuple=self.disk_ntuple(device,mountpoint,fstype)
            retlist.append(ntuple)
        return retlist
    def disk_usage(self,path):
        st=os.statvfs(path)
        free=(st.f_bavail*st.f_frsize)
        total=(st.f_blocks*st.f_frsize)
        used=(st.f_blocks-st.f_bfree)*st.f_frsize
        try:
            percent=(float(used)/total)*100
        except ZeroDivisionError:
            percent=0
        return self.usage_ntuple(str(total/1024/1024)+'M',\
                str(used/1024/1024)+'M',str(free/1024/1024)+'M',round(percent,1))

    def get_cpuinfo(self):
        return cpuinfo.get_cpu_info()

    def get_diskinfo(self):
        ret=''
        output=cStringIO.StringIO()
        for part in self.disk_partitions():
             output.write(str(part))
             output.write(str(self.disk_usage(part.mountpoint)))
             output.write('\n')
        ret=output.getvalue()
        output.close()
        return ret

    def get_meminfo(self):
        ret_mem=[]
        with open('/proc/meminfo','r') as f:
            for line in f:
                m1=re.search(r'^MemTotal:\s+(\d+)',line)
                m2=re.search(r'^MemAvailable:\s+(\d+)',line)
                if m1:
                    ret_mem.append(m1.group())
                elif m2:
                    ret_mem.append(m2.group())
                else:
                    continue
        return ret_mem


class GetSysteminfo(object):
    def __init__(self):
        self.sysinfo=GetSysInfo()
    @Pyro4.expose
    def get_sysinfo(self,which):
        switcher={
                'cpu':self.sysinfo.get_cpuinfo,
                'disk':self.sysinfo.get_diskinfo,
                'memory':self.sysinfo.get_meminfo,
                }
        return switcher.get(which)()

def main():
    Pyro4.Daemon.serveSimple({GetSysteminfo:"Get.systeminfo"},\
            host='192.168.19.130',ns=False)

if __name__=='__main__':
    main()
