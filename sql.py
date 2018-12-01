#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 18-11-30
# @Author  : Jacob_Zhou (zzh839985914@gmail.com)
# @Link    : https://github.com/Jacob0817
# @Version : $Id$

import os
from peewee import *

database = MySQLDatabase("test", user="root", host="localhost", port=3306)


class Person(Model):
    name = CharField()
    birthday = DateField()
    is_relative = BooleanField()

    class Meta:
        database = database

if __name__ == '__main__':
    p = Person(name = 'test_name', birthday = 19980708, is_relative = True)
    p.save()
