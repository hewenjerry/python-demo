import os
class Person(object):
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return "{first name :" + self.first_name \
            + " ; last name :" + self.last_name + "}"


a1 = [Person("liu", "xing"), Person("liu", "xu"), Person("zhang", "xing")]
a2 = [Person("liu", "qin"), Person("li", "jun"), Person("zhang", "hua")]
if __name__=='__main__':
	print a1
	print a2
        d = {}
        for per in a1:
          if per.first_name not in d:
            d[per.first_name] = []
          d[per.first_name].append(per)
        for per in a2:
          if per.first_name not in d:
            d[per.first_name] = []
          d[per.first_name].append(per)
	
	print 'normal way group: %s' % d
	
	d = {}
	for per in a1:
	  d.setdefault(per.first_name,[]).append(per)
	for per in a2:
	  d.setdefault(per.first_name,[]).append(per)
	print 'dict setdefault: %s' % d
