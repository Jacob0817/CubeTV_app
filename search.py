#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 18-12-01
# @Author  : Jacob_Zhou (zzh839985914@gmail.com)
# @Link    : https://github.com/Jacob0817
# @Version : $Id$

from sql import *


class format_value:

    def __init__(self, rtime):
        self.rtime = str(rtime)[::-1]

    def msx(self):
        if (self.rtime == '1-'):
            return('DNF')
        elif (self.rtime == '2-'):
            return('DNS')
        else:
            arr = [self.rtime[i:i + 2] for i in range(0, len(self.rtime), 2)]
            time = '-'.join(arr)
            return time[::-1]


if __name__ == '__main__':
    p = Results.select().where(Results.personid == '2014ZHOU09')
    for person in p:
        value1 = format_value(person.value1)
        print(value1.msx())
