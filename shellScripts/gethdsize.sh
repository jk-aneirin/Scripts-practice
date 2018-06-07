#!/bin/bash
shopt -s -o nounset
HD=${1:?'input hd type,for example hda or sda'}

#!/bin/bash
shopt -s -o nounset
HD=${1:?'input hd type,for example hda or sda'}

size=$(fdisk -l /dev/$HD |grep "heads,*" |awk '{print $1*$3*$5/2048}')

echo "size of disk is $size MB"
