print("请选择游戏")
game = input("1:王者荣耀 2:植物大战僵尸")
account = "123456"
pwd = "123456"
if game == "1":
	acc = input("请输入账号")
	p = input("请输入密码")
	if acc == account and p == pwd:
		print("登录成功\n欢迎来到王者峡谷")
	else:
		print("登录失败")
elif game == "2":
	print("一大波僵尸正在来袭")
else:
	print("sorry do not have the game")
