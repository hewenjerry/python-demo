import time
import calendar
from datetime import date, datetime

def add_month(sourcedate, months):
    '''
    >>> add_month(date(2010,10,31), 1) == date(2010, 11, 30)
    True
    >>> add_month(date(2010,10,31), 12) == date(2011, 10, 31)
    True
    '''
    month = sourcedate.month - 1 + months
    year = sourcedate.year + month / 12
    month = month % 12 + 1
    day = min(sourcedate.day, calendar.monthrange(year,month)[1])
    return sourcedate.replace(year=year, month=month, day=day)

def mkdate(datestr):
    if len(datestr) == 4:
        datestr = '%s-%s-%s' % (datetime.now().year, datestr[:2], datestr[2:])
    return datetime.strptime(datestr, '%Y-%m-%d').date()

def date2timestamp(d, to_int=False):
    '''
    >>> date2timestamp(date(2014, 1, 1), to_int=True)
    1388505600
    >>> date2timestamp(date(2014, 1, 1))
    1388505600.0
    '''
    ts = time.mktime(d.timetuple())
    if to_int:
        ts = int(ts)
    return ts

if __name__ == '__main__':
    print mkdate('2013-02-12')
    print mkdate('0212')

    print add_month(mkdate('0419'), 3)
    print add_month(mkdate('0419'), 12)
