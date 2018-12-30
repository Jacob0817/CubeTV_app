#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 18-12-16
# @Author  : Jacob_Zhou (zzh839985914@gmail.com)
# @Link    : https://github.com/Jacob0817
# @Version : $Id$

import os
from search import *
import numpy as np
import matplotlib.pyplot as plt

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
        val = [float(value1.sx()),float(value2.sx()),float(value3.sx()),float(value4.sx()),float(value5.sx())]
        a_val.append(val)
    return a_val

if __name__ == '__main__':
    results = n_results('2011ZHAN24',444)[0]
    print(results)    
    x = [1,2,3,4,5]
    y = results

    plt.plot(x,y)
    plt.yticks([30,40,50,60.70])
    plt.title('test')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()