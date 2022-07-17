# prompt="Tell me a city you want got to."
# prompt+="\nEnter 'quit' to be end the program:"
# while True:
#     city=input(prompt)
#     if city=='quit':
#         break
#     else:
#         print(f"You love to go to {city.title()}!")

#打印1-10之间的奇数
current_number=0
while current_number<10:
    current_number+=1
    if current_number%2==0:
        continue
    else:
        print(current_number)