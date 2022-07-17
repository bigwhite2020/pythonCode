#读取文件的内容
#绝对路径
# file_path='D:/Users/Mr.White/PycharmProjects/pythonProject/data/pi_digits.txt'
# with open(file_path) as file_object:
#     contents = file_object.read()
# print(contents.rstrip())

#相对路径
# with open('../data/pi_digits.txt') as file_object:
#     contents = file_object.read()
# print(contents.rstrip())

#for循环逐行读取
# with open('../data/pi_digits.txt') as file_object:
#     for line in file_object:
#         print(line.rstrip())

#readline()方法
# with open('../data/pi_digits.txt') as file_object:
#     lines=file_object.readlines()
# for line in lines:
#     print(line.rstrip())

#拼接字符串读取
# with open('../data/pi_digits.txt') as file_object:
#     lines=file_object.readlines()
# pi_string=''
# for line in lines:
#     pi_string+=line.strip()
# print(pi_string)
# print(len(pi_string))

#读取大型文件
with open( '../../data/pi_million_digits.txt' ) as file_object:
    lines=file_object.readlines()
pi_string=''
for line in lines:
    pi_string+=line.strip()
print(f"{pi_string[:51]}...")
print(len(pi_string))