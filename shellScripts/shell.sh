#!/bin/bash
#bash的内置命令shift可以往前移动位置参数的值，其语法如下：
#shift n 
#执行shift n，${n+1}的值会放入$1
echo "\$@的初始值：$@"
while shift
do
    [ -n "$1" ]&&echo "shift 1次，\$@的变化：$@"
done

