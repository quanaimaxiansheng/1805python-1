import random
number = random.randint(1,100)

count = 0
for i in range(10):
	user =  int(input("请输入数字"))
	if user > number:
		print("猜大了")
	elif user < number:
		print("猜小了")
	else:
		print("猜对了")
		break
	count+=1#猜的次数

if count == 1:
	print("大神")
elif count > 1 and count < 5:
	print("半仙")
elif count >=5 and count < 9:
	print("修仙")
elif count >=9 and count == 10:
	print("23333")
