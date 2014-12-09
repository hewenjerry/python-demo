import os

if __name__=='__main__':
	d = dict([('a', 1), ('b', 2), ('c', 3)])
	print 'sort before: %s' % d 
	print 'sort after: %s'  % sorted(d.items(), lambda x, y: cmp(x[1], y[1]),reverse=True)
