list = []#名片容器

#专人专责 这个函数就检查名字是否合法
def check_name(name):
    if len(name) > 2 and len(name) < 5:
        return True
    else:
        return False

#玩游戏
def play_game():
    pass

#打印名片
def print_card():
    print("名字\t职位")
    for i  in list:
        print(" %s\t %s"%(i["name"],i["job"]))

#删除名片
def del_card():
    pass

#修改名片
def fix_card():
    name =  input("请输入要修改的名字")
    flag = False#默认没有此人
    for i  in list:
        if name == i["name"]:
            flag = True
            print("1:修改名字")    
            print("2:修改职位")
            n = int(input("请选择序号"))
            if n == 1:
                name = input("请输入名字")
                i["name"] = name
                print("修改成功")
            elif n == 2:
                job = input("请输入新的职位")
                i["job"] = job
                print("修改成功")
    if flag == False:
        print("查无此人")            
#查找名片
def find_card():
    '''
    可以根据名字 
    可以根据电话找
    '''
    name = input("请输入要查找的名字")
    flag = False#默认没有找到
    for i in list:
        if name == i["name"]:
            flag = True
            print("名字:%s\n职位%s"%(i["name"],i["job"]))
    if flag == False:
        print("查无此人")

#添加名片
def add_card():
    ''' 
    添加的时候，手机号不能重复
    '''
    dict = {}#初始化字典
    name = input("请输入名字")
    job = input("请输入职位")
    
    #检查一下名字合法不合法
    result = check_name(name)
    if result == False:
        print("格式化有误")
        return
    #构建字典
    dict["name"] = name
    dict["job"] = job
    
    #加入到列表
    list.append(dict)    



#菜单函数
def print_menu():
    print("1:添加名片")
    print("2:查找名片")
    print("3:修改名片")
    print("4:删除名片")
    print("5:打印名片")
    print("6:游戏功能")
    print("7:退出系统")


#主入口函数
def  main():
    print("欢迎使用名片管理系统".center(50,"*"))
    while True:
        print_menu()
        num = int(input("请选择功能"))
        if num == 1:
            add_card()
        elif num == 2:
            find_card()
        elif num == 3:
            fix_card()
        elif num == 4:
            del_card()
        elif num == 5:
            print_card()
        elif num == 6:
            play_game()
        elif num == 7:
            break
#调用函数
main()    
