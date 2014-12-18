#!/usr/bin/env python
# encoding: utf-8
import random
import os
from sys import argv
def __number_change(digger_count, bury_count):
    if digger_count <= 7:
        digger_count = random.randint(8,15)
    bury_count = int(digger_count*1.5) + random.randint(1,10)
    return digger_count,bury_count

if __name__ == '__main__':
    digger_count = int(argv[1])
    bury_count = int(argv[2])
    digger_count,bury_count = __number_change(digger_count, bury_count)
    print 'digger_count=%s, bury_count=%s' % (digger_count,bury_count)
    print 'digger_count=%s, bury_count=%s' % (__number_change(digger_count, bury_count))

