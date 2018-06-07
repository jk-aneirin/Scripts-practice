#!/bin/bash

shopt -s -o nounset
desfile=$(find /home/xl/sh -name '*.one')
for f in $desfile;do
    mv $f `echo $f |sed 's/one/txt/'` 
done
