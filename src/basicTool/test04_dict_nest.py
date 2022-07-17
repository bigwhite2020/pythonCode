#1、列表套字典
alien_0={'color':'green','point':5}
alien_1={'color':'yellow','point':10}
list1=[alien_0,alien_1]
print(list1)
for alien in list1:
    print(alien)
print("-------split----------")
#2、字典套列表
testList=['myok1','myok2']
testDict={'task1':'mydict','task2':testList}
print(testDict)
for list1 in testDict['task2']:
    print(list1)
print("-------split----------")
#3、字典套字典
alien_0={'color':'green','point':5}
alien_1={'color':'yellow','point':10}
aliens={'fisrt':alien_0,'second':alien_1}
print(aliens)
for a,b in aliens['second'].items():
    print(f"{a}:{b}")