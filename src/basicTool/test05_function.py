# def green_user():
#     """显示简单的问候语"""
#     print("hello world")
# green_user()
#
# def green_user(username):
#     """显示简单的问候语"""
#     print( f"Hello,{username.title()}!" )
# green_user("Lucy")

# def describe_pet(animal_type,pet_name):
#     """显示宠物的信息"""
#     print(f"I have a {animal_type}")
#     print(f"My {animal_type}'s name is {pet_name}")
# describe_pet('dog','Mary')
# describe_pet('cat','Little White')

# def describe_pet(animal_type,pet_name):
#     """显示宠物的信息"""
#     print(f"I have a {animal_type}")
#     print(f"My {animal_type}'s name is {pet_name}")
# describe_pet(animal_type='dog',pet_name='Mary')

#默认值
# def describe_pet(pet_name,animal_type='cat'):
#     """显示宠物的信息"""
#     print(f"I have a {animal_type}")
#     print(f"My {animal_type}'s name is {pet_name}")
# describe_pet(pet_name='Mary')
# describe_pet('Big White')

#返回值
# def get_formatted_name(first_name,last_name):
#     """返回全名，并且首字母大写"""
#     full_name=f"{first_name} {last_name}"
#     return full_name.title()
# name=get_formatted_name("mike","jackson")
# print(name)
#
# #实参可选
# def get_formatted_name(first_name,middle_name,last_name):
#     """返回全名，并且首字母大写"""
#     full_name=f"{first_name} {middle_name} {last_name}"
#     return full_name.title()
# name=get_formatted_name("mike","jackson")
# print(name)

#同时满足以上两种
# def get_formatted_name(first_name,last_name,middle_name=''):
#     """返回全名，并且首字母大写"""
#     full_name=f"{first_name} {middle_name} {last_name}"
#     return full_name.title()
# name1=get_formatted_name("mike","jackson",'midddd')
# name2=get_formatted_name("mike","jackson")
# print(name1)
# print(name2)

#返回字典
# def build_person(first_name,last_name):
#     """返回一个字段"""
#     persion={'first':first_name,'last':last_name}
#     return persion
# dicttest1=build_person('xiao','long')
# print(dicttest1)

#function+while
# def get_formatted_name(first_name,last_name):
#     """返回全名，并且首字母大写"""
#     full_name=f"{first_name} {last_name}"
#     return full_name.title()
# while True:
#     print("Please tell me your name:")
#     print("（enter 'q' at any time to quit）")
#     f_name=input("First name:")
#     if f_name=='q':
#         break
#     l_name=input("Last name:")
#     if l_name=='q':
#         break
#     formatted_name=get_formatted_name('mike','jackson')
#     print(f"\nhello,{formatted_name}!")


#传递列表
# def greet_users(names):
#     """向列表中的每位用户发出简单的问候"""
#     for name in names:
#         msg=f"Hello,{name.title()}!"
#         print(msg)
# username=['bk','anna','tom','mary']
# greet_users(username)

# 在函数中修改列表，处理用户认证
# unconfirmed_users=['alice','brian','candace']
# confirmed_users=[]
#
# def confirmed(unconfirmed_users,confirmed_users):
#     while unconfirmed_users:
#         current_user = unconfirmed_users.pop()
#         print( f"Verfying users:{current_user.title()}" )
#         confirmed_users.append( current_user )
#     # 显示所有验证的用户
# def print_confirmed_users(confirmed_users):
#     print( "\nThe following users have been confirmed!" )
#     for confirm_user in confirmed_users:
#         print( confirm_user.title() )
#
# confirmed(unconfirmed_users,confirmed_users)
# print_confirmed_users(confirmed_users)
# print(unconfirmed_users)

#禁止函数修改列表
#将列表的副本传递给函数
# unconfirmed_users=['alice','brian','candace']
# confirmed_users=[]
#
# def confirmed(unconfirmed_users,confirmed_users):
#     while unconfirmed_users:
#         current_user = unconfirmed_users.pop()
#         print( f"Verfying users:{current_user.title()}" )
#         confirmed_users.append( current_user )
#     # 显示所有验证的用户
# def print_confirmed_users(confirmed_users):
#     print( "\nThe following users have been confirmed!" )
#     for confirm_user in confirmed_users:
#         print( confirm_user.title() )
#
# confirmed(unconfirmed_users[:],confirmed_users)
# print_confirmed_users(confirmed_users)
# print(unconfirmed_users)

#传递任意数量的实参
#*号可以生成一个空元组，封装接收的所有值
# def make_pizza(*toppings):
#     """打印顾客点的所有配料"""
#     print(toppings)
# make_pizza('pepperoni')
# make_pizza('mushrooms','chesse','green peppers')

#结合使用位置实参和任意数量实参
def make_pizza(size,*toppings):
    """打印顾客点的所有配料"""
    print(f"Making a {size}-inch pizza with the folowing toppings")
    for topping in toppings:
        print(f'-{topping}')
# make_pizza(16,'pepperoni')
# make_pizza(12,'mushrooms','chesse','green peppers')

# 十、使用任意数量的关键字实参
#**可以生成一个空字典
# def build_profile(first,last,**user_info):
#     """创建一个字典，其中包含有关用户的信息"""
#     user_info['first_name']=first
#     user_info['last_name']=last
#     return user_info
# user_profile=build_profile('albert','master',location='princeton',field='physics',number=1)
# print(user_profile)