import random
i = 0
number = random.randint(1,100)#随机出来一个数字
while i < 10:
	#执行代码
	py = int(input("请输入数字"))#用户输入数字
#判断
	if py > number:
		print("输入大了")
	elif py < number:
		print("输入小了")
	else:
		print("猜对了")
		i  = 10 #停止循环
	i+=1




