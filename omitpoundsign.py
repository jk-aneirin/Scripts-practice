#!/usr/bin/env python
import sys
import re
file=sys.argv[1]
prog=re.compile('^\s*#')
with open(file,'r') as f:
    for line in f:
        if not prog.match(line):
            print line,


