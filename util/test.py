#!/usr/bin/env python
# encoding: utf-8

if __name__ == '__main__':
    try:
        f = open('./test.conf', 'r')
    except:
       raise

    def lines():
        whole_line = ""
        for line in f:
            line = line.strip()
            if line.endswith("\\"): # wrap lines
                whole_line += line[:-1]
                continue
            whole_line += line
            yield whole_line
            whole_line = ""
#        if whole_line:
#            yield whole_line

    for line in lines():
        if line :
           print 'filter str=%s' % line
