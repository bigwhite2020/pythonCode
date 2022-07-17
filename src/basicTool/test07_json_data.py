import json
#写入数据
# number=[2,3,5,7,11,13]
# filename='../data/number.json'
# with open(filename,'w') as f:
#     json.dump(number,f)
#

#读取数据
# filename='../data/number.json'
# with open(filename) as f:
#     numbers=json.load(f)
# print(numbers)

#保存与读取用户输入
# username=input("What is your name?")
# filename='username.json'
# with open(filename,'w') as f:
#     json.dump(username,f)
#     print(f"We'll remember you when you come back,{username}!")
# with open(filename) as f:
#     username=json.load(f)
#     print(f"Welcom back,{username}")

#重构
def get_stored_username():
    """当没有错误时读取保存的用户名"""
    filename='username.json'
    try:
        with open(filename) as f:
            username=json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """验证新用户名"""
    username=input("What is your name?")
    filename='username.json'
    with open(filename,'w') as f:
        json.dump(username,f)
    return username

def greet_user():
    """greet the user by name"""
    username=get_stored_username()
    if username:
        print(f"Welcome back,{username}!")
    else:
        username=get_new_username()
        print(f"We will remember you when you come back,{username}!")

greet_user()