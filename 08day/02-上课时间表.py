print("1:星期一\n2:星期二\n3:星期三\n4:星期四\n5:星期五\n6:星期六\n7:星期天")
number = int(input("请输入星期几(可以用序号)"))

if number >= 1 and number <= 5:
	day = int(input("请输入1:上午 2:下午"))
	if day == 1:#上午
		time = int(input("请输入时间"))
		if time > 8 and time < 11:
			print("正在学习") 
		else:
			print("我也不知道自己干什么")
	else:
		time = int(input("请输入时间"))
		if time > 14 and time < 17:
			print("正在学习") 
		else:
			print("我也不知道自己干什么")
elif number  == 6:
	print("全天上课")
elif number == 7:
	print("逛街")

