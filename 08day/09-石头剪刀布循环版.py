"
两个人玩的游戏
电脑
普通玩家
1代表石头
2代表剪刀
3代表布
"""
import random#导入随机工具只导入一次
i = 0#作为while条件
while i < 3:
	pc = random.randint(1,3)#每次随机生产一个数字大小是1-3之间
	py = int(input("请输入1:石头2:剪刀3:布"))#用户输入的

#下面代码判断谁赢谁输
	if py > 0 and py < 4:#大条件
		if (py == 1 and pc == 2) or (py == 2 and pc == 3) or (py == 3 and pc == 1):
			print("玩家赢了")#注意缩进
		elif py == pc:
			print("平局")#注意缩进
		else:
			print("电脑赢了")#注意缩进
	else:
		print("输入有误")		

	i+=1#每次加上1让while最多执行三遍

