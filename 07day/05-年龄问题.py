age = int(input("请输入年龄"))
sex = input("请输入性别")
#假如是女孩并且大于15岁 才能玩游戏
#假如是男孩

# 17岁  男

if age > 15 and sex =="女":
	print("可以玩游戏")
elif age > 18 or sex == "男":
	print("回家种地") 
else:
	print("哈哈哈哈哈哈哈哈哈")
