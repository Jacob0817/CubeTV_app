#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 18-12-16
# @Author  : Jacob_Zhou (zzh839985914@gmail.com)
# @Link    : https://github.com/Jacob0817
# @Version : $Id$

import os
from search import *

def n_results(personid,eventid):
    p = Results.select().where(Results.personid == personid, Results.eventid == eventid)
    p_count = Results.select().where(Results.personid == personid, Results.eventid == eventid).count()
    a_val = []
    for i in range(p_count -1,p_count -6,-1):
        value1 = format_value(p[i].value1)
        value2 = format_value(p[i].value2)
        value3 = format_value(p[i].value3)
        value4 = format_value(p[i].value4)
        value5 = format_value(p[i].value5)
        val = [str(value1.msx()),str(value2.msx()),str(value3.msx()),str(value4.msx()),str(value5.msx())]
        a_val = a_val + val
    return a_val

if __name__ == '__main__':
    print(n_results('2011ZHAN24',444))
