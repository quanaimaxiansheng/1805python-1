a = 2#全局变量 定义函数外部叫全局变量
def show():
    a = 1#局部变量 定义函数里面就局部变量
    #这个a跟外面的a没有关系，只是名字一样而已    
    #全局和局部变量名字不要一样

#show()
#`print(a)


a = 100
def show1(a):
    a = 200#定义局部变量

#show1(a)
#print(a)    


a = 30
def show2():
    global a#生命下面的变量修改的是全局的
    a = 40#因为上面有global声明，所以这修改的就是全局变量，而不是定义了一个局部变量

#show2()
#print(a)

list = []
def add():
    #global list
    list.add(1)#因为列表是可变类型数据，不需要太声明global

add()

