str ="laowang"
'''
for i  in str:
	print(i)
'''

#range
'''
for i in range(起始值,终止值,步长):
'''
# random.randint 有头有尾
# range()有头无尾
for i in range(10):
	#print(i)
	pass

for i in range(0,10):
	#print(i)
	pass

for i in range(0,10,2):
	#print(i)
	pass

for i  in range(0,10,-1):
	#print(i)
	pass

for i in range(10,-1,-1):
	#print(i)
	pass

for i  in range(101):
	if  i == 88:
		#break
		continue
	print(i)
