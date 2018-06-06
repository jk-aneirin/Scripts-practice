import re
def CountHttpStatus(alog):
    ret=dict()
    pa=re.compile('HTTP\/1.1\"\s[0-9]{3}')
    with open(alog,'r') as f:
        for line in f.readlines():
            m=pa.search(line)
            if m:
                status=m.group().split()[1]
                if status in ret:
                    ret[status]+=1
                else:
                    ret[status]=1

            else:
                continue
    #print sorted(ret.items(),key=lambda x:x[1],reverse=True)
    for k,v in ret.items():
        print k,v
CountHttpStatus('./apache.log')



