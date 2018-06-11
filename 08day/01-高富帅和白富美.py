sex = input("请输入性别")
if sex == "男":
	height = int(input("请输入身高"))
	money = int(input("请输入身价"))
	face = int(input("请输入颜值"))
	if height > 170 and money >1000 and face > 90:
		print("你是高富帅")
	else:
		print("呵呵")
elif sex == "女":
	white = input("请输入皮肤颜色")
	money = int(input("请输入身价"))
	face = int(input("请输入颜值"))
	if white =="白" and money > 1000 and face > 90:
		print("白富美") 
	else:
		print("不哭...")
