#声明函数
def jisuanqi(x,y,z):#形参
    if z == "+":
        print("和是%d"%(x+y))
    elif z == "-":
        print("差是%d"%(x-y))
    elif z == "*":
        print("积是%d"%(x*y))
    elif z == "/":
        if y != 0:
            print("商是%f"%(x/y))
        else:
            print("不合法")

x = int(input("请输入x值"))
y = int(input("请输入y值"))
laowang = input("请输入+-*/")
jisuanqi(x,y,laowang)#实参  python当中是按照引用传递



