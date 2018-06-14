for i in range(2,101):
	#i 49
	#i 5
	flag = 1  #假设2-101之间全是素数
	for j in range(2,i):#验证我的假设`
		if i%j == 0:
			flag = 0
			break

	if flag == 1:#假设成立
		print(i)
