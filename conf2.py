#!/usr/bin/env python
#! -*- coding: utf8 -*-

import re
import os

def string2list(s, sep=','):
    return [i.strip() for i in s.split(sep)]

def is_separator(c):
    assert isinstance(c, basestring)
    if c == ":" or c == "=" or c.isspace():
        return True
    return False

class ConfParse(object):
    """
    """

    def __init__(self, filename, resolve_ref=True):
        self.options = {}
        self.messages = []
        self.parse(filename)
        if resolve_ref:
            self.resolve_reference()

    def get(self, key, default_value = "", resolve_ref = False):
        key = key.lower()
        value = self.options.get(key, default_value)
        if resolve_ref:
            ref = re.match(".*\\{\\{(.*?)\\}\\}", value)
            if not ref:
                return value
            ref_val = ref.group(1).strip()
            pos1 = value.find('{')
            pos2 = value.rfind('}') + 1
            prefix = value[:pos1]
            lastfix = value[pos2:]
            if ref_val != key:
                rv = self.get(ref_val, default_value, resolve_ref)
                self.options[key] = prefix + rv + lastfix
                return rv
        else:
            return value

    def get_values(self, key):
        val = self.get(key)
        vals = [v.strip() for v in val.split(',')]
        return vals

    def get_all(self):
        return self.options

    def parse(self, filename):
        try:
            f = open(filename, 'r')
        except:
            return

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
            if whole_line:
                yield whole_line

        for line in lines():
            # remove comments
            line = line.split("#")[0].split(";")[0]
            if not line:
                continue
            s_s_pos = -1
            s_e_pos = -1
            for pos, c in enumerate(line):
                if is_separator(c):
                    if s_s_pos == -1:
                        s_s_pos = pos
                    s_e_pos = pos
                elif s_s_pos != -1:
                    break # end-of-separator

            if s_e_pos == -1:
                key = line
                val = ''
            else:
                key = line[:s_s_pos]
                val = line[s_e_pos + 1:]

            key = key.strip()
            val = val.strip()

            if key == 'include':
                path = val
                if not os.path.isabs(path):
                    path = os.path.dirname(os.path.abspath(filename)) + '/' + val
                self.parse(path)
            else:
                self.options[key] = val

    def resolve_reference(self):
        for key in  self.options:
            self.get(key, "", True)

class Conf(object):

    def __init__(self, filename):
        self._conf = ConfParse(filename)
        self.local_conf = {}
        self.local_conf['local_ip'] = '127.0.0.1'

    def get_values(self, key):
        val = self.local_conf.get(key)
        if val:
            return [p.strip() for p in val.split(',')]
        sv = self._conf.get_values(key)
        vals = [val for val in sv]
        return vals

    def get(self, key, val=''):
        local_val = self.local_conf.get(key)
        if local_val:
            return local_val
        return self._conf.get(key, val)

    def get_all(self):
        all_conf = self._conf.get_all()
        real_all_conf = {}
        for key, value in all_conf.items():
            real_all_conf[key] = value
        real_all_conf.update(self.local_conf)
        return real_all_conf

    def __getattr__(self, name):
        try:
            return super(Conf, self).__getattr__(name)
        except:
            return self.get(name)

if __name__ == '__main__':
    conf = Conf('./test.conf')
    #conf = Conf('./t.conf')
    options = conf.get_all()
    for key in options:
        print key, options[key]
