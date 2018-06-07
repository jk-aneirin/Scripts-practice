#!/bin/bash

shopt -s -o nounset

DIR=${1:?'provide the path,eg:/var'}
if [[ ! $DIR == /* ]];then  
    DIR=/$DIR
fi

declare -i size SIZE
SIZE=50

while read size dir;do
    if [ $size -gt $SIZE ];then
        echo -e "$size\t\t$dir"
    fi
done < <(find $DIR -mindepth 1  -type d -exec du -sm {} \;)

