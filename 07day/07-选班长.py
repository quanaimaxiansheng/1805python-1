import  random
import time
c = 0
l = 0 
m = ["柴子健","李宁"]

for i in range(3):
	time.sleep(3)
	print("正在努力选班长")
	count = random.randint(0,100)
	if count%2 == 0:
		c+=1 #c = c+1
	else:
		l+=1 #l = l+1

if c > l:
	print("班长:%s"%m[0])
else:
	print("副班长:%s"%m[1])
