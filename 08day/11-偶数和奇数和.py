o_sum = 0
j_sum = 0
i = 0
while i <=100:
	#print(i)
	if i % 2==0:#偶数
		o_sum = o_sum+i
	else:
		j_sum = j_sum+i
	i+=1

print("偶数的和是%d"%o_sum)
print("奇数的和是%d"%j_sum)
