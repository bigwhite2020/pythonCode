#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time:2022/6/19 16:53
# @author: Mrwhite
# @File:glabal_demo.py
# @DESC:

variable = "very good"

def up_variable():
    global variable
    variable = variable+"ok"
    return  variable

res = up_variable()
print(res)
print(variable)
