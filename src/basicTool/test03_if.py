#if-else语句
cars=['audi','bmw','toyota']
for car in cars:
    if car=='bmw':
        print(car.upper())
    else:
        print(car.title())


#if-elif-else语句
age=12
if(age<4):
    print("Your admission cost is $0.")
elif(age<18):
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")