#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time:2022/1/3 16:55
# @author: Mrwhite
# @File:testNozhuanyi.py
# @DESC:


test = r'{"a":"\nacd","b":"tesxt5","c":67}';

test1=test.replace(r"\n","")

print(test)
print(test1)