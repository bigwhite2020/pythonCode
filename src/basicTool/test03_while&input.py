# prompt="Tell me something,and I will repeat it back to you:"
# prompt+="\nEnter 'quit' to be end the program."
# message=""
# while message!='quit':
#     message=input(prompt)
#     if message!='quit':
#         print(message)

prompt="Tell me something,and I will repeat it back to you:"
prompt+="\nEnter 'quit' to be end the program."
#设置标志
active=True
while active:
    message=input(prompt)
    if message=='quit':
        active=False
    else:
        print(message)