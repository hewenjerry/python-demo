#!/usr/bin/env python
# encoding: utf-8
import os
from sys import argv

class GroupStats(object):
 def __init__(self, id, name,count):
    self.id=id
    self.name=name
    self.count=count
 def __str__(self):
    return 'id=%d, name=%s, count=%d' % (self.id, self.name, self.count)


if __name__ == '__main__':
#    print 'exception before------'
#    raise Exception('invalid param')
#执行shell命令将结果输入到控制台中
    #find_pid_cmd = 'ps aux | grep %s | grep -v grep' % argv[1]
    #ret_val = os.system(find_pid_cmd)
    #print 'retsult=%s' % ret_val
   group_record =GroupStats(1,"hewen",12)
   if group_record :
     group_record .id = group_record .id or 0 if group_record .id > 2 else 9
     group_record .count = group_record .count or 0 if group_record .count > 12 else None

    print group_record
