testList=['x','y','z','o']
#删除指定位置元素
del testList[0]
print(testList)

#删除并弹出最后一个元素
testList=['x','y','z','o']
popTest= testList.pop();
print(popTest)
print(testList)

#删除并弹出指定位置元素最后一个元素
testList=['x','y','z','o']
popTest= testList.pop(2);
print(popTest)
print(testList)