'''
i = 1
while i < 24:
	print("玩游戏%d小时"%i)
	if i == 8:#当你玩8小时的时候 父亲来了，回去一顿揍
		print("your father come here ")
		#break#终止循环
	i+=1
'''
j = 0
while j < 23:
	j+=1
	if j == 8:
		print("you father come here")
		continue
	print("玩游戏%d"%j)	

