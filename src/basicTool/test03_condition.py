#1、忽略大小写
car='Audi'
print(car=='audi')
print(car.lower()=='audi')
print(car.upper()=='AUDI')
#查看运行结果：
print('----分割线-----------')
#2、检查不相等
car='Audi'
print(car !='AUDI')
#查看运行结果：
print('----分割线-----------')

#3、检查多个条件
age_0=22
age_1=18
print(age_0>=21 and age_1>=21)
print((age_0>=21) and (age_1<21))
print(age_0>=21 or age_1>=21)
#查看运行结果：
print('----分割线-----------')

#4、检查特定值是否包含在列表中
testList=['A','B','C']
print('A' in testList)
print('D' not in testList)
#查看运行结果：
print('----分割线-----------')

#5、检查列表是否为空
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
#查看运行结果：
print('----分割线-----------')