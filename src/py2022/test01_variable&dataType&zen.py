#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time:2022/4/17 16:08
# @author: Mrwhite
# @File:test01_variable&dataType&zen.py
# @DESC:

#1含引号的字符串变量
print("python is 'ok'")
print('java is "ok"')
print("shell is \"ok\"")

#2制表符与换行符
print("test01\ntest02\ttest03")

#3大小写
myTest1="myTEst";
myTest2="MyTest";
print(myTest1.upper())
print(myTest2.lower())

#4f表达式拼接字符
firstName='Mr'
middleName='ok'
lastName='white'
print(f'{firstName}.{middleName}.{lastName}')

#5删除空间
text = ' this is  s stripTest             '
print(f"'{text.lstrip()}'");
print(f"'{text.rstrip()}'")
print(f"'{text.strip()}'")

#6基本运算
print(4/2)
print(4//2)
print(1+2)
print(1+2.0)
print(1200_00_123)

#7常量
MAX_THINGS='HELLO WORLD'

#8注释
#不会打印注释的

