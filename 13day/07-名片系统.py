list = []#存放名字

print("名片管理系统".center(50,"*"))

while True:
    print("1:添加名片".center(50," "))
    print("2:查找名片".center(50," "))
    print("3:修改名片".center(50," "))
    print("4:删除名片".center(50," "))
    print("5:退出".center(50," "))
    num = int(input("请选择功能"))
    if num  == 1:
        d = {}#空字典
        name = input("请输入要添加的名字")
        job = input("请输入要添加的职位")
        phone = input("请输入手机号")
        d["name"] = name
        d["job"] = job
        d["phone"] = phone

        #添加到列表
        list.append(d)
        print(list)

