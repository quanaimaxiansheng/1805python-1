import random
all_money = 0 #消费总钱数

for i in range(1,31):#每月30天
	for j in range(1,3):#每天2次
		km = 34
		if km <= 6:#小于6公里
			price = 3#单价
		elif km > 6 and km <=12:
			price = 4
		elif km > 12 and km <=22:
			price = 5
		elif km > 22 and km <= 32:
			price = 6
		elif km > 32:
			if (km-32)%20 == 0:
				price = 6+(km-32)/20
			else:
				price = 6+int((km-32)/20)+1
		#打折逻辑
		if all_money > 100 and all_money <= 150:
				price = price*0.8
		elif all_money > 150 and all_money <=400:
				price = price *0.5
	
		all_money = all_money + price

print("总钱%.02f"%all_money)
