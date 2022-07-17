myTest=['a','b','c']
#访问列表元素
#直接访问
print(myTest[0])
print(myTest[-1])
print(f"my letter is {myTest[1]}")
myTest=['a','b','c','e','f']
#访问切片,左闭右开
print(myTest[0:1])
print(myTest[:2])
print(myTest[1:3])
print(myTest[1:])
print(myTest[:])
print(myTest[-2:])
print(myTest[0:5:2])#取对应步长
#遍历列表
myTest=['a','b','c','e','f']
for letter in myTest:
    print(letter)