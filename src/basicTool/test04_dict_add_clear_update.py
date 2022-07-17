#1、访问字段
alien_0={'color':'green','point':5}
print(alien_0['color'])
print(alien_0.get('point'))
#查看结果：
print("-------split----------")

#2、更新字典
alien_0={'color':'green','point':5}
alien_0['x_postion']=0
alien_0['y_postion']=25
alien_0['color']='yellow'
print(alien_0)
#查看结果：
print("-------split----------")

#3、删除键值对
alien_0={'color':'green','point':5}
del alien_0['color']
print(alien_0)
#查看结果：
print("-------split----------")
