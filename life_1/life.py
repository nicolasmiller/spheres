#!/usr/bin/env python

# spoj 1 - life, the universe, and everything

import sys

for line in sys.stdin:
    line = line.strip()
    if int(line) == 42:
        break
    print line
