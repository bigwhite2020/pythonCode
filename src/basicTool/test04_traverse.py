#1、遍历字典的键值对
alien_0={'color':'green','point':5}
for a,b in alien_0.items():
    print(f"key:{a}")
    print(f"value:{b}")
#查看结果:
print("-------split----------")
#2、遍历字典的所有键
alien_0={'color':'green','point':5}
for a in alien_0.keys():
    print(f"key:{a}")
#查看结果:
print("-------split----------")
#3、遍历字典的所有值
alien_0={'color':'green','point':5}
for a in alien_0.values():
    print(f"value:{a}")
#查看结果:
print("-------split----------")
#4、遍历并去重字典的值
alien_0={'test01':1,'test02':1,'test03':2,'test04':2,'test05':3,'test06':3,}
for a in set(alien_0.values()):
    print(f"key:{a}")
#查看结果:
print("-------split----------")