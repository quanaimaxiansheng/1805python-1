x = int(input("请输入x值"))
y = int(input("请输入y值"))

c = input("请输入+-*/")

if c == "+":
	z = x+y
	print("%d+%d=%d"%(x,y,z))
elif c == "-":
	z = x-y
	print("%d-%d=%d"%(x,y,z))
elif c == "*":
	z = x*y
	print("%d*%d=%d"%(x,y,z))
elif c == "/":
	if y != 0:
		z = x/y
		print("%d/%d=%.02f"%(x,y,z))
	else:
		print("输入有误")
