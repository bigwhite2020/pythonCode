#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time:2022/5/9 23:03
# @author: Mrwhite
# @File:test02_list.py
# @DESC:

#1访问列表
#1.1访问列表元素
myTest=["A","B","C","D","E","F","G"]
print("列表的第一个元素为：",myTest[0])
print("列表的最后一个元素为：",myTest[-1])
print(f"我最喜欢的一个字母为：{myTest[3]}")

#1.2访问列表的切片(左闭右开)
myTest=['a','b','c','e','f']
print("列表的第1-2个元素",myTest[0:1])
print("列表的第x-3个元素",myTest[:2])
print("列表的第2-4个元素",myTest[1:3])
print("列表的第2-x个元素",myTest[1:])
print("列表的全部元素",myTest[:])
print("列表的第-2：x个元素",myTest[-2:])
print("列表的第1-6个元素，且步长为2",myTest[0:5:2])

#1.3遍历列表for
myTest=['a','b','c','e','f']
for letter in  myTest:
    print(letter,end="")

#2更新列表
#2.1新增元素
testList=['x','y','z']
#末尾新增
testList.append("o")
print(testList)
#指定位置插入元素
testList.insert(2,"k")
print(testList)

#2.2修改元素
testList=['x','y','z']
testList[1]="o"
print(testList)

#3删除元素
#3.1 del删除
testList=['x','y','z','o']
del testList[3]
print(testList)

#3.2 pop弹出元素
testList=['x','y','z','o']
popTest = testList.pop();
print(popTest)
print(testList)

#3.3 pop弹出指定位置元素
testList=['x','y','z','o']
popTest=testList.pop(2)
print(popTest)
print(testList)

#4 列表排序
#4.1字母顺序排序
cars=['ac','aa','ba','ab']
cars.sort()
print(cars)

#4.2字母顺序反序
cars=['ac','aa','ba','ab']
cars.sort(reverse=True)
print(cars)

#4.3临时排序
cars=['ac','aa','ba','ab']
cars2=sorted(cars)
print(cars)
print(cars2)

#反转列表
cars=['ac','aa','ba','ab']
cars.reverse()
print(cars)

#5len()与range()/list()
#5.1 列表长度len
cars=['ac','aa','ba','ab']
print(len(cars))

#5.2 range()与list()一起使用
print(list(range(6)))
print(list(range(0,6)))
print(list(range(2,5)))
print(list(range(0,8,2)))

#6 练习创建一个包含1-10平方的列表
#6.1 for循环
squares=[]
for i in range(1,11):
    x=i*i
    squares.append(x)
print(squares)

#6.2列表解析
squares=[]
squares = [value**2 for value in range(1,11)]
print(squares)

#7 复制列表两种方式
#7.1、直接赋值：相同对象
myfoods=['a','b','c']
myfoods2=myfoods
myfoods[0]="A"
print(myfoods)
print(myfoods2)

#7.2 重复复制：不同对象
myfoods=['a','b','c']
myfoods2=myfoods[:]
myfoods[0]="A"
print(myfoods)
print(myfoods2)

#8 元组：不可变的列表
#8.1 查看元组内容
dimensions=(200,50)
print(type(dimensions))
print(dimensions[0])
print(dimensions)

#8.2 遍历元组
dimensions=(200,50)
for dimension in dimensions:
    print(dimension)

#8.3 修改元素值
dimensions=(200,50)
dimensions=(400,100)
print(dimensions)

