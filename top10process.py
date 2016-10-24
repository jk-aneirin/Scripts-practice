from subprocess import call
ret=call("ps axww|grep -v '\['|awk '{print $5,$6,$7,$8}'|uniq -c|sort -nr|head",shell=True)
print ret
