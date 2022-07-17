#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time:2022/7/17 16:40
# @author: Mrwhite
# @File:closuresAndDecorators.py
# @DESC:

def func1(func):#外部闭包函数的参数是被装饰的函数对应
    def func2():
        print("装饰器新增加的打印项")
        return func() #返回外部函数接受的参数被装饰函数的调用
    return func2

#return func   #返回了函数名
#return func() #返回了函数的调用

@func1
def myprint():
    print("你好，我是print")

myprint()
