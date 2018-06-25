def show(a):
    a = a+a
    print("内部的%d"%a) 
x = 1
#show(x)
#print("外部的%d"%x)

def show1(a):
    a+=a
    print("内部的%d"%a) 
x = 1
#show1(x)
#print("外部的%d"%x)


def show2(a):
    a+=a
    print(a)#[1,2,1,2] 
x = [1,2]
#show2(x)[1,2,1,2]
#print(x)

def show3(a):
    a = a+a
    print(a) 
x = [1,2]
show3(x)
print(x)


'''
a = a+a 先算右边，然后找一个新的变量，然后把值赋予给他
a+=a a本来事先已经有个指向的引用，对于可变类型数据来说，改的是引用指向的那个值

a = a+a 和a+=a对于不可变类型数据来说，没有任何影响，相当于一样
'''




