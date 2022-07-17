# 处理用户认证的列表
# unconfirmed_users=['alice','brian','candace']
# confirmed_users=[]
# while unconfirmed_users:
#     current_user=unconfirmed_users.pop()
#     print(f"Verfying users:{current_user.title()}")
#     confirmed_users.append(current_user)
# #显示所有验证的用户
# print("\nThe following users have been confirmed!")
# for confirm_user in confirmed_users:
#     print(confirm_user.title())

#删除指定元素的列表
# pet=['dog','cat','pig','cat','triger','rabbit']
# print(f"删除前:{pet}")
# while 'cat' in pet:
#     pet.remove('cat')
# print(f"删除后：{pet}")

#使用字段记录问卷调差
mydict={}
active=True
while active:
    name=input("Please enter your name:")
    city=input("Please enter what city you want go to:")
    mydict[name]=city
    next=input("Do you want to send this questionnaire to another people(yes/no):")
    if next=='no':
        break
print("The questionnaire is over,now the result is:")
for name,city in mydict.items():
    print(f"{name.title()} want go to {city.title()}!")