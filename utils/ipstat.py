#!/usr/bin/python

"""cal log file number of ip"""

import re

f=open("/usr/local/tengine/logs/access.log","r")
arr={}
lines = f.readlines()
for line in lines:
     ipaddress=re.compile(r'((?:(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))\.){3}(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d))))')
     match=ipaddress.match(line)
     if match:
            ip = match.group(1)
            if(arr.has_key(ip)):
                arr[ip]+=1
            else:
                arr.setdefault(ip,1)

f.close()
for key in arr:
        print(key+"->"+str(arr[key]))