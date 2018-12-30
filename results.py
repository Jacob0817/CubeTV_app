#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 18-12-16
# @Author  : Jacob_Zhou (zzh839985914@gmail.com)
# @Link    : https://github.com/Jacob0817
# @Version : $Id$

from sql import *


class format_value:

    def __init__(self, rtime):
        self.time = str(rtime)[::-1]
        self.rtime = rtime

    # 分-秒-毫秒
    def msx(self):
        if (self.time == '1-'):
            return('DNF')
        elif (self.time == '2-'):
            return('DNS')
        else:
            if(self.rtime >= 6000):
                self.rtime = (int(self.rtime / 6000)) * 10000 + self.rtime - 6000
                self.time = str(self.rtime)[::-1]
            arr = [self.time[i:i + 2] for i in range(0, len(self.time), 2)]
            time = '.'.join(arr)
            return time[::-1]

    # 秒-毫秒
    def sx(self):
        if (self.time == '1-'):
            return('DNF')
        elif (self.time == '2-'):
            return('DNS')
        else:
            arr = [self.time[i:i + 2] for i in range(0, len(self.time), 2)]
            time = '.'.join(arr)
            return time[::-1]


def n_results(personid, eventid):
    p = Results.select().where(Results.personid == personid, Results.eventid == eventid)
    p_count = Results.select().where(Results.personid == personid, Results.eventid == eventid).count()
    a_val = []
    for i in range(p_count - 1, p_count - 6, -1):
        value1 = format_value(p[i].value1)
        value2 = format_value(p[i].value2)
        value3 = format_value(p[i].value3)
        value4 = format_value(p[i].value4)
        value5 = format_value(p[i].value5)
        val = [value1.msx(), value2.msx(), value3.msx(), value4.msx(),value5.msx()]
        a_val.append(val)
    return a_val


if __name__ == '__main__':
    results = n_results('2011ZHAN24', 333)[0]
    print(results)
