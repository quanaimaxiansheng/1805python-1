account = input("请输入账号")
pwd = input("请输入密码")
print("欢迎光临您的个人银行\n祝你花钱愉快")
money = 100000
#如果计算128天的利息
other_money = 0.04/365*128*money
print("你的个人资产:%d,昨天收益大概是%d"%(money,other_money))
need_money = int(input("请输入取款金额"))
#判断钱够不够
f_money = money+other_money-need_money
print("剩余金额:%d"%f_money)



