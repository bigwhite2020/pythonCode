#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time:2022/7/17 17:53
# @author: Mrwhite
# @File:decorators_demo.py
# @DESC:

def arg_func(sex):
    def func1(b_func):
        def func2():
            if sex == 'man':
                print("你不可以生娃")
            if sex == "woman":
                print("你可以生娃")
            return b_func()
        return func2
    return func1

@arg_func(sex='man')
def man():
    print("好好上班")


@arg_func(sex='woman')
def woman():
    print("好好带娃")

man()
print("-------分割线--------")
woman()

