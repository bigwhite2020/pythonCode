# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("You can't divide by zero!")

# filename="testfile.txt"
# try:
#     with open(filename,encoding='utf-8') as f:
#         contents=f.read()
# except FileNotFoundError:
#     print(f"sorry,the file {filename} does not exits.")


try:
    print(5/0)
except ZeroDivisionError:
    pass
