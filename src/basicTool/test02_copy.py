#1、直接赋值：相同对象
myfoods=['a','b','c']
myfoods2=myfoods
#改变myfood
myfoods[0]='A'
print(myfoods)
print(myfoods2)

#2、重新赋值：不同对象
myfoods=['a','b','c']
myfoods3=myfoods[:]
#改变myfood
myfoods[0]='A'
print(myfoods)
print(myfoods3)