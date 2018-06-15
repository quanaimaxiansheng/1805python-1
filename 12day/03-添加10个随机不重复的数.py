import random
list = []

while len(list) < 10 :
    number = random.randint(1,100)
    if number in list:
        print("重复了%d"%number)
        continue
    list.append(number)

print(list)
    
