print("商品管理系统".center(40,"*"))
goods = []#商品列表[["卫龙",5],["可乐"，5]]
while True:#可以无限添加商品
    print("1、添加商品")
    print("2、查找商品")
    print("3、修改商品")
    print("4、删除商品")
    print("5、退出系统")
    number = int(input("请选择功能"))
    if number == 1:
        good = []#里面的小列表
        name = input("请输入时商品名字")
        price = float(input("请输入商品价格"))
        good.append(name)
        good.append(price)
        #加入大列表
        goods.append(good)
        print(goods)
    elif number == 2:
        #goods = [["可乐",5],["雪碧"，4]]
        name = input("请输入你要查找的商品名字")
        for  n in goods:
             if name  ==  n[0]:
                print("商品名字是%s,价格是%.02f"%(name,n[1]))
                break
    elif number == 3:
        name = input("请输入你要修改的商品名字")
        for n in goods:
            if name == n[0]:
                print("1、修改名字")
                print("2、修改价格")
                print("3、修改名字和价格")
                nu = int(input("请选择功能")) 
                if  nu == 1:
                    name = input("请输入新的名字")
                    #xx[position]  = name
                    n[0] = name
                elif nu == 2:
                    price = float(input("请输入价格"))
                    n[1] = price 
                elif nu == 3:
                    name = input("请输入新的名字")
                    price = float(input("请输入价格"))
                    n[0] = name
                    n[1] = price 
                break
        print(goods)
    elif number == 4:
        name = input("请输入要删除的名字")
        for position,l in enumerate(goods):
            if name == l[0]:
                goods.pop(position)
                print(goods)
                break
    elif number == 5:
        break




