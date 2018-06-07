#!/bin/bash
shopt -s -o nounset
ACTno=${1:?'wrong!provide account number'}
PKey=''
ACT=''
ACTprefix='stu'  #prefix account
ACTlist='accounts.txt'
declare -i k okact=0

gen_key() {
    declare -i N I
    declare -i KeyLen  #store length of passwd
    KeyLen=${1:?'wrong!provide length of string'}
    PKey=''
    AFB='ABCDEFGHIJKLM;0123456789#abcdefghijk_NOPQRSTUVWXYZ;
    mnopqrstuvwxyz^0123456789_abcdefghijk#0123456789;mnopqrstuvwxyz_ABCDEFGHIJKLM^0123456789'
    for ((I=0;I<KeyLen;I++))
    do
        N=$(head -1 /dev/urandom |od -N 2 |head -1 |awk '{print $2 * 1}')
        ((N%=${#AFB}))
        PKey=$PKey${AFB:$N:1}  #PKey store passwd
    done
}

echo "-------------------------">>$ACTlist

for ((k=1;k<=$ACTno;k++))
do
    ACT="$ACTprefix$k"
    gen_key 6 
    adduser --quiet --disabled-password --gecos '' $ACT
    if [ $? -eq 0 ];then
        echo "$ACT:$PKey"|chpasswd
        echo "account:$ACT|passwd:$PKey">>$ACTlist
        echo "----------------------------">>$ACTlist
        ((okact++))
        echo "account creation completion"
    fi
done

echo "create number of account $okact"
echo "look at file $ACTlist"
