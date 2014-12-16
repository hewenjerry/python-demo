# coding: utf-8
#!/usr/bin/env python

import time
from multiprocessing import Pool
import random
import os

def div_list(ls,n):
    if not isinstance(ls,list) or not isinstance(n,int):
        return []
    ls_len = len(ls)
    if n<=0 or 0==ls_len:
        return []
    if n > ls_len:
        return []
    elif n == ls_len:
        return [[i] for i in ls]
    else:
        j = ls_len/n
        k = ls_len%n
        ls_return = []
        for i in xrange(0,(n-1)*j,j):
            ls_return.append(ls[i:i+j])
        ls_return.append(ls[(n-1)*j:])
        return ls_return


def long_time_task(name,taskList):
    print 'Run task %s (%s) %s...' % (name, os.getpid(), taskList)
    start = time.time()
    for x in taskList:
        print "starting  %s" % x
        print os.popen('sh grep_log_file.sh "3190830679" ' + x).readlines()
        print "ending  %s" % x
    end = time.time()
    print 'Task %s runs %0.2f seconds.' % (name, (end - start))

if __name__=='__main__':
      allFiles=os.popen('sh grep_log.sh 2014-12-15 "3190830679"').readlines()
      allFiles=map(lambda x: x[14:-1], allFiles)
      THREAD_NUM=22
      divList=div_list(allFiles,THREAD_NUM)

      print 'Parent process %s.' % os.getpid()
      p = Pool()
      for i in range(THREAD_NUM):
            p.apply_async(long_time_task, args=(i,divList[i]))
      print 'Waiting for all subprocesses done...'
      p.close()
      p.join()
      print 'All subprocesses done.'
