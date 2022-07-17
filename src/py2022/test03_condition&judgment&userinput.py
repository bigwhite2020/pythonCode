#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time:2022/5/12 23:05
# @author: Mrwhite
# @File:test03_condition&judgment&userinput.py
# @DESC:

# 一. if语句
# 1 if-else
cars=['audi', 'bmw', 'toyota']
for car in cars:
    if car=='bmw':
        print( f'this car is {car},is my car' )
    else:
        print( f'this car is {car},is not my car' )

# 2 if-elif-else
age=12
if (age<4):
    print( "Your admission cost is $0." )
elif (age<18):
    print( "Your admission cost is $50." )
else:
    print( "Your admission cost is $100." )

# 二.条件检索
# 1 忽略大小写
car='Audi'
print(car=='audi')
print(car.lower()=='audi')
print(car.upper()=='AUDI')
# 2、检查不相等
car='Audi'
print(car !='audi')
# 3、检查多个条件
age_0=22
age_1=18
print(age_0>=21 and age_1>=21)
print(age_0>=21 and age_1<21)
print(age_0>=21 or age_1>=21)
# 4、检查特定值是否包含在列表中
testList=['A','B','C']
print('A' not in testList)
print('D' not in testList)
# 5、检查列表是否为空
testList2=[1,2,3]
testList3=[]
if testList2:
    for test in testList2:
        print(test)
    else:
        print("testList2为空")
if testList3:
    for test in testList2:
        print(test)
    else:
        print("testList3为空")

#三.用户输入input
# 1、用户输入并返回
message = input("Tell me something,and i will repeat it back to you:")
print(message)
# 2、f表达式返回
name=input("Please enter yout name:")
print(f"my name is {name}!")
# 3、更长的句子
prompt="Tell me something,and I will repeat it back to you,"
prompt+="\nWhat's your name?\n"
name=input(prompt)
print(f"hello {name.title()}")
# 4、int()获取数值输入
age=input("How old are you？:")
age=int(age)#不转换会报错
print(f"Your age is {age+1}!")

#四.while+inoput(),让用户选择何时退出
#1、普通用法
prompt="Tell me something,and I will repeat it back to you:"
prompt+="\nEnter 'quit' to be end the program."
message=""
while message!='quit':
    message=input(prompt)
    if message!='quit':
        print(message)
#2、进阶用法
prompt="Tell me something,and I will repeat it back to you:"
prompt+="\nEnter 'quit' to be end the program."
#设置标志
active=True
while active:
    message=input(prompt)
    if message=='quit':
        active=False
    else:
        print(message)





