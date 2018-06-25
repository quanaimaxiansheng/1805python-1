s = "老王"#全局变量
'''
如果你想用函数去修改全局变量的时候，这个时候在函数内部一定要声明global,否则改不了。但是对于可变类型来说，可以不声明golbal 如：list dict
'''
def change_name():
    global s
    s = "老宋"


change_name()
print(s)
