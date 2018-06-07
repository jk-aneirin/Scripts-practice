#!/bin/bash
datafile='gethdsize.sh'
exec 4<&0 #备份标准输入
exec < $datafile #对标准输入进行输入转向的操作，在这个命令之后，只要是读取的操作，其来源皆改到datafile

while read;do
    echo $REPLY #内容会被保存到变量REPLY并打印
done

exec 0<&4  #还原标准输入
exec 4<&-  #关闭文件代码4
