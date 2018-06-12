i = 1
a_sum = 0
while i < 100:
	if i % 2 == 0:
		a_sum = a_sum - i #偶数减
	else:
		a_sum = a_sum + i #奇数加
	
	i+=1

print(a_sum)#50		
