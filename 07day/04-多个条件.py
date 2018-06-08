age = int(input("请输入年龄"))

if age <8:
	print("在家愉快的玩耍")

if age > 8 and age < 15:
	print("在外求学")

if age >= 15 and age < 20:
	print("上大学了")

if age >=20:
	print("成家立业了")

#--------------华丽分割线-----------------

if age < 8:
	print("在家")
elif age > 8 and age <15:
	print("求学")
elif age >=15 and age < 20:
	print("上大学")
elif age >=20:
	print("成家立业") 
