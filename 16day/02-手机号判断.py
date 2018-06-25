'''
把手机号验证的功能是不是拆除来了
'''
def register(account,pwd):
    a = isPhone(account)
    if a:
        print("呵呵呵")

def login(account,pwd):
    result = isPhone(account)
    if result:
        print("哈哈哈")

def isPhone(account):#判断手机号合法不合法
    if len(account) == 11 and account.startswith("1"):
        return True
    else:
        return False


'''
当前有多个函数里面有相同重复的功能的时候，这个时候应该考虑独立封装成一个函数，方便多个函数去调用
'''

register("18612345678","122")
login("18612345678","122")
